from netCDF4 import Dataset
import csv
import xarray as xr
from datetime import datetime as dt

def read_in_gdal(file_in):
    xrds = xr.open_dataset(file_in)
    return xrds

def read_in_metadata(file_in):
    rows = []; keys = []; values = []

    with open(file_in,'r') as metadata:
        csvreader = csv.reader(metadata) 
        for row in csvreader:
            rows.append(row)

    #Rows ignoring the header
    for row in rows[1:]:
        keys.append(row[0])
        values.append(row[1])

    metadata_dict = dict(zip(keys, values))
    return metadata_dict

def add_metadata_to_array(xrds, metadata_dict):
    xrds.attrs = metadata_dict

    dtnow = dt.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    xrds.attrs['date_created'] = dtnow
    xrds.attrs['history'] = f'File created at {dtnow} using xarray in Python'
    xrds.attrs['Conventions'] ='ACDD-1.3, CF-1.11'

    # Adding missing variable attributes
    xrds.variables['Band1'].attrs['units']='meter'
    xrds.variables['Band1'].attrs['positive']='up'
    xrds.variables['Band1'].attrs['standard_name']='height'
    xrds.variables['Band1'].attrs['coverage_content_type']='image'
    xrds.variables['lat'].attrs['coverage_content_type']='coordinate'
    xrds.variables['lon'].attrs['coverage_content_type']='coordinate'
    
    return xrds
