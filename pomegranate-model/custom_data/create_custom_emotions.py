import pandas as pd

def combine_csv_with_labels(positive_file, neutral_file, negative_file, output_file):
    positive_df = pd.read_csv(positive_file)
    neutral_df = pd.read_csv(neutral_file)
    neutral_df_double = pd.read_csv(neutral_file)
    negative_df = pd.read_csv(negative_file)
    negative_df_double = pd.read_csv(negative_file)

    positive_df['label'] = 'POSITIVE'
    neutral_df['label'] = 'NEUTRAL'
    neutral_df_double['label'] = 'NEUTRAL'
    negative_df['label'] = 'NEGATIVE'
    negative_df_double['label'] = 'NEGATIVE'

    combined_df = pd.concat([positive_df, neutral_df, negative_df], ignore_index=True)
    shuffled_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)
    shuffled_df.to_csv(output_file, index=False)
    print(f"CSV saved to {output_file}")

# Example usage
combine_csv_with_labels('positive_fullfeatures.csv', 'neutral_fullfeatures.csv', 'negative_fullfeatures.csv', 'custom_emotions_artificial.csv')
