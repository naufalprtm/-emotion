import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_to_csv(data, filename):
    """Save data to a CSV file."""
    data.to_csv(filename, index=False)
