from multiprocessing import AuthenticationError
import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TrustMeBroAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get("Trust-Me")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed(f"No user {username}")
        

class JWTAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None
        
        try:
            # Check for 'Bearer ' prefix and remove it
            auth_parts = auth_header.split()
            if len(auth_parts) != 2 or auth_parts[0].lower() != "bearer":
                raise AuthenticationFailed("Invalid token format")
            
            token = auth_parts[1]
            
            # Decode the token
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"],
            )
            
            # Get user from payload
            user_id = payload.get("pk")
            if not user_id:
                raise AuthenticationFailed("Invalid token payload")
            
            user = User.objects.get(pk=user_id)
            return (user, None)
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Invalid token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")
        except Exception as e:
            raise AuthenticationFailed(f"Authentication failed: {str(e)}")