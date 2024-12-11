''' Python script for converting gdal output to CF-compliant netCDF format
The script reads in the gdal output and metadata fields from separate files
Script requires the following input files: gdal -file and metadata fields -file

Authors: imatero (ilkka.matero@sios-svalbard.org) and rhann (richard.hann@ntnu.no)
Date: 7.12.2024
'''

import xarray as xr
from lib import data_input_output_functions as io

def main(tif_fp, gdal_fp, metadata_fp, output_fp):

    # Ask user if they want to skip the GDAL transformation step
    skip_gdal = input("Do you want to skip the GDAL transformation step? (yes/no): ").strip().lower()

    if skip_gdal not in ['yes', 'y']:
        # Translate TIF into NetCDF
        print('Translate TIF into NetCDF. This can take a while.')
        subprocess.run(['gdal_translate', '-of', 'NetCDF', tif_fp, gdal_fp], check=True)
        print('Done translating TIF into NetCDF')    
    else:
        print('Skipping GDAL transformation step.')
        
    # Read in NetCDF files
    gdal_in = io.read_in_gdal(gdal_fp)
    
    # Read in metadata
    metadata_dict = io.read_in_metadata(metadata_fp)
    
    # Write metadata to the file
    data_xarray = io.add_metadata_to_array(gdal_in, metadata_dict)
    
    # Write netCDF file
    data_xarray.to_netcdf(output_fp,'w',format='netCDF4')
    print('Done writing netCDF file') 
    
if __name__ == "__main__":
    # Specify paths to the input and output files:
    tif_fp = 'data/example_DEM.tif'    # Input .tif raw file
    gdal_fp = 'data/example_DEM.nc>' # Output .nc NetCDF file
    metadata_fp = 'data/example_csv_file.csv' # Input .csv file with metadata
    output_fp = 'output/example_output_with_metadata.nc' # Output .nc NetCDF file
    
    main(gdal_fp, metadata_fp, output_fp)
