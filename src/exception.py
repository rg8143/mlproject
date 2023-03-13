import sys
from logger import logging

def error_message_detail(error, error_details:sys):
    _, _, exc_tb=error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_num = exc_tb.tb_lineno
    err_msg = str(error)

    error_message = f"Error occured in python script - file name : [{file_name}], line number : [{line_num}], error message : [{err_msg}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):

        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details=error_detail)

    def __str__(self):
        return self.error_message
    


# if __name__=="__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero error occured!!")
#         raise CustomException(e, sys)