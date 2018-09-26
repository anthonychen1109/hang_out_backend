from api.serializers import UserSerializer

# helper method that returns info for user
# passes back user info for frontend usage after getting a token
def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
