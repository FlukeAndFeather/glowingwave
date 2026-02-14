#!/usr/bin/env python
"""
Script 01: Download Data

This script downloads the raw data from source and saves it to data/raw/.

Usage:
    python scripts/01_download_data.py
"""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.data_utils import load_config


def main():
    """Download data from configured sources."""
    # Load configuration
    config = load_config('config.yaml')

    print("Starting data download...")

    # Get data sources from config
    sources = config.get('data', {}).get('sources', {})
    raw_data_path = Path(config['data']['paths']['raw'])

    # Ensure raw data directory exists
    raw_data_path.mkdir(parents=True, exist_ok=True)

    # Download each data source
    for name, url in sources.items():
        print(f"Downloading {name} from {url}...")

        # TODO: Implement download logic
        # Example using requests:
        # import requests
        # response = requests.get(url)
        # with open(raw_data_path / f'{name}.csv', 'wb') as f:
        #     f.write(response.content)

    print("Data download complete!")
    print(f"Raw data saved to: {raw_data_path}")


if __name__ == '__main__':
    main()
