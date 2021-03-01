#!/usr/bin/env python

"""
common.py: 
	The common.py file contains all the common methods which can me called from test case scripts
"""

__author__     = "Gurpreet Singh"
__date__       = "1st Mar 2021"
__version__    = "0.1"

import configparser as cp

def get_parameter_from_config(section, parameter):
    """Gets the parameter value from the specified section of the config file. It assumes the config file is in the 
    following path relative to the code file being executed:
        '../config/'

    Parameters
    ----------
    section : str, required
        The name of the section in the config file, where to read the parameter value from
    parameter: str, required
        The parameter name whose value is required  

    Returns
    -------
        The value of the parameter under the specified section in the config file. 
    """

    ## Read the parameter data from the config file
    config = cp.ConfigParser(allow_no_value = True)
    config.read(r'../config/api_testing.config')
    
    url = config.get(section, parameter)

    return url

