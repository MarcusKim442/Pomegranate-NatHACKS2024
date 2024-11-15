import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter


def main():
    # Enable BrainFlow logging
    BoardShim.enable_dev_board_logger()

    # Setup parameters for USB dongle connection
    params = BrainFlowInputParams()
    params.serial_port = "COM3"  

    # Initialize the board
    board = BoardShim(BoardIds.GANGLION_BOARD.value, params)  
    board.prepare_session()

    # Start streaming data
    board.start_stream()
    print("Streaming data. Press Ctrl+C to stop...")

    try:
        while True:
            # Retrieve latest 256 samples
            data = board.get_current_board_data(256)

            # Save to file
            DataFilter.write_file(data, "live_data.csv", "a")
            print("Data saved to live_data.csv")

            # Optional: Print data shape for debugging
            print(data.shape)

            # Sleep to control data retrieval rate
            time.sleep(1)

    except KeyboardInterrupt:
        print("Stopping stream...")

    finally:
        # Stop streaming and release resources
        board.stop_stream()
        board.release_session()
        print("Session released. Goodbye!")


if __name__ == "__main__":
    main()
