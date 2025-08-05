#
#% BFlow filter
#% Recursive digital filter techniques
#% references:
#% -J.G. Arnold and P.M Allen. Automated methods for estimating BFlow and groundwater recharge from streamflow records. Journal of the Americam Water Resources Association vol 35[2] [April 1999]: 411-424
#% -J.G. Arnold, P.M. Allen, R. Muttiah, and G. Bernhardt Automated base flow separation and recession analysis techniques. Ground Water vol 33[6]: 1010-1018.
#% Input variables
#% -strflow: continuous streamflow measurements at river guages or field flumes
#% Outpur variables:
#% -BFlow: BFlow/subsurface flow filted by three passes
#% Syntax
#function BFlow = BFlow[strflow]
import pandas as pd
#import matplotlib.pyplot as plt
import hydrofunctions as hf
import numpy as np
data = hf.NWIS('01585200', 'dv', period='P30D')
data.get_data()
strflow=pd.DataFrame(data.df())
strflow.columns=('discharge','b')
strflow.plot()
strflow=strflow.drop(columns='b')

a = .925
b = (1+a) / 2
# strflow = evnt1a[:,5];
flow = np.array(strflow['discharge'])
DR = np.array(strflow['discharge'])
BFlow = pd.DataFrame(np.zeros([len(DR),3]),index=strflow.index)
DR[0] = flow[0] * 0.5
BFlow.iat[0,0] = flow[0] - DR[0]
BFlow.iat[0,1] = BFlow.iat[0,0]
BFlow.iat[0,2] = BFlow.iat[0,0]
# first pass [forward]
for i in range(1,len(flow)):
    DR[i] = a * DR[i-1] + b * (flow[i] - flow[i-1])
    if (DR[i] < 0):
        DR[i] = 0
        
    BFlow.iat[i,0] = flow[i] - DR[i]
    if (BFlow.iat[i,0] < 0):
        BFlow.iat[i,0] = 0
        
    if (BFlow.iat[i,0] > flow[i]):
        BFlow.iat[i,0] = flow[i]

# second pass [backward]
BFlow.iat[len(flow)-1,1] = BFlow.iat[len(flow)-1,0]
for i in range(len(flow)-2,-1,-1):    
    DR[i] = a * DR[i+1] + b * (BFlow.iat[i,0] - BFlow.iat[i+1,0])
    if DR[i] < 0:
        DR[i] = 0
    BFlow.iat[i,1] = BFlow.iat[i,0] - DR[i]
    if BFlow.iat[i,1] < 0:
        BFlow.iat[i,1] = 0
    if BFlow.iat[i,1] > BFlow.iat[i,0]:
        BFlow.iat[i,1] = BFlow[i,0]

# third pass [forward]
BFlow.iat[len(flow)-1,2] = BFlow.iat[len(flow)-1,0]
for i in range(1,len(flow)):
    DR[i] = a * DR[i-1] + b * (BFlow.iat[i,1]- BFlow.iat[i-1,1])
    if DR[i] < 0:
        DR[i] = 0
    BFlow.iat[i,2] = BFlow.iat[i,1] - DR[i]
    if BFlow.iat[i,2] < 0:
        BFlow.iat[i,2] = 0
    if BFlow.iat[i,2] > BFlow.iat[i,1]:
        BFlow.iat[i,2] = BFlow.iat[i,1]

BFlow[2].plot()
strflow['BFlow']=BFlow[2]
strflow.plot()