# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:17:43 2019

@author: Admin
"""

import pandas as pd
from hydroeval import *
import numpy as np
from netCDF4 import Dataset

# load the observed timeseries
with Dataset('E:/Python_class/Data/Hydrology/catchment.obs.flow.nc', 'r', format='NETCDF4') as f:  # read the NetCDF file
    observed_flow = f.variables['flow'][:]  # this is the observed discharge timeseries
    observed_dt = f.variables['DateTime'][:]  # this is the timestamp series for the observed period

# load the observed timeseries
with Dataset('E:/Python_class/Data/Hydrology/catchment.sim.flow.nc', 'r', format='NETCDF4') as f:  # read the NetCDF file
    simulated_flow = f.variables['flow'][:]  # these are the simulated timeseries
    simulated_dt = f.variables['DateTime'][:]  # this is the timestamp series for the simulated period
#data = pd.read_csv('E:/Python_class/Data/Hydrology/discharge.csv')
#data = data.set_index('date') #to create date as index
##Hydroeval does not work with dataframe only with numpy so I had to do this transformation
s = np.array(data['simulated']) 
o = np.array(data['observed'])
if not np.array_equal(observed_dt, simulated_dt):
    raise Exception('The observed and simulated periods do not match.')
from hydroeval import *

# use the evaluator with the Kling-Gupta Efficiency (objective function 1)
my_kge = evaluator(kge, simulated_flow, observed_flow)

# use the evaluator with the Kling-Gupta Efficiency for inverted flow series (objective function 2)
my_kge_inv = evaluator(kge, simulated_flow, observed_flow, transform='inv')

# use the evaluator with the Root Mean Square Error (objective function 3)
my_rmse = evaluator(rmse, simulated_flow, observed_flow)
my_rmse = evaluator(rmse, s, o)
my_kge = evaluator(kge, s, o)
my_kge_inv = evaluator(kge, s, o, transform='inv')
my_kgeprime = evaluator(kgeprime, s, o)
my_nse = evaluator(nse, s, o)
my_mare = evaluator(mare, s, o)
my_pbias = evaluator(pbias, s, o)
my_nse_c2m = evaluator(nse_c2m, s, o)
my_kge_c2m = evaluator(kge_c2m, s, o)
my_kgeprime_c2m = evaluator(kgeprime_c2m, s, o)
