''' Python script for converting gdal output to CF-compliant netCDF format
The script reads in the gdal output and metadata fields from separate files
Script requires the following input files: gdal -file and metadata fields -file

Author: imatero (ilkka.matero@sios-svalbard.org)
Date: 27.5.2024
'''

import xarray as xr
from lib import data_input_output_functions as io

def main(gdal_fp, metadata_fp, output_fp):
    gdal_in = io.read_in_gdal(gdal_fp)
    
    # Read in metadata
    metadata_dict = io.read_in_metadata(metadata_fp)
    
    # Write metadata to the file
    data_xarray = io.add_metadata_to_array(gdal_in, metadata_dict)
    
    # Write netCDF file
    data_xarray.to_netcdf(output_fp,'w',format='netCDF4')
    
if __name__ == "__main__":
    # Specify paths to the input and output files:
    gdal_fp = 'data/<input_filepath.nc>'
    metadata_fp = 'data/<metadata_filepath.csv>'
    output_fp = 'output/<output_filepath>.nc'
    
    main(gdal_fp, metadata_fp, output_fp)