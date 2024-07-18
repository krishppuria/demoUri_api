# ----------------------------------------------------------------
# Email validation
# ----------------------------------------------------------------

def emailValidationError():
    error_messages={
        'required': 'Please enter your email. This field is required.',
        'blank': 'The email field cannot be left blank. Please enter a email.',
        'invalid': 'Please enter a valid email address.',
        'null': 'Email field cannot be null. Please provide a valid email.',
    }
    return error_messages

# ----------------------------------------------------------------
# String fields errors
# ----------------------------------------------------------------

def stringRequiredFieldError(fieldName):
    error_messages={
        'required': f'Please enter your {fieldName}. This field is required.',
        'blank': f'The {fieldName} field cannot be left blank. Please enter a {fieldName}.',
        'invalid': f'The provided {fieldName} value is not a valid string. Please enter a valid {fieldName}.',
        'null': f'{fieldName} field cannot be null. Please provide a valid value.',
    }
    return error_messages

# ----------------------------------------------------------------
# List fields errors
# ----------------------------------------------------------------

def listError(fieldName):
    error_messages={
        'not_a_list': f'The provided {fieldName} value is not a valid List. Please provide a valid value or leave it empty.',        
        'required': f'Please enter your {fieldName}. This field is required.',
        'blank': f'The {fieldName} field cannot be left blank. Please enter a {fieldName}.',
        'invalid': f'The provided {fieldName} value is not a valid List. Please enter a valid {fieldName}.',
        'null': f'{fieldName} field cannot be null. Please provide a valid value.',
    }
    return error_messages

# ----------------------------------------------------------------
# Number fields error
# ----------------------------------------------------------------
def numberRequiredFieldError(fieldName):
    error_messages={
        'required': f'Please provide your {fieldName}. This field is required.',
        'blank': f'The {fieldName} cannot be left blank. Please enter.',
        'min_value': f'Please enter valid {fieldName}.',
        'invalid': f'The provided {fieldName} value is not a valid number. Please enter a valid number.',
        'null': f'{fieldName} field cannot be null. Please provide a valid value.',
    }
    return error_messages

# ----------------------------------------------------------------
# Choice fields error
# ----------------------------------------------------------------
def choiceRequiredFieldError(fieldName):
    error_messages={
        'required': f'Remember to choose a {fieldName}.',
        'blank': f'The {fieldName} field cannot be left blank. Please choose a account type.',
        'invalid_choice': f'The selected {fieldName} is not valid. Please choose from the available options.',
        'null': f'{fieldName} field cannot be null. Please provide a valid value.',
    }
    return error_messages


# ----------------------------------------------------------
# File fields error messages
# ----------------------------------------------------------

def fileError(field_name):
    return {
        'required': f'{field_name} is required. Please upload a valid image file.',
        'invalid': f'Invalid {field_name}.',
        'no_name': f'{field_name} has no name.',
        'empty': f'{field_name} is empty.',
        'max_length': f'{field_name} exceeds the maximum length.',
        'contradiction': f'Contradiction detected in {field_name}.'
    }

# -----------------------------------------------------------------
# Not required error
# -----------------------------------------------------------------
def notRequiredError(fieldName):
    error_messages={
        'null': f'{fieldName} field should not be null. Please provide a valid value or leave it empty.',
        'blank': f'The {fieldName} cannot be left blank. Please provide a valid value or leave it empty.',
        'invalid': f'The provided {fieldName} value is not a valid string.Please provide a valid value or leave it empty.',
        'not_a_list': f'The provided {fieldName} value is not a valid List.Please provide a valid value or leave it empty.',
        'invalid_choice': f'The selected {fieldName} is not valid. Please choose from the available options or leave it empty.',
    }
    return error_messages