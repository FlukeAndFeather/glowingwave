#!/usr/bin/env python
"""
Script 01: Download Data

This script downloads the raw data from source and saves it to data/raw/.

Usage:
    python scripts/01_download_data.py
"""

import sys
from pathlib import Path
import requests
import geopandas as gpd

# Add src to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from src.data_utils import load_config


def download_california_current_shapefile(output_dir):
    """
    Download California Current LME shapefile from Marine Regions WFS.

    Parameters
    ----------
    output_dir : Path
        Directory to save the shapefile
    """
    print("Downloading California Current (LME #3) from Marine Regions WFS...")

    # WFS endpoint
    url = "https://geo.vliz.be/geoserver/MarineRegions/wfs"

    # Specify parameters for WFS request
    params = dict(
        service="WFS",
        version="2.0.0",
        request="GetFeature",
        typeName="MarineRegions:lme",
        outputFormat="application/json",
        cql_filter="lme_number=3"  # Filter for California Current (LME #3)
    )

    print(f"  WFS endpoint: {url}")
    print(f"  Requesting: {params['typeName']}")
    print(f"  Filter: {params['cql_filter']}")

    # Fetch data from WFS using requests
    r = requests.get(url, params=params)
    r.raise_for_status()  # Raise error if request failed

    # Create GeoDataFrame from geojson
    # Marine Regions data is in WGS84 (EPSG:4326)
    california_current = gpd.GeoDataFrame.from_features(
        r.json(),  # requests.json() parses the JSON response
        crs="EPSG:4326"
    )

    print(f"  Downloaded {len(california_current)} feature(s)")

    # Save to shapefile
    shapefile_path = output_dir / 'california_current_lme.shp'
    california_current.to_file(shapefile_path)
    print(f"  Saved to: {shapefile_path}")

    return shapefile_path


def main():
    """Download data from configured sources."""
    # Load configuration
    config = load_config('config.yaml')

    print("=" * 60)
    print("STARTING DATA DOWNLOAD")
    print("=" * 60)

    # Set up paths
    raw_data_path = Path(config['data']['paths']['raw'])
    shapefiles_dir = raw_data_path / 'shapefiles'

    # Ensure directories exist
    shapefiles_dir.mkdir(parents=True, exist_ok=True)

    # Download California Current shapefile
    print("\n1. California Current Shapefile")
    print("-" * 60)
    download_california_current_shapefile(shapefiles_dir)

    print("\n" + "=" * 60)
    print("DATA DOWNLOAD COMPLETE!")
    print("=" * 60)
    print(f"Raw data saved to: {raw_data_path}")


if __name__ == '__main__':
    main()
