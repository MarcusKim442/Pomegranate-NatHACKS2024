import time
import threading
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter
from brainflow.exit_codes import BrainFlowError


# Global variable to track if streaming should continue
keep_running = True


def user_input_handler():
    """
    Function to handle user input for stopping the program.
    Runs on a separate thread to avoid blocking the main program.
    """
    global keep_running
    input("Press Enter to stop streaming...\n")
    keep_running = False


def main():
    # Enable BrainFlow logging
    BoardShim.enable_dev_board_logger()

    # Setup parameters for USB dongle connection
    params = BrainFlowInputParams()
    params.serial_port = "COM3"  # Confirm COM3 is correct
    params.timeout = 15  # Increase timeout for initialization

    # Start a separate thread to monitor for user input
    input_thread = threading.Thread(target=user_input_handler)
    input_thread.daemon = True
    input_thread.start()

    # Initialize the board
    try:
        board = BoardShim(BoardIds.GANGLION_BOARD.value, params)
        board.prepare_session()
        print("Session prepared successfully.")

        # Start streaming data
        board.start_stream()
        print("Streaming data. Press Enter to stop...")

        while keep_running:
            # Retrieve the latest 10 samples
            data = board.get_current_board_data(20)

            # Save to file in append mode
            DataFilter.write_file(data, "live_data.csv", "a")
            print("Data saved to live_data.csv")

            # Optional: Print data shape for debugging
            print(f"Data shape: {data.shape}")

            # Sleep to control data retrieval rate
            time.sleep(1)

    except BrainFlowError as e:
        print(f"BrainFlowError: {e}")

    except KeyboardInterrupt:
        print("Stopping stream manually...")

    finally:
        # Stop streaming and release resources
        if "board" in locals() and board.is_prepared():
            board.stop_stream()
            board.release_session()
            print("Session released.")


if __name__ == "__main__":
    main()
