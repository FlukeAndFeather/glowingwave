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
import copernicusmarine
from shapely.geometry import box
from shapely.geometry.polygon import Polygon

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


def download_copernicus_bgc_data(
    output_dir: Path,
    start_date: str,
    end_date: str,
    ext: Polygon,
    variables: list[str]
) -> Path:
    """
    Download Copernicus biogeochemical data for specified region and time range.

    Parameters
    ----------
    output_dir : Path
        Directory to save the NetCDF file
    start_date : str
        Start date in YYYY-MM-DD format
    end_date : str
        End date in YYYY-MM-DD format
    ext : shapely.geometry.polygon.Polygon
        Bounding box as a Shapely Polygon geometry (created with shapely.geometry.box)
    variables : list[str]
        List of variable names to download (e.g., ["nppv", "zeu", "thetao"])

    Returns
    -------
    Path
        Path to the downloaded NetCDF file
    """
    print(f"Downloading Copernicus BGC data...")

    # Extract bounds from the extent
    min_lon, min_lat, max_lon, max_lat = ext.bounds

    # Dataset information
    dataset_id = "cmems_mod_glo_bgc_my_0.083deg-lmtl_P1D-i"

    print(f"  Dataset ID: {dataset_id}")
    print(f"  Date range: {start_date} to {end_date}")
    print(f"  Bounds: {min_lon}°E to {max_lon}°E, {min_lat}°N to {max_lat}°N")
    print(f"  Variables: {', '.join(variables)}")

    # Output file
    output_file = output_dir / f"copernicus_bgc_{start_date}_{end_date}.nc"

    # Download subset using copernicusmarine
    copernicusmarine.subset(
        dataset_id=dataset_id,
        variables=variables,
        minimum_longitude=min_lon,
        maximum_longitude=max_lon,
        minimum_latitude=min_lat,
        maximum_latitude=max_lat,
        start_datetime=f"{start_date}T00:00:00",
        end_datetime=f"{end_date}T23:59:59",
        output_filename=str(output_file)
    )

    print(f"  Downloaded: {output_file}")
    print(f"  Size: {output_file.stat().st_size / 1024 / 1024:.1f} MB")

    return output_file


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
    copernicus_dir = raw_data_path / 'copernicus'

    # Ensure directories exist
    shapefiles_dir.mkdir(parents=True, exist_ok=True)
    copernicus_dir.mkdir(parents=True, exist_ok=True)

    # Download California Current shapefile
    print("\n1. California Current Shapefile")
    print("-" * 60)
    download_california_current_shapefile(shapefiles_dir)

    # Download Copernicus biogeochemical data
    print("\n2. Copernicus Biogeochemical Data")
    print("-" * 60)
    # Extract bounding box from California Current shapefile
    ca_current_shapefile = gpd.read_file(shapefiles_dir / 'california_current_lme.shp')
    minx, miny, maxx, maxy = ca_current_shapefile.total_bounds
    ca_current_extent = box(minx, miny, maxx, maxy)
    download_copernicus_bgc_data(
        output_dir=copernicus_dir,
        start_date="2005-01-01",
        end_date="2024-12-31",
        ext=ca_current_extent,
        variables=["zooc", "npp"]
    )

    print("\n" + "=" * 60)
    print("DATA DOWNLOAD COMPLETE!")
    print("=" * 60)
    print(f"Raw data saved to: {raw_data_path}")


if __name__ == '__main__':
    main()
