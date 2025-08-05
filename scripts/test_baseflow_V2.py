#
#BFlow filter
#Recursive digital filter techniques
# -strflow: continuous streamflow measurements at river guages or field flumes
# Outpur variables:
# -BFlow: BFlow/subsurface flow filted by three passes
import pandas as pd
#import matplotlib.pyplot as plt
import hydrofunctions as hf
import numpy as np
def baseflow():
    data = hf.NWIS('04180000', 'dv', period='P365D')
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
    BFlow = np.zeros([len(DR),3])
    DR[0] = flow[0] * 0.5
    BFlow[0,0] = flow[0] - DR[0]
    BFlow[0,1] = BFlow[0,0]
    BFlow[0,2] = BFlow[0,0]
    # first pass [forward]
    for i in range(1,len(flow)):
        DR[i] = a * DR[i-1] + b * (flow[i] - flow[i-1])
        if (DR[i] < 0):
            DR[i] = 0
            
        BFlow[i,0] = flow[i] - DR[i]
        if (BFlow[i,0] < 0):
            BFlow[i,0] = 0
            
        if (BFlow[i,0] > flow[i]):
            BFlow[i,0] = flow[i]
    
    # second pass [backward]
    BFlow[len(flow)-1,1] = BFlow[len(flow)-1,0]
    for i in range(len(flow)-2,-1,-1):    
        DR[i] = a * DR[i+1] + b * (BFlow[i,0] - BFlow[i+1,0])
        if DR[i] < 0:
            DR[i] = 0
        BFlow[i,1] = BFlow[i,0] - DR[i]
        if BFlow[i,1] < 0:
            BFlow[i,1] = 0
        if BFlow[i,1] > BFlow[i,0]:
            BFlow[i,1] = BFlow[i,0]
    
    # third pass [forward]
    BFlow[len(flow)-1,2] = BFlow[len(flow)-1,0]
    for i in range(1,len(flow)):
        DR[i] = a * DR[i-1] + b * (BFlow[i,1]- BFlow[i-1,1])
        if DR[i] < 0:
            DR[i] = 0
        BFlow[i,2] = BFlow[i,1] - DR[i]
        if BFlow[i,2] < 0:
            BFlow[i,2] = 0
        if BFlow[i,2] > BFlow[i,1]:
            BFlow[i,2] = BFlow[i,1]
    
    strflow['BFlow']=BFlow[:,2]
    #strflow['DR']=DR
    strflow.plot()
    return(BFlow)
    #plt.savefig('E:\\Python_class\\Data\\Hydrology\\test_baseflow.pdf')
    #strflow['DR'].plot()
    #strflow['BFlow'].plot()
bf = baseflow()