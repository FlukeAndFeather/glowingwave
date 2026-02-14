# Glowingwave

A reproducible scientific data analysis project.

## Overview

This project performs data analysis involving data download, processing, and visualization. The structure is designed to facilitate reproducibility and clear organization.

## Project Structure

```
glowingwave/
├── README.md                    # This file
├── environment.yml              # Conda environment specification
├── .gitignore                   # Files to exclude from version control
├── config.yaml                  # Configuration parameters
├── data/                        # Data directory (not version controlled)
│   ├── raw/                     # Original, immutable data
│   ├── processed/               # Processed data ready for analysis
│   └── README.md                # Data documentation
├── notebooks/                   # Jupyter notebooks for exploration
│   ├── 01_explore_data.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_visualizations.ipynb
├── scripts/                     # Reproducible analysis scripts
│   ├── 01_download_data.py
│   ├── 02_preprocess.py
│   ├── 03_analyze.py
│   └── 04_generate_figures.py
├── src/                         # Reusable Python modules
│   ├── __init__.py
│   ├── data_utils.py
│   ├── plotting.py
│   └── analysis.py
├── figures/                     # Generated figures (not version controlled)
└── research_notes/              # Analysis documentation
    └── methods.md
```

## Setup

### 1. Create the conda environment

```bash
conda env create -f environment.yml
conda activate glowingwave
```

### 2. Download the data

Follow the instructions in `data/README.md` or run:

```bash
python scripts/01_download_data.py
```

## Usage

### Running the analysis pipeline

Execute the numbered scripts in order:

```bash
python scripts/01_download_data.py
python scripts/02_preprocess.py
python scripts/03_analyze.py
python scripts/04_generate_figures.py
```

### Exploratory analysis

For interactive exploration, use the Jupyter notebooks:

```bash
jupyter notebook
```

Then open the notebooks in the `notebooks/` directory.

## Configuration

Analysis parameters can be modified in `config.yaml`. This includes:
- Data source URLs
- File paths
- Analysis parameters
- Visualization settings

## Data

See `data/README.md` for information about:
- Data sources and citations
- Download instructions
- Data descriptions
- File formats

## Dependencies

All dependencies are specified in `environment.yml`. Key packages include:
- Python 3.x
- numpy, pandas, scipy
- matplotlib, seaborn
- jupyter
- pyyaml

## Author

[Your Name]

## Date

Created: 2026-02-13
