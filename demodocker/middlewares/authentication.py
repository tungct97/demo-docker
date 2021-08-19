from django.conf import settings

from rest_framework import authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework.exceptions import AuthenticationFailed as RestAuthenticationFailed
from demodocker.middlewares.http_exception import AuthenticationFailed


class Authentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        # if settings.USE_BATCH:
        #     access_token = request.META.get('HTTP_AUTHORIZATION').split("Bearer ")[1]
        #     if settings.AWS_SECRET_ACCESS_KEY and settings.AWS_ACCESS_KEY_ID:
        #         self.cognito_client = boto3.client('cognito-idp',
        #                                            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        #                                            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        #                                            region_name=settings.AWS_S3_REGION_NAME)
        #     else:
        #         self.cognito_client = boto3.client('cognito-idp', region_name=settings.AWS_S3_REGION_NAME)
        #
        #     try:
        #         cognito_user = self.cognito_client.get_user(
        #             AccessToken=access_token
        #         )
        #     except Exception:
        #         raise AuthenticationFailed()
        #     cognito_user_id = list(filter(lambda x: x['Name'] == 'sub', cognito_user['UserAttributes']))[0]['Value']
        #     user = User.objects.filter(cognito_user_id=cognito_user_id).first()
        #     validated_token = access_token
        # else:
        jwt_authentication = JWTAuthentication()
        try:
            user, validated_token = jwt_authentication.authenticate(request)
        except InvalidToken:
            raise AuthenticationFailed()
        except RestAuthenticationFailed:
            raise AuthenticationFailed()
        except Exception:
            raise AuthenticationFailed()
        if not user:
            raise AuthenticationFailed()
        return user, validated_token
