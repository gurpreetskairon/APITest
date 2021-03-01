#!/usr/bin/env python

"""
testcases.py: 
	The testcases.py file contains an acceptance test case, which tests 3 conditions in the json reponse
    from a restful API call.

    The code uses the unittest library for runnnig the test cases. To make it configurable, the code 
    reads the API url from a config file placed in the config directory under the project directory. 
"""

__author__     = "Gurpreet Singh"
__date__       = "1st Mar 2021"
__version__    = "0.1"


import unittest
import requests
from common import *

class TestRESTAPI(unittest.TestCase):

    def test_acceptance(self):
        ## The test case acceptance criteria to test the REST API.
        # Makes a http request and parses the json reponse for the parameters and their values
        # which satisfy the acceptance criteria.    

        response = requests.get(get_parameter_from_config("test_acceptance", "url"))

        # check if the http response status is in between status code 200 and 299. This implies the request was ok  
        self.assertTrue(response.status_code >= 200 and response.status_code < 300)
        json_response = response.json()

        # check if there is a Name key and verify its value 
        self.assertEqual(json_response['Name'], "Carbon credits")

        # check if there is a CanRelist key and verify its value
        self.assertTrue(json_response['CanRelist'])

        # check if there is Promotions element and verify the values of Name and Description keys
        promotions_element = json_response["Promotions"]

        for list_item in promotions_element:
            if list_item['Name'] == "Gallery":
                self.assertEqual(list_item['Description'], "2x larger image") 
       

if __name__ == '__main__':
    unittest.main()


        
