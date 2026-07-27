from rest_framework.views import exception_handler
from rest_framework.response import Response

ERROR_MESSAGES = {
    "This field is required.": {
        "message": "Please fill in all required fields.",
        "code": 400
    },
    "Invalid data. Expected a dictionary, but got str.": {
        "message": "Invalid data format. Please provide a valid JSON object.",
        "code": 400
    },
    "Authentication credentials were not provided.": {
        "message": "Please login first.",
        "code": 401
    },
    "Token is invalid or expired": {
        "message": "Your session has expired. Please login again.",
        "code": 401
    },
    "You do not have permission to perform this action.": {
        "message": "You don't have enough permissions.",
        "code": 403
    },
    "No active account found with the given credentials": {
        "message": "Invalid username or password.",
        "code": 401
    },
}

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        errors = response.data
        
        if isinstance(errors, dict):
            first_key = next(iter(errors))
            first_error = errors[first_key]
            message = first_error[0] if isinstance(first_error, list) else first_error
        else:
            message = str(errors)
        
        custom_error = ERROR_MESSAGES.get(message)
        
        if custom_error:
            return Response({
                "success": False,
                "code": custom_error["code"],
                "message": custom_error["message"]
            }, status=custom_error["code"])
        
        return Response({
            "success": False,
            "code": response.status_code,
            "message": message
        }, status=response.status_code)
    
    return response