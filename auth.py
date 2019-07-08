from sanic.response import json
from functools import wraps

def check_request_for_authorization_status(request):
    secret = '45ouZ16zyeuMGDHspOADMdZQn3O9AmICo68BprdjIHDsIjj0AwF8i7fDXVEnJiyf'
    return request.headers.get('Authorization') == secret

def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authorized = check_request_for_authorization_status(request)

            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response
            else:
                return json({ "status": "Unauthorized" }, 401)
        return decorated_function
    return decorator
