#
#% BFlow filter
#% Recursive digital filter techniques
#% references:
#% -J.G. Arnold and P.M Allen. Automated methods for estimating BFlow and groundwater recharge from streamflow records. Journal of the Americam Water Resources Association vol 35(2) (April 1999): 411-424
#% -J.G. Arnold, P.M. Allen, R. Muttiah, and G. Bernhardt Automated base flow separation and recession analysis techniques. Ground Water vol 33(6): 1010-1018.
#% Input variables
#% -strflow: continuous streamflow measurements at river guages or field flumes
#% Outpur variables:
#% -BFlow: BFlow/subsurface flow filted by three passes
#% Syntax
#function BFlow = BFlow(strflow)
import pandas as pd
import matplotlib.pyplot as plt
import hydrofunctions as hf
import numpy as np
def baseflow():
    data = hf.NWIS('01585200', 'dv', period='P30D')
    data.get_data()
    strflow=pd.DataFrame(data.df())
    strflow.columns=['discharge','b']
    strflow.plot()
    a = .925
    b = (1+a) / 2
    # strflow = evnt1a(:,5);
    DR = strflow
    BFlow = np.array(strflow)
    DR(1) = strflow(1) * .5
    BFlow(1,1) = strflow(1) - DR(1)
    BFlow(1,2) = BFlow(1,1)
    BFlow(1,3) = BFlow(1,1)
    # first pass (forward)
    for i = 2:len(strflow)
        DR(i) = a * DR(i-1) + b * (strflow(i) - strflow(i-1))
        if DR(i) < 0
            DR(i) = 0;
        end
        BFlow(i,1) = strflow(i) - DR(i);
        if BFlow(i,1) < 0
            BFlow(i,1) = 0;
        end
        if BFlow(i,1) > strflow(i)
            BFlow(i,1) = strflow(i);
        end
    end
    # second pass (backward)
    BFlow(end-1,2) = BFlow(end-1,1);
    for i = [len(strflow)-2:-1:1]
        DR(i) = a * DR(i+1) + b * (BFlow(i,1) - BFlow(i+1,1));
        if DR(i) < 0
            DR(i) = 0;
        end
        BFlow(i,2) = BFlow(i,1) - DR(i);
        if BFlow(i,2) < 0
            BFlow(i,2) = 0;
        end
        if BFlow(i,2) > BFlow(i,1)
            BFlow(i,2) = BFlow(i,1);
        end
    end
    # third pass (forward)
    BFlow(end-1,3) = BFlow(end-1,1);
    for i = 2:len(strflow)
        DR(i) = a * DR(i-1) + b * (BFlow(i,2)- BFlow(i-1,2));
        if DR(i) < 0
            DR(i) = 0;
        end
        BFlow(i,3) = BFlow(i,2) - DR(i);
        if BFlow(i,3) < 0
            BFlow(i,3) = 0;
        end
        if BFlow(i,3) > BFlow(i,2)
            BFlow(i,3) = BFlow(i,2);
        end
    end
    return;