import time
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

    print("Streaming data for 10 seconds...")
    time.sleep(10)
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    # Convert raw data into a DataFrame
    df = pd.DataFrame(np.transpose(data))

    # Get column indices
    timestamp_column = BoardShim.get_timestamp_channel(BoardIds.GANGLION_BOARD.value)
    eeg_channels = BoardShim.get_eeg_channels(BoardIds.GANGLION_BOARD.value)
    noise_column = BoardShim.get_marker_channel(BoardIds.GANGLION_BOARD.value)  # Use marker for noise

    # Ensure order: timestamp, 4 EEG channels, noise
    columns_to_keep = [timestamp_column] + eeg_channels[:4] + [noise_column]
    df = df.iloc[:, columns_to_keep]

    # Drop columns with all zero values
    df = df.loc[:, (df != 0).any(axis=0)]
    
    # Rename columns for clarity
    column_names = ['timestamp', 'channel_1', 'frontal_1', 'frontal_2', 'channel_4', 'noise']
    df.columns = column_names



    # Save data to CSV
    output_file = 'processed_data.csv'
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":
    main()
