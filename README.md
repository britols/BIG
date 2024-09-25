# BIG
A journey through large climate files

[Cookbooks] (https://cookbooks.projectpythia.org)

[Dask Arrays with Xarray](https://foundations.projectpythia.org/core/xarray/dask-arrays-xarray.html)

[Unidata Chunking Data: Why it Matters](https://www.unidata.ucar.edu/blogs/developer/entry/chunking_data_why_it_matters)

>With a conventional contiguous (index-order) storage layout, the time dimension varies most slowly, y varies faster, and x varies fastest. In this case, the spatial access is fast (0.013 sec) and the time series access is slow (180 sec, which is 14,000 times slower). If we instead want the time series to be quick, we can reorganize the data so x or y is the most slowly varying dimension and time varies fastest, resulting in fast time-series access (0.012 sec) and slow spatial access (200 sec, 17,000 times slower). In either case, the slow access is so slow that it makes the data essentially inaccessible for all practical purposes, e.g. in analysis or visualization.

[Handling very large files in Python](https://annefou.github.io/metos_python/07-LargeFiles/)

>When your netCDF file becomes large, it is unlikely you can fit the entire file into your laptop memory. You can slice your dataset and load it so it can fit into your laptop memory. You can slice netCDF variables using a syntax similar to numpy arrays:

>The elasped time spent to extract your slice strongly depends on how your data has been stored (how the dimensions are organized):



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

