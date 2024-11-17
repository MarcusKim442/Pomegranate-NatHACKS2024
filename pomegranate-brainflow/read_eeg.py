import time
import os
import numpy as np
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter


def main():
    BoardShim.enable_dev_board_logger()

    # Initialize parameters for Ganglion board
    params = BrainFlowInputParams()
    params.serial_port = "COM3"  # Update with your actual COM port
    board = BoardShim(BoardIds.GANGLION_BOARD.value, params)
    board.prepare_session()
    board.start_stream()

    # Update the recording time to match the required 1,240 seconds
    print("Streaming data for a few seconds...")
    time.sleep(180)  # 20 minutes and 40 seconds
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    # Convert raw data into a DataFrame
    df = pd.DataFrame(np.transpose(data))

    # Get channel indices for Ganglion
    timestamp_column = BoardShim.get_timestamp_channel(BoardIds.GANGLION_BOARD.value)
    eeg_channels = BoardShim.get_eeg_channels(BoardIds.GANGLION_BOARD.value)
    noise_column = 0

    # Ensure the order: timestamps, EEG channels, AUX noise
    selected_columns = [timestamp_column] + eeg_channels + [noise_column]
    df = df.iloc[:, selected_columns]

    # Rename columns for clarity
    column_names = ['timestamps', 'TP9', 'AF7', 'AF8', 'TP10', 'Right AUX']
    df.columns = column_names

    # Ensure timestamps are in floating-point format
    df['timestamps'] = df['timestamps'].astype(float)

    # Drop columns with all zero values
    df = df.loc[:, (df != 0).any(axis=0)]

    # Save processed data to CSV in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, 'processed_data.csv')
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":
    main()
