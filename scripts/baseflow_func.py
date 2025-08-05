#created as a practice for Python Class_ Spring 2019(SemII)
#Baseflow separation Method using 
#Arnold recursive didgital filter method (Single parameter=strflow and three pass filter)
#Eckhardt digital filter(two parameter= strflow, BFImax and single pass filter)
import numpy as np
#Recursive digital filter techniques
# -strflow: continuous streamflow measurements at river guages or field flumes
# Outpur variables:
# -BFlow: BFlow/subsurface flow filted by three passes
#Reference: -J.G. Arnold and P.M Allen. Automated methods for estimating BFlow and groundwater recharge from streamflow records. Journal of the Americam Water Resources Association vol 35(2) (April 1999): 411-424
#-J.G. Arnold, P.M. Allen, R. Muttiah, and G. Bernhardt Automated base flow separation and recession analysis techniques. Ground Water vol 33(6): 1010-1018.

def AR_baseflow(strflow):
    #intial conditions
    a = .925
    b = (1+a) / 2
    flow = np.array(strflow)
    DR = np.array(strflow)
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
    
    return(BFlow[:,2])

# Input variable-strflow: continuous streamflow measurements at river guages or field flumes and BFImax
# Outpur variables-BFlow: BFlow/subsurface flow filted by three passes
#Reference:Eckhardt, Klaus. "How to construct recursive digital filters for baseflow separation." Hydrological Processes: An International Journal 19, no. 2 (2005): 507-515.
def EK_baseflow(strflow):
    alpha=.98
    BFI = 0.8
    flow = np.array(strflow)
    BFlow = np.zeros([len(flow)])
    BFlow[0] = flow[0]
    for i in range(1,len(flow)):
    # algorithm
            BFlow[i] = ((1 - BFI) * alpha * BFlow[i-1] + (1 - alpha) * BFI * flow[i]) / (1 - alpha * BFI)
            if BFlow[i] > flow[i]:
                BFlow[i] = flow[i]

    return(BFlow)
