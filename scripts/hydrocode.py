----------------------------------------------------------------------------
# Name:        hydrocode.py
# Purpose:     download streamflow data from USGS and plot hydrograph
# Author:      Alka Tiwari
# Created:     22/01/2019
#-------------------------------------------------------------------------------
import hydrofunctions as hf
%matplotlib inline 
# any of the following format can be used to download dail value "dv" of the streamflow
#strflow = hf.NWIS('02108000','dv',period='P365D')
strflow = hf.NWIS('02108000', 'dv', '2018-01-01','2019-01-01')
strflow.get_data()
strflow.df().head()
strflow.df().plot()
plt.xlabel("Time")
plt.ylabel("Discharge(cfs)")
plt.title("Discharge Hydrograph for NCFR NEAR CHINQUAPIN, NC")