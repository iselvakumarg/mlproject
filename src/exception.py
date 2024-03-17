"""
This code contains the custom exception error msg formatting of the project
"""
import sys

def error_message_detail(error, error_detail: sys):
    """
    This function constructs a detailed error message that includes:
        - The name of the python script where the error occured
        - The line number where the error occured
        - The original error msg itself

        Args:
            error: The original error msg
            error_detail: A reference to the sys module

        Return:
            error_message (str): modified error msg
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number {exc_tb.tb_lineno} error message [{str(error)}]"
    return error_message


class CustomException(Exception):
    """
    This class defines a custom exception type that inherits from the built-in Exception class. 
    It is designed to provide more informative error messages compared to standard exceptions.

    Args:
        error_message (str): str contains the original error msg that describes the error condition
        error_detail (sys): It contains the result of calling sys.exc_info(). 
        This allows the class to extract details about the exception's origin
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
