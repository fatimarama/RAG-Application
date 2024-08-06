import sys

from custom_logger import logger


# function is created, it is taking error name and error detail as input 
# python sys module is providing error detail
# exc returns tuple of 3 (type, error, traceback)
# __, means empty, we only want the traceback, because we dont want the first two
# filename: we are extracting the file name from traceback
# exc_tb.tb_lineno: is the error line number

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# error message, and error detail is coming from error log
# super init means we are inheriting from the base class
# then we are returning the error message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
