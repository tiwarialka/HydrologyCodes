import baseflow_func
import pandas as pd
import matplotlib.pyplot as plt
import hydrofunctions as hf
#download data using hydrofunction from USGS NWIS
data = hf.NWIS('04180000', 'dv', period='P365D')
data.get_data()
#storing the downloaded value in strflow dataframe
strflow=pd.DataFrame(data.df())
strflow.columns=('discharge','b') #naming the column
#strflow.plot()
strflow=strflow.drop(columns='b') #drop unnecessary column
# calling the function and storing the value in a column of the dataframe
strflow['AR_baseflow'] = baseflow_func.AR_baseflow(strflow['discharge'])
strflow['EK_baseflow'] = baseflow_func.EK_baseflow(strflow['discharge'])
strflow.plot() # plotting all the values in one plot

