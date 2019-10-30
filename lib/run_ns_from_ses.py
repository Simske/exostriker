#!/usr/bin/env python
"""
@author: Trifon Trifonov
"""


import sys,  os
sys.path.insert(0, './lib')
sys.path.append('./lib/RV_mod/') #RV_mod directory must be in your path
import RV_mod as rv
import gls as gls
import numpy as np
import glob
import dill
import os
 
 
arguments = len(sys.argv) - 1

if arguments==3 and sys.argv[1] == '-ses' and os.path.exists(sys.argv[2]):
    try:
        file_pi = open(sys.argv[2], 'rb')
        fit_ses = dill.load(file_pi)
        file_pi.close()   
        fit = fit_ses 
 
    except (ImportError, KeyError, AttributeError) as e:
        print("%s cannot be recognaized"%sys.argv[2])
 
    target_name = sys.argv[3] 
 
    fit.live_points_fact = 100
    fit = rv.run_nestsamp(fit, threads=4, std_output=False, stop_crit = 0.01, Dynamic_nest = False, live_points = 400,fileoutput=False )
     
    file_ses = open(r"%s_out.ses"%target_name, 'wb')
    dill.dump(fit, file_ses)
    file_ses.close()    
    
    


     
