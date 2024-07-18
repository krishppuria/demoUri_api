from rest_framework import serializers
from utils.errorHandling import emailValidationError,fileError, stringRequiredFieldError,listError, notRequiredError, choiceRequiredFieldError, numberRequiredFieldError
from datetime import datetime

# ----------------------------------------------------------------
# Define Candidate Signup serializer
# ----------------------------------------------------------------

class CandidateSignUp(serializers.Serializer):
    firstName = serializers.CharField(error_messages=stringRequiredFieldError("First name"))
    lastName = serializers.CharField(error_messages=stringRequiredFieldError("Last name"))
    email = serializers.EmailField(error_messages=stringRequiredFieldError("Email"))
    phone = serializers.IntegerField(min_value=10000000, error_messages=numberRequiredFieldError("Mobile number"))
    country = serializers.CharField(error_messages=stringRequiredFieldError("Country"))
    password = serializers.CharField(error_messages=stringRequiredFieldError("Password"))
    fcmToken = serializers.CharField(
        required=False,
        allow_null=True,
        error_messages= notRequiredError('Fcm Token'),
    )
    createdAt = serializers.DateTimeField(
        required=False,
        default = datetime.now,
    )
    account = serializers.CharField(
        required=False,
        default= "Active",
    )
