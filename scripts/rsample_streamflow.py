#-------------------------------------------------------------------------------
# Name:        resample_streamflow.py
# Purpose:     compute various statistic of the downloaded daily and instantaneous streamflow data from USGS
# Author:      Alka Tiwari
# Created:     22/01/2019
#-------------------------------------------------------------------------------
import hydrofunctions as hf
import pandas as pd
import matplotlib.pyplot as plt
strflow = hf.NWIS('02108000', 'dv', '2009-01-01','2019-01-01')
strflow.get_data()
data10y=pd.DataFrame(strflow.df())
data10y.columns=['discharge','b']
data10y.plot()

# computing and plotting annual average value of streamglow over 10 years.

annual_avg=data10y.resample('Y').mean()
annual_avg.columns=['mean']
annual_avg.plot()

# computing annual minimum value of streamglow over 10 years.

annual_min=data10y.resample('Y').min()
annual_min.columns=['min', 'x ']

# computing monthly mean and minimum value of streamglow over 10 years.

monthly=data10y.resample('M').mean()
monthly.columns=['mean']
monthly['min']=data10y['discharge'].resample('M').min()

# plotting monthly mean and monthly minimum values of streamflow over 10 years

test=monthly.plot()
test.set(xlabel="Time", ylabel="Stream FLow (cfs)")
# save it at speciifed location
#plt.savefig('E:\\Python_class\\Data\\Hydrology\\test.pdf')

# plotting 10 year od daily streamflow and annual average and minimum values.

plt.figure()
plt.plot(data10y.index, data10y['discharge'])
plt.plot(annual_avg.index, annual_avg['mean'],annual_avg.index, annual_min['min'])

# getting instantaneous values and plotting the hydrograph

instant = hf.NWIS('02108000', 'iv', '2018-08-01','2018-12-01')
instant.get_data()
data_inst=pd.DataFrame(instant.df())
data_inst.columns=['instantaneous','b']
data_inst.plot()
