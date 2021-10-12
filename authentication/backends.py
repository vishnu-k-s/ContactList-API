import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework_jwt.utils import jwt_decode_handler


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        print('hi')
        print(auth_data)
        print('hi2')
        if not auth_data:
            return None

        prefix = auth_data.decode('utf-8').split(' ')
        token1 = auth_data.decode('utf-8').split(' ')

        #a_d="b'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imp3dGp3dGp3dCJ9.NQvGXZXzHpfJpUtNePMPmR9iBZpJ_q2viAeuLL-K_fk'"
        #token2 = a_d.decode('utf-8').split(' ')
        print(token1)
        #print(token2)
        payload=jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imp3dGp3dGp3dCJ9.OATQTDtYIUW_CYQEvedzwu0ht8-FT1X_5VrJdGRZwME','JWTSECRETKEYJWTSECRETKEYJWTSECRETKEY',algorithms="HS256")
        print(payload)
        try:
            #print('error1')
            #payload=jwt.decode(token1,'JWTSECRETKEYJWTSECRETKEYJWTSECRETKEY')
            #payload=jwt.decode('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InN0cmluZzEyMzQifQ.jcmffK8ue6Jjn5gtckLCBNoNqK7XHD_AzRSsuq1K74o')
            #payload = jwt_decode_handler(token)
            #print('error2')
            
             
            '''
              payload={
                "username": "newuser",
                "first_name": "newuser",
                "last_name": "newuser",
                "email": "newuse2@gmail.com",
                "phone_number": "newuser2"
            }
            '''
            
            user = User.objects.get(username=payload['username'])
            
            return(user,token1)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Your Token is expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Your token is Invalidd')
        
        return super().authenticate(request)
        