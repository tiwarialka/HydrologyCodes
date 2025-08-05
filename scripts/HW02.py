import matplotlib
import matplotlib.pyplot as plt
from climata.usgs import DailyValueIO
import pandas as pd
import numpy as np
import csv


plt.style.use('ggplot')
# %matplotlib inline
matplotlib.rcParams['figure.figsize'] = (14.0, 8.0)

# set parameters
nyears = 20
ndays = 365 * nyears
station_id = "03333700"
param_id = "00060"

datelist = pd.date_range(end=pd.datetime.today(), periods=ndays).tolist()
data = DailyValueIO(
    start_date=datelist[0],
    end_date=datelist[-1],
    station=station_id,
    parameter=param_id,
)

with open('W:\A4_Python\Homeworks\Data_03333700.csv', mode='ab') as csv_file:
        fieldnames1 = ['Date', 'Discharge']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames1)
        writer.writeheader()

# create lists of date-flow values for Kokomo Creek
for series in data:
    dates = [r[0] for r in series.data]
    flow = [r[1] for r in series.data]
    with open('W:\A4_Python\Homeworks\Data_03333700.csv', mode='ab') as csv_file:
        fieldnames1 = ['Date', 'Discharge']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames1)
        writer.writerow({'Date': str(dates[-1]), 'Discharge': flow[-1]})

