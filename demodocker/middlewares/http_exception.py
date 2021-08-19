from rest_framework import status


class AuthenticationFailed(Exception):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'

#
# class BasesException(Exception):
#
#     def __init__(self, msg_code):
#         self.msg_code = msg_code
#
#     def __str__(self):
#         return str(self.msg_code)
#
#
# class BadRequestError(BasesException):
#     status_code = 400
