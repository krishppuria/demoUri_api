import jwt
import json

secret_key = "sjjfdsgh875349fg45yuh67j32s3rtt0ejf98eythg"

# ----------------------------------------------------------------
# Get token
# ----------------------------------------------------------------

def get_tokens(user):
    
    json_data = json.dumps(str(user['_id'])).strip("\"")
    user['_id'] = json_data
    
    payload = {
        "userId": user['_id'],
        "email": user['email'],
    }
    
    token = jwt.encode(payload, secret_key )
    user['token'] = token
    return user

# ----------------------------------------------------------------
# Verify token
# ----------------------------------------------------------------

def verify_token(request):

    auth_header = request.META.get('HTTP_AUTHORIZATION')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        algorithms = ["HS256"]
        try:
            payload = jwt.decode(token, secret_key, algorithms)
            setattr(request, 'user', payload)
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.DecodeError:
            return False
        except jwt.InvalidTokenError:
            return False
    return False


# ---------------------------------------------------------
# Return data with objectid
# ---------------------------------------------------------

def dataWithObjectId(data):
    
    json_data = json.dumps(str(data['_id'])).strip("\"")
    data['_id'] = json_data
    
    return data

