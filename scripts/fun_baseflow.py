import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sp
#def fdc_simple(df, site, begyear=1900, endyear=2015, normalizer=1):
    '''
    Generate flow duration curve for hydrologic time series data
    PARAMETERS:
        df = pandas dataframe of interest; must have a date or date-time as the index
        site = pandas column containing discharge data; must be within df
        begyear = beginning year of analysis; defaults to 1900
        endyear = end year of analysis; defaults to 2015
        normalizer = value to use to normalize discharge; defaults to 1 (no normalization)
    
    RETURNS:
        matplotlib plot displaying the flow duration curve of the data
        
    REQUIRES:
        numpy as np
        pandas as pd
        matplotlib.pyplot as plt
        scipy.stats as sp
    '''
    # limit dataframe to only the site
    #df = df[[site]]
#    site = sites[28]
#    df = USGS_Site_Data[[site]]
#    begyear = 1900
#    endyear = 2015
#    data = df[(df.index.to_datetime() > pd.datetime(begyear,1,1))&(df.index.to_datetime() < pd.datetime(endyear,1,1))]
    data = data.dropna()
    data = hf.NWIS('01585200', 'dv', period='P30D')
    # filter dataframe to only include dates of interest
    data = df[(df.index.to_datetime() > pd.datetime(begyear,1,1))&(df.index.to_datetime() < pd.datetime(endyear,1,1))]

    # remove na values from dataframe
    data = data.dropna()

    # take average of each day of year (from 1 to 366) over the selected period of record
    data['doy']=data.index.dayofyear
    dailyavg = data[site].groupby(data['doy']).mean()
        
    data = np.sort(dailyavg)

    ## uncomment the following to use normalized discharge instead of discharge
    #mean = np.mean(data)
    #std = np.std(data)
    #data = [(data[i]-np.mean(data))/np.std(data) for i in range(len(data))]
    data = [(data[i])/normalizer for i in range(len(data))]
    
    # ranks data from smallest to largest
    ranks = sp.rankdata(data, method='average')

    # reverses rank order
    ranks = ranks[::-1]
    
    # calculate probability of each rank
    prob = [(ranks[i]/(len(data)+1)) for i in range(len(data)) ]
    
    # plot data via matplotlib
    plt.plot(prob,data,label=site+' '+str(begyear)+'-'+str(endyear))