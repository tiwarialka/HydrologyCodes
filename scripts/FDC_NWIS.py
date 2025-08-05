import pandas as pd
import matplotlib.pyplot as plt
import hydrofunctions as hf
import numpy as np
import scipy.stats as sp
import scipy as sc    
data = hf.NWIS('04180000', 'dv', period='P10D')
data.get_data()
strflow=pd.DataFrame(data.df())
strflow.columns=('discharge','b')
strflow=strflow.drop(columns='b')
strflow.plot()
flow = strflow.sort_values('discharge',)
#strflow = np.sort(strflow)
ranks = sp.rankdata(flow, method='average')
ranks = ranks[::-1]
prob = [100*(ranks[i]/(len(flow)+1)) for i in range(len(flow)) ]
#flow['prob']=prob[:4]
plt.figure()
plt.scatter(prob,flow)
plt.plot(prob,flow)
plt.yscale('log')
plt.grid(which = 'both')
plt.xlabel('% of time that indicated discharge was exceeded or equaled')
plt.ylabel('discharge (cfs)')
plt.xticks(range(0,100,5))
plt.title('Flow duration curve')
