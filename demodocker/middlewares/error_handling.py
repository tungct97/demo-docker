import logging

from django.conf import settings
from django.http import JsonResponse
from rest_framework import status
# from marshmallow.exceptions import ValidationError
from rest_framework_simplejwt.exceptions import InvalidToken

# from apps.user.models import LanguageChoice
from demodocker.middlewares.http_exception import AuthenticationFailed


class ErrorHandleMiddleware:
    logger = logging.getLogger('request')

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        # if exception and isinstance(exception, ValidationError):
        #     return JsonResponse({'detail': exception.messages}, status=status.HTTP_400_BAD_REQUEST)
        if exception and isinstance(
            exception, (InvalidToken, AuthenticationFailed)
        ):
            return JsonResponse({'detail': '401 Unauthenticated'}, status=exception.status_code)
        # elif exception and isinstance(exception, APIException):
        #     return JsonResponse({'detail': exception.detail}, status=exception.status_code)
        # elif exception and isinstance(exception, BadRequestError):
        #     message_error = get_message(request, exception.msg_code)
        #     return JsonResponse({'detail': message_error}, status=exception.status_code)
        else:
            self.logger.error(exception, exc_info=True)
            message = None
            if settings.DEBUG:
                message = str(exception)
            return JsonResponse({'detail': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# def get_message(request, msg_code):
#     if not (settings.JA_MESSAGES_ERROR.get(msg_code) or settings.MESSAGES_ERROR.get(msg_code)):
#         return msg_code
#     if request.user.language == LanguageChoice.get_value('ja'):
#         return settings.JA_MESSAGES_ERROR[msg_code]
#     return settings.MESSAGES_ERROR[msg_code]
#
#
# def custom_exception_handler(exc, context):
#     response = exception_handler(exc, context)
#     if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:
#         response.data['detail'] = get_message(context['request'], response.data['detail'])
#     return response
