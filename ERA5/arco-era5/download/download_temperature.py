#C:\Users\ls2236\AppData\Local\anaconda3\envs\arco\python.exe C:\Users\ls2236\Projects\BIG\ERA5\arco-era5\download\download_temperature.py


import xarray as xr
import dask
import gc
from distributed import Client,LocalCluster



def roll_longitude(ds):
    return ds.assign_coords(longitude=(((ds.longitude + 180) % 360) - 180)).sortby('longitude')

def load_cloud_data():
        
        data_in_cloud = xr.open_zarr(
            'gs://gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3',
            chunks = {"time": 48},
            storage_options=dict(token='anon')
        )

        return(data_in_cloud)

def download_year(year,data_in_cloud):

    try:

        print(f"Processing year: {year}")

        date_i = f'{year}-01-01'
        date_f = f'{year}-01-05'
        latN = 90
        latS = 20
        lonW = -150
        lonE = -40
        Var = '2m_temperature'

        data = data_in_cloud.sel(time=slice(date_i,date_f))
        data = roll_longitude(data)
        data = data.sel(latitude = slice(latN,latS),longitude=slice(lonW,lonE))

        data = data[Var]
        data = data.persist()
        
        #grouped_data = data.groupby("time.dayofyear")
        grouped_data = data.resample(time="D")
        daily_t2_max = grouped_data.max()
        daily_t2_min = grouped_data.min()
        output_data = xr.Dataset({
             'daily_t2_max': daily_t2_max,
             'daily_t2_min': daily_t2_min
        })

        file_name = r"C:\Users\ls2236\Projects\BIG\ERA5\arco-era5\data\{}_{}.nc".format(Var,year)
        print(file_name)
        output_data.to_netcdf(file_name,mode='w')

    except Exception as e:
            print(f"Error processing year {year}: {e}")
            return
    
    finally:
         del data, grouped_data, daily_t2_max, daily_t2_min, output_data
         gc.collect()
         

if __name__ == "__main__":

    cluster = LocalCluster()         
    client = cluster.get_client()
    print(cluster.get_client)

    data_in_cloud = load_cloud_data()

    try:
        years = ['2019','2020']

        for year in years:
            download_year(year,data_in_cloud)

    finally:
        client.close()