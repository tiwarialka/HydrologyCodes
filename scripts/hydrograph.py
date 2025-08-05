# To import pyplot library.
# pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation.
import matplotlib.pyplot as plt

# To import pandas library.
# pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd

# Utilising pandas library, csv file is read from the storage
data=pd.read_csv('C:/Users/devlab/Desktop/Python_class/Data01/NCFRHW01.csv',usecols=['DateTime','Discharge, cfs'])

# Converts DateTime String to Date
timestamp=pd.to_datetime(data.DateTime)

# To plot Histogram for Streamflow Data
plt.hist(data.Discharge,bins=35)
plt.xlabel("Streamflow (cfs)")
plt.ylabel("Frequency")
plt.title("Histogram for Streamflow Data \n (USGS 02108000 NORTHEAST CAPE FEAR RIVER NEAR CHINQUAPIN, NC)  \n Period: 2018-09-01 to 2018-09-2")
plt.show()

# To plot Hydrograph for Streamflow Data
plt.plot(timestamp,data.Discharge)
plt.xlabel("Time (days)")
plt.ylabel("Streamflow (cfs)")
plt.title("Discharge Hydrograph \n (USGS 02108000 NORTHEAST CAPE FEAR RIVER NEAR CHINQUAPIN, NC)  \n Period: 2018-09-01 to 2018-09-02")
plt.show()

import matplotlib.pyplot as plt
#a=np.random.random(100)
#b=np.random.random(100)
#plt.scatter(a,b)
#plt.show()
import pandas as pd
data = pd.read_csv(r'C:\Users\devlab\Desktop\Python_class\Class01\wabash.csv',usecols=['datetime','discharge','stage'])
timestamp =pd.to_datetime(data.datetime)
plt.plot(timestamp,data.discharge)
plt.xlabel("Time(days)")
plt.ylabel("Discharge(cfs)")
plt.title("Discharge Hydrograph for Wabash")
plt.show()