def success_response(status_code, message, data):
    return {
        "statusCode": status_code,
        "message": message,
        "data": data
    }

def error_response(status_code, error, data):
    return {
        "statusCode": status_code,
        "error": error,
        "data": data
    }