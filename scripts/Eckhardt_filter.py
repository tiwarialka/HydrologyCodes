# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:20:21 2019

@author: Admin
"""
#' Baseflow Separation by use of an Eckhardt Filter
#'
#' Extract baseflow from a daily streamflow record using the method described by
#'Eckhardt (2005).
#'
#' @param date vector of dates corresponding to each \code{discharge}, should be of class "Date."
#' Missing values are not permitted.
#' @param discharge the daily streamflow to be separated missing values are not permitted
#'within the time specified by \code{Start} and \code{end}.
#' @param BFImax maximum BFI to use in the filtering.
#' @param alpha filter parameter.
#' @param STAID the station identifier for the data.
#' @references Eckhardt, K., 2005, How to construct recursive digital filters for
#'  baseflow separation: Hydrological Processes, v. 19, no. 2, p. 507–515.
#'
#' @return an object of class "baseflow" and inherits class "data.frame" of the selected data,
#'a data frame of the baseflow information, and other information about the analysis.
#'
#' @keywords baseflow
#' @examples
#'
#'\dontrun{
#'}
#'@export 
# https://rdrr.io/github/smwesten-usgs/recharge/src/R/Eckhardt_digital_filter.R

def Eckhardt(self, alpha=.98, BFI=.80, re=1):
        """
        Recursive digital filter for baseflow separation. Based on Eckhardt, 2004.\n
        series : array of discharge measurements\n
        alpha : filter parameter\n
        BFI : BFI_max (maximum baseflow index)\n
        re : number of times to run filter
        """
        print('round ' + str(re))
        print(self.bflow[:5])
        # first looks to see if there has alread been a run
        if len(self.bflow) > 0:
            Q = np.array(self.bflow)
        else:
            Q = np.array(self.Q)
        f = np.zeros(len(Q))
        f[0] = Q[0]
        for t in np.arange(1,len(Q)):
            # algorithm
            f[t] = ((1 - BFI) * alpha * f[t-1] + (1 - alpha) * BFI * Q[t]) / (1 - alpha * BFI)
            if f[t] > Q[t]:
                f[t] = Q[t]
        # adds the baseflow to self variables so it can be called recursively
        self.bflow = f
        print(max(self.bflow))
        # calls method again if multiple passes are specified
        if re > 1:
            self.Eckhardt(alpha=alpha, BFI=BFI, re=re-1)

        return self.bflow