from utils.respone import errorResponse, successResponse
from .models import Account
from rest_framework.decorators import api_view
from . import serializers
from rest_framework import status
from config.jwtToken import get_tokens, verify_token, dataWithObjectId
import bcrypt
from datetime import datetime
from bson import ObjectId
from django.core.mail import send_mail
from django.template.loader import render_to_string


# ----------------------------------------------------------------
# signup user
# ----------------------------------------------------------------

@api_view(['POST'])
def signup(request):

    phone = request.data.get('phone')
    email = request.data.get('email')

    # Email Already Exists
    email_already = Account.get(email)
    if (email_already):
        return errorResponse("The email provided already exists.Please use a different email.")

    # Mobile Number already Exists
    phone_already = Account.getUserByPhone(int(phone))
    if (phone_already):
        return errorResponse("The mobile number provided already exists.Please use a different mobile number.")
    serializer = serializers.CandidateSignUp(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['password'] = bcrypt.hashpw(
            serializer.validated_data['password'].encode('utf-8'),
            bcrypt.gensalt()
        )
        serializer.validated_data['email'] = serializer.validated_data['email'].lower()
        user = Account.create(serializer.validated_data)
        data = get_tokens(user)
        return successResponse(data,"Congratulations! Your OTP has been successfully verified.")
    return errorResponse(list(serializer.errors.values())[0][0])



# ----------------------------------------------------------------
# Profile
# ----------------------------------------------------------------

@api_view(['GET'])
def profile(request):

    # verify token
    token = verify_token(request)
    if not token:
        return errorResponse("The token provided is not valid. Please provide a valid token.")

    user = Account.getUserByEmail(request.user['email'])
    if not user:
        return errorResponse("Something went wrong please check again.")
    data = dataWithObjectId(user)
    return successResponse(data, "My profile")


# ----------------------------------------------------------------
# User Profile
# ----------------------------------------------------------------

@api_view(['GET'])
def userProfile(request):

    # verify token
    token = verify_token(request)
    if not token:
        return errorResponse("The token provided is not valid. Please provide a valid token.")
    email = request.GET.get('email')
    if not email:
        return errorResponse("The email is not valid. Please provide a valid email.")
    user = Account.get(email)
    return successResponse(user, "My profile")
