# APITest #
Sample API test

# Library Dependencies #
python 3.x
unittest
requests 2.22.0
configparser

# Steps To Run #
1. Please make sure the above software/library dependencies are installed on your machine
2. Once you clone the git repository or downloaded the source code, you would find the directory named 'APITest'. Under this directory, you would find 'code' and 'config' directories.
3. The 'config' directory has the 'api_testing.config' file, which contains the base information like the API URL. If you would be using this script to test a different API, change the URL parameter under the '[test_acceptance]' section.
4. Open a command prompt and go the './APITest/code' directory. There would be two python files named 'testcases.py' and 'common.py'. To run the test cases, rn the following command ont he prompt:
> python testcases.py
5. The test results would be displayed on the commond prompt itself.

