# Work Journal

## 2026-02-13: Project Setup and California Current Mapping

### Summary

Established the complete project infrastructure for the Glowingwave oceanographic analysis project. Created a reproducible research structure following best practices: organized directory layout (data/, notebooks/, scripts/, src/, figures/), conda environment management with environment.yml, comprehensive documentation, and proper .gitignore for large data files.

Set up geospatial analysis capabilities by adding geopandas and cartopy to the environment. Successfully integrated Marine Regions Web Feature Service (WFS) to download the California Current Large Marine Ecosystem (LME #3) shapefile programmatically. This required troubleshooting direct download methods and implementing the proper WFS API calls with filtered queries.

Separated data acquisition from analysis by creating a dedicated download script (scripts/01_download_data.py) that handles WFS requests, while the Jupyter notebook (01_california_current_map.ipynb) focuses solely on visualization and analysis. The notebook creates a map of the California Current boundary with coastlines, borders, and gridlines using cartopy projections.

Configured GitHub Pages deployment using the /docs folder. Created an automated HTML generation script (scripts/generate_html.py) that converts Jupyter notebooks to HTML for web viewing. Built a clean index page for easy navigation.

Repository pushed to https://github.com/FlukeAndFeather/glowingwave.git with three commits capturing the progression from initial setup through the complete California Current mapping workflow.

### Next Session Goals

Download and process surface chlorophyll concentration data for the California Current region (early June 2025). Evaluate two primary data sources: NOAA CoastWatch ERDDAP (simpler API, no authentication) versus Copernicus Marine Service (CMEMS, requires account but potentially better coverage). Test both services to determine which provides better data quality and easier integration. Once downloaded, overlay chlorophyll data on the California Current boundary map.

## 2026-02-14: Copernicus Biogeochemical Data and Animated Profiles

### Summary

Added copernicusmarine package to environment and created download function for Copernicus Marine Service biogeochemical data. Downloaded 20 years (2005-2024) of daily zooplankton carbon and net primary production data for California Current region (2.4 GB). Created biogeochemical map notebook with dual x-axis latitudinal profiles showing mean values across longitude. Generated animated GIF (29 MB, ~1,044 frames) displaying temporal evolution of latitudinal profiles over the 20-year period. Embedded animation in notebook and deployed to GitHub Pages. Merged chla branch into main.

### Next Session Goals

Model the seasonal progression of the latitudinal peak in zooplankton carbon and net primary production. Analyze how peak location varies throughout the year and identify patterns across the 20-year time series.
