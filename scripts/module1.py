#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tiwari13
#
# Created:     14/02/2019
# Copyright:   (c) tiwari13 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

#!{sys.executable} -m pip install hydrofunctions

import hydrofunctions as hf

#%matplotlib inline

herring2 = hf.NWIS('03335500', 'iv', start_date='2010-10-01',end_date='2018-09-30')

herring2.get_data()

herring2.df().plot()

Timeseries = herring2.df()

Timeseries.columns=["discharge","flag"]

Timeseries.head()

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import os

Timeseries.to_csv("Timeseries.csv",sep = ',')

Daily = Timeseries.resample('D').max()

Daily.head()

Year = Daily.resample('Y').max()

Year.head()

Year = Daily.resample('365D').max()

Year.head()

plt.savefig('test.png', bbox_inches='tight')

Year["year"]=Year.index.year

fig, ax = plt.subplots(figsize = (11,8))

ax.scatter(x=Year.index,

y=Year['discharge'],

color = 'purple')