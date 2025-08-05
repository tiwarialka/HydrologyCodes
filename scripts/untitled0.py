from netCDF4 import Dataset

# load the observed timeseries
with Dataset('E:/Python_class/Data/Hydrology/catchment.obs.flow.nc', 'r', format='NETCDF4') as f:  # read the NetCDF file
    observed_flow = f.variables['flow'][:]  # this is the observed discharge timeseries
    observed_dt = f.variables['DateTime'][:]  # this is the timestamp series for the observed period

# load the observed timeseries
with Dataset('E:/Python_class/Data/Hydrology/catchment.sim.flow.nc', 'r', format='NETCDF4') as f:  # read the NetCDF file
    simulated_flow = f.variables['flow'][:]  # these are the simulated timeseries
    simulated_dt = f.variables['DateTime'][:]  # this is the timestamp series for the simulated period
import numpy as np

# check that the two timestamp arrays are identical (i.e. same periods)
if not np.array_equal(observed_dt, simulated_dt):
    raise Exception('The observed and simulated periods do not match.')
    
from hydroeval import *

# use the evaluator with the Kling-Gupta Efficiency (objective function 1)
my_kge = evaluator(kge, simulated_flow[0], observed_flow)

# use the evaluator with the Kling-Gupta Efficiency for inverted flow series (objective function 2)
my_kge_inv = evaluator(kge, simulated_flow[0], observed_flow, transform='inv')

# use the evaluator with the Root Mean Square Error (objective function 3)
my_rmse = evaluator(rmse, simulated_flow[0], observed_flow)