# Dronedata_to_CF_NetCDF
Short python code for converting gdal output to CF-compliant netCDF format

The intended use of this code is for converting files that are already in netcdf format to CF-compliant NetCDF -files by adding the required and recommended metadata elements to the output file.
For installing and using Geospatial Data Abstraction Library (GDAL) for converting GeoTIFF to NetCDF, please refer to https://nsidc.org/data/user-resources/help-center/how-do-i-convert-geotiff-netcdf-file

Required packages: 
  - xarray
  - netCDF4
  - csv
  - datetime
