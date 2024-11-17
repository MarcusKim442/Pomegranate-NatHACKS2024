import os
import numpy as np
from pomapp.eeg_features import generate_feature_vectors_from_samples

def gen_training_matrix(file_path, output_file, cols_to_ignore):
    """
    Reads the csv file and assembles the training matrix with 
    the features extracted using the functions from EEG_feature_extraction.

    Parameters:
        file_path (str): file path for the CSV file to process.
        output_file (str): filename for the output file.
        cols_to_ignore (list): list of columns to ignore from the CSV

    Returns:
        None
    """
    # Initialise return matrix
    FINAL_MATRIX = None

    # Generate feature vectors without removing redundancy
    vectors, header = generate_feature_vectors_from_samples(
        file_path,
        nsamples=150,        # Use 150 samples per window
        period=1.0,  
                # state = 1,        # Use a 1-second window
        remove_redundant=True,  # Disable redundancy removal
        cols_to_ignore=cols_to_ignore
    )

    print(f"Total features generated: {vectors.shape[1]} columns")

    if FINAL_MATRIX is None:
        FINAL_MATRIX = vectors
    else:
        FINAL_MATRIX = np.vstack([FINAL_MATRIX, vectors])

    print('FINAL_MATRIX shape:', FINAL_MATRIX.shape)

    # Shuffle rows
    np.random.shuffle(FINAL_MATRIX)

    # Save to file
    np.savetxt(output_file, FINAL_MATRIX, delimiter=',',
               header=','.join(header),
               comments='')

    print(f"Output file saved to {output_file}")

if __name__ == '__main__':
    # Define the input and output file paths
    file_path = os.path.abspath("neutral.csv")  # Adjust path if needed
    output_file = "features.csv"

    # Generate the training matrix
    gen_training_matrix(file_path, output_file, cols_to_ignore=-1)
