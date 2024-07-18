from rest_framework.response import Response
from rest_framework import status

# ----------------------------------------------------------------
# Api Response Success
# ----------------------------------------------------------------

def successResponse(data,message,s=status.HTTP_200_OK ):
    return Response({ "success" : True,"message" : message, "data" :data , }, status= s )

# ----------------------------------------------------------------
# Api Response Error
# ----------------------------------------------------------------

def errorResponse(message,s=status.HTTP_200_OK):
    return Response({ "success" : False,"message" : message, }, status=s )

