""" The Logging Module
The logging module in Python is a ready-to-use and powerful module that is designed to meet the needs of beginners as well as enterprise teams. It is used by most of the third-party Python libraries, so you can integrate your log messages with the ones from those libraries to produce a homogeneous log for your application.

Adding logging to your Python program is as easy as this: """
import logging

""" With the logging module imported, you can use something called a “logger” to log messages that you want to see. By default, there are 5 standard levels indicating the severity of events. Each has a corresponding method that can be used to log events at that level of severity. The defined levels, in order of increasing severity, are the following:

DEBUG
INFO
WARNING
ERROR
CRITICAL
The logging module provides you with a default logger that allows you to get started without needing to do much configuration. The corresponding methods for each level can be called as shown in the following example: """
def The_Logging_Module():
    logging.debug('This is a debud message')
    logging.info('This is a info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')


""" output:
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message """

""" ---------------------------------------------------------------------------------------------------- """

def basic_config():
    logging.basicConfig(level='DEBUG', filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')
    The_Logging_Module()

""" output:
root - DEBUG - This is a debud message
root - INFO - This is a info message
root - WARNING - This is a warning message
root - ERROR - This is an error message
root - CRITICAL - This is a critical message
root - DEBUG - This is a debud message
root - INFO - This is a info message
root - WARNING - This is a warning message
root - ERROR - This is an error message
root - CRITICAL - This is a critical message """


def formatting_output():
    logging.basicConfig(level='DEBUG', filename='app.log', filemode='a', format='%(process)d-%(levelname)s-%(message)s')
    logging.warning('This is a warning with process id')

""" output:
6756-WARNING-This is a warning with process id """

def formatting_output_2():
    logging.basicConfig(level='INFO', filename='app.log', filemode='a', format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info('This is info with date and time')

""" output:
2019-12-19 11:59:40,336-This is info with date and time
19-Dec-19 12:02:01-This is info with date and time """

def logging_variable_data():
    name = 'John'
    logging.basicConfig(level='DEBUG', filename='app.log', filemode='a', format='%(asctime)s-%(process)d-%(levelname)s-%(message)s')
    logging.error('%s raised an error', name)

""" output:
2019-12-19 12:14:49,628-10088-ERROR-John raised an error """

def logging_variables_with_fstrings():
    animal = 'cat'
    logging.basicConfig(level='DEBUG', filename='app.log', filemode='a', format='%(asctime)s-%(process)d-%(levelname)s-%(message)s')
    logging.error(f'{animal} has encountered an error')

""" output:
2019-12-19 12:17:07,614-12612-ERROR-cat has encountered an error """
