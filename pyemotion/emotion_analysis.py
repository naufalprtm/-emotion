import pandas as pd

def load_emotion_data(file_path):
    """Load emotion data from CSV."""
    return pd.read_csv(file_path)

def analyze_emotions(dataframe):
    """Analyze emotion occurrences in the DataFrame."""
    return dataframe['emotion'].value_counts()

def get_emotion_statistics(user_id):
    """Get statistics for a specific user."""
    # Assuming you have a DataFrame `df` with the relevant data
    df = load_emotion_data('data/data_emotion.csv')
    user_data = df[df['user_id'] == user_id]
    return analyze_emotions(user_data)
