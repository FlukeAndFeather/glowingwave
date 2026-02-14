# Data Documentation

This directory contains all data used in the Glowingwave analysis project.

## Directory Structure

- `raw/` - Original, immutable data files as downloaded from source
- `processed/` - Cleaned and processed data ready for analysis

## Data Sources

### California Current Shapefile
- **Source**: Marine Regions (www.marineregions.org)
- **Name**: Large Marine Ecosystem (LME) #3 - California Current
- **Download Date**: 2026-02-13
- **Description**: Boundary of the California Current Large Marine Ecosystem, extending from southern Baja California to the Gulf of Alaska. The California Current is one of 66 Large Marine Ecosystems (LMEs) defined by NOAA.
- **Format**: Shapefile (.shp, .shx, .dbf, .prj)
- **Size**: ~2-5 MB (compressed)
- **License**: Available for scientific and educational use
- **Citation**: Flanders Marine Institute (2019). Maritime Boundaries Geodatabase: Large Marine Ecosystems, version 1. Available online at https://www.marineregions.org/. https://doi.org/10.14159/E5D3-YQYP
- **URL**: https://www.marineregions.org/gazetteer.php?p=details&id=4418
- **Download URL**: https://www.marineregions.org/download_file.php?name=World_LME_v1.zip
- **Location in project**: `data/raw/shapefiles/`

### Global Ocean Biogeochemical Hindcast
- **Source**: Copernicus Marine Service
- **Product**: GLOBAL_MULTIYEAR_BGC_001_033 - Global Ocean Low and Mid Trophic Levels Biomass Content Hindcast
- **Dataset ID**: cmems_mod_glo_bgc_my_0.083deg-lmtl_P1D-i_202511
- **Download Date**: 2026-02-13
- **Description**: Global ocean reanalysis of zooplankton and micronekton biomass using the SEAPODYM dynamical population model. Includes net primary productivity, euphotic zone depth, sea water temperature and velocity.
- **Temporal Coverage**: January 1, 1998 to December 31, 2024 (daily)
- **Spatial Coverage**: Global ocean (80°S to 89.92°N, 180°W to 179.92°E)
- **Spatial Resolution**: 0.083° × 0.083° (~9 km at equator)
- **Format**: NetCDF-4
- **Variables**: Zooplankton and micronekton biomass, net primary productivity, euphotic zone depth, temperature, velocity
- **License**: Copernicus Marine Service Product License
- **DOI**: https://doi.org/10.48670/moi-00020
- **URL**: https://data.marine.copernicus.eu/product-detail/GLOBAL_MULTIYEAR_BGC_001_033/INFORMATION
- **Location in project**: `data/raw/copernicus/`

## Download Instructions

### Prerequisites

**Copernicus Marine Service Authentication**
- For downloading ocean data from Copernicus Marine Service, you must first authenticate
- Create a free account at https://data.marine.copernicus.eu/register
- Run the following command to set up your credentials:
  ```bash
  copernicusmarine login
  ```
- You only need to do this once; credentials are saved locally

### Manual Download
1. Visit [URL]
2. Download [specific file or dataset]
3. Place in `data/raw/`

### Automated Download
Run the download script:
```bash
python scripts/01_download_data.py
```

## Data Description

### Variables/Columns
Document the key variables/columns in your dataset:

| Column Name | Type | Description | Units |
|-------------|------|-------------|-------|
| var1        | float | Description | unit  |
| var2        | int   | Description | -     |

## Preprocessing Steps

Document any preprocessing applied to the raw data:
1. Step 1: [e.g., Remove missing values]
2. Step 2: [e.g., Normalize values]
3. Step 3: [e.g., Feature engineering]

## File Naming Conventions

- Raw data: `[dataset_name]_raw_[date].ext`
- Processed data: `[dataset_name]_processed_[date].ext`

## Notes

- Raw data should never be modified - keep it immutable
- All preprocessing should be documented and reproducible via scripts
- Large files (>100MB) are excluded from version control via .gitignore

## Citations

If you use this data in publications, please cite:
```
[Citation format]
```

## Data Privacy & Ethics

[Note any privacy considerations, ethical constraints, or data use agreements]
