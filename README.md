# BIG
A journey through large climate files


##### [ARCO ERA5](https://github.com/google-research/arco-era5)

ar - An ML-ready, unified (surface & atmospheric) version of the data in Zarr. (Analysis Ready)
co - A port of gaussian-gridded ERA5 data to Zarr. (Cloud Optimized)
raw - All raw grib & NetCDF data.


[Cookbooks](https://cookbooks.projectpythia.org)

**XARRAY**

[Xarray Tutorial](https://tutorial.xarray.dev/intro.html)

**DASK**

[Dask Resources](https://scrapbox.io/pycoaj/dask)

[grid metrics (vorticity, divergent, etc)](https://xgcm.readthedocs.io/en/latest/grid_metrics.html)

[Parallelizing Xarray with Dask](https://github.com/ProjectPythia/dask-cookbook/blob/main/notebooks/03-dask-xarray.ipynb)

[Notebook w/ some dask info](https://github.com/ProjectPythia/ERA5_interactive-cookbook/blob/main/notebooks/06_era5_anomaly.ipynb)

[Using dask with ECMWF API](https://github.com/rsignell-usgs/pangeo_showcase_20221012/blob/main/00_era5_test_api.ipynb)

[Dask Arrays with Xarray](https://foundations.projectpythia.org/core/xarray/dask-arrays-xarray.html)

[Unidata Chunking Data: Why it Matters](https://www.unidata.ucar.edu/blogs/developer/entry/chunking_data_why_it_matters)

>With a conventional contiguous (index-order) storage layout, the time dimension varies most slowly, y varies faster, and x varies fastest. In this case, the spatial access is fast (0.013 sec) and the time series access is slow (180 sec, which is 14,000 times slower). If we instead want the time series to be quick, we can reorganize the data so x or y is the most slowly varying dimension and time varies fastest, resulting in fast time-series access (0.012 sec) and slow spatial access (200 sec, 17,000 times slower). In either case, the slow access is so slow that it makes the data essentially inaccessible for all practical purposes, e.g. in analysis or visualization.

[Handling very large files in Python](https://annefou.github.io/metos_python/07-LargeFiles/)

>When your netCDF file becomes large, it is unlikely you can fit the entire file into your laptop memory. You can slice your dataset and load it so it can fit into your laptop memory. You can slice netCDF variables using a syntax similar to numpy arrays:

>The elasped time spent to extract your slice strongly depends on how your data has been stored (how the dimensions are organized):

Intel(R) Xeon(R) w5-3425   3.19 GHz
12 cores
64 GB RAM

**Climatology**

[Calculating Climatologies and Anomalies with Xarray and Dask:](https://nbviewer.org/gist/rabernat/30e7b747f0e3583b5b776e4093266114)


[Optimizing climatology calculation with Xarray and Dask](https://discourse.pangeo.io/t/optimizing-climatology-calculation-with-xarray-and-dask/2453)


[Strategies for climatology calculations](https://flox.readthedocs.io/en/latest/user-stories.html)

[Best practices to go from 1000s of netcdf files to analyses on a HPC cluster?](https://discourse.pangeo.io/t/best-practices-to-go-from-1000s-of-netcdf-files-to-analyses-on-a-hpc-cluster/588/39)


[Global Mean Surface Temperature](https://gallery.pangeo.io/repos/pangeo-gallery/cmip6/global_mean_surface_temp.html)

**Analysis ready kerchunk**

[pywren.io](http://pywren.io)

[Kerchunk Tutorial 2022-04-25](https://github.com/lsterzinger/2022-esip-kerchunk-tutorial/blob/main/01-Create_References.ipynb)

[Using AWS Lambda and PyWren for Landsat 8 Time Series](https://github.com/aws-samples/pywren-workshops/blob/master/Lab-4-Landsat-NDVI/Landsat_NDVI_Timeseries.ipynb)

[Accessing NetCDF and GRIB file collections as cloud-native virtual datasets using Kerchunk](https://medium.com/pangeo/accessing-netcdf-and-grib-file-collections-as-cloud-native-virtual-datasets-using-kerchunk-625a2d0a9191)

[Cloud-Performant NetCDF4/HDF5 with Zarr, Fsspec, and Intake](https://medium.com/pangeo/cloud-performant-netcdf4-hdf5-with-zarr-fsspec-and-intake-3d3a3e7cb935)

**Julia**

[julia: What would be the best approach to handle large NetCDF sets?](https://discourse.julialang.org/t/what-would-be-the-best-approach-to-handle-large-netcdf-sets/102091/11)

[Extracting data from netcdf stacked file](https://discourse.julialang.org/t/extracting-data-from-netcdf-stacked-file/90927)

[NCDatasets.jl](https://github.com/Alexander-Barth/NCDatasets.jl)

[YAXArrays.jl](https://github.com/JuliaDataCubes/YAXArrays.jl)

[Rasters.jl](https://rafaqz.github.io/Rasters.jl/stable/)

[ClimateTools.jl Importing a NetCDF dataset](https://juliaclimate.github.io/ClimateTools.jl/stable/datasets/#Manipulations-1)

[ClimateUtilities.jl reading NC](https://github.com/CliMA/ClimaUtilities.jl/blob/main/docs/src/filereaders.md)

[JuliaClimate Nootebooks](https://juliaclimate.github.io/Notebooks/#climate-models)

[ShallowWater.jl](https://docs.juliahub.com/General/ShallowWaters/stable/)


**Python:**

[XARRAY Advanced Indexing](https://stackoverflow.com/questions/69330668/efficient-way-to-extract-data-from-netcdf-files)

[More Advanced Indexing](https://docs.xarray.dev/en/stable/user-guide/indexing.html#more-advanced-indexing)

[Python Training from Unidata](https://github.com/Unidata/python-training/tree/master)

[Python Gallery from Unidata](https://unidata.github.io/python-training/gallery/gallery-home/)

[Metpy getting started](https://unidata.github.io/MetPy/latest/userguide/startingguide.html)

[Metpy easy plots](https://unidata.github.io/MetPy/latest/tutorials/declarative_tutorial.html#sphx-glr-tutorials-declarative-tutorial-py)

[Earthkit - ECMWF Python library](https://github.com/ecmwf/earthkit)

[Parallelizing Xarray with Dask from NCAR](https://ncar.github.io/dask-tutorial/notebooks/03-dask-xarray.html)

[Speeding up reading of very large netcdf file in python](https://stackoverflow.com/questions/35422862/speeding-up-reading-of-very-large-netcdf-file-in-python)

>I highly recommend that you take a look at the xarray and dask projects. Using these powerful tools will allow you to easily split up the computation in chunks. This brings up two advantages: you can compute on data which does not fit in memory, and you can use all of the cores in your machine for better performance. You can optimize the performance by appropriately choosing the chunk size (see documentation).

[How to select an inter-year period with xarray?](https://stackoverflow.com/questions/52533630/how-to-select-an-inter-year-period-with-xarray/52572399#52572399)

[xarray - select the data at specific x AND y coordinates](https://stackoverflow.com/questions/72179103/xarray-select-the-data-at-specific-x-and-y-coordinates/72179547#72179547)

[Subtract two xarrays while keeping all dimensions](https://stackoverflow.com/questions/69866469/subtract-two-xarrays-while-keeping-all-dimensions/69867005#69867005)

[Resample xarray object to lower resolution spatially](https://stackoverflow.com/questions/53886153/resample-xarray-object-to-lower-resolution-spatially/53952389#53952389)

[Python: How to write large netcdf with xarray](https://stackoverflow.com/questions/69810367/python-how-to-write-large-netcdf-with-xarray)


**Visualization**

https://projectpythia.org/advanced-viz-cookbook/notebooks/1-comparison.html