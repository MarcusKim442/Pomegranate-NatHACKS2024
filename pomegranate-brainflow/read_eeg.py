import time
import csv
import argparse
import numpy as np
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardI
from brainflow.data_filter import DataFilter
# from brainflow.ml_model import MLModel, BrainFlowMetrics, BrainFlowClassifiers, BrainFlowModelParams

def main():
    BoardShim.enable_board_logger()
    DataFilter.enable_data_logger()
    # MLModel.enable_ml_logger()
    parser = argparse.ArgumentParser()
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False,
                        default=15)
    parser.add_argument('--board-id', type=int, help='board ID, use 1 for Ganglion', required=True)
    parser.add_argument('--streamer-params', type=str, help='streamer params', required=False, default='')
    parser.add_argument('--output-file', type=str, help='Output CSV file name', required=False, default='eeg_data.csv')
    args = parser.parse_args()

    params = BrainFlowInputParams()
    params.serial_port = 'COM3'
    params.timeout = args.timeout

    board = BoardShim(args.GANGLION_BOARD, params)
    # master_board_id = board.get_board_id()
    # sampling_rate = BoardShim.get_sampling_rate(master_board_id)
    # eeg_channels = BoardShim.get_eeg_channels(master_board_id)

    board.prepare_session()
    board.start_stream(45000, args.streamer_params)
    print("Collecting data... Press Ctrl+C to stop.")

    try:
        # Collect data for a specified duration
        time.sleep(10)  # Collect data for 10 seconds; adjust as needed
        data = board.get_board_data()
    finally:
        # Stop streaming and release the session
        board.stop_stream()
        board.release_session()

    timestamps = data[BoardShim.get_timestamp_channel(master_board_id)]
    with open(args.output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['Timestamp'] + [f'EEG_Channel_{ch}' for ch in eeg_channels]
        writer.writerow(header)

        for i in range(len(timestamps)):
            row = [timestamps[i]] + [data[ch][i] for ch in eeg_channels]
            writer.writerow(row)

    print(f"EEG data saved to {args.output_file}")



if __name__ == "__main__":
    main()