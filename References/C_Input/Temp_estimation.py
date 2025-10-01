import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs

url = "https://www.ncei.noaa.gov/thredds/dodsC/noaa-global-temp-v6/NOAAGlobalTemp_v6.0.0_gridded_s185001_e202507_c20250806T150124.nc"

xrds = xr.open_dataset(url)

desired_date = '2025-08-01'
data_for_desired_date = xrds.sel(time = desired_date, method = 'nearest')

print(data_for_desired_date)

