# -*- coding -*-

api_code = {
    'success': 200,
    'server_error':500,
    'param_error': 501,
}

api_message = {
    'success': 'success'
}


def ChatResponse(code=api_code['success'], data=None, message=api_message['success']):
    return {
        'code': code,
        'data': data,
        'message': message
    }