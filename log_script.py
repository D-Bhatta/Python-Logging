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

basic_config()