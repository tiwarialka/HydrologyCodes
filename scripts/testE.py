import pandas as pd
import hydrofunctions as hf
import numpy as np
def EK_baseflow():
    data = hf.NWIS('04180000', 'dv', period='P365D')
    data.get_data()
    strflow=pd.DataFrame(data.df())
    strflow.columns=('discharge','b')
    #strflow.plot()
    strflow=strflow.drop(columns='b')
#initial conditions
    alpha=.98
    BFI = 0.8
    flow = np.array(strflow['discharge'])
    BFlow = np.zeros([len(flow)])
    BFlow[0] = flow[0]
    for i in range(1,len(flow)):
    # algorithm
            BFlow[i] = ((1 - BFI) * alpha * BFlow[i-1] + (1 - alpha) * BFI * flow[i]) / (1 - alpha * BFI)
            if BFlow[i] > flow[i]:
                BFlow[i] = flow[i]
            strflow['BFlow']=BFlow
            strflow.plot()
            