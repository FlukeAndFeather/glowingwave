# Data Documentation

This directory contains all data used in the Glowingwave analysis project.

## Directory Structure

- `raw/` - Original, immutable data files as downloaded from source
- `processed/` - Cleaned and processed data ready for analysis

## Data Sources

### Dataset Name
- **Source**: [Provide URL, DOI, or citation]
- **Download Date**: [YYYY-MM-DD]
- **Description**: [Brief description of what this dataset contains]
- **Format**: [CSV, JSON, HDF5, etc.]
- **Size**: [Approximate file size]
- **License**: [Data license if applicable]

## Download Instructions

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
