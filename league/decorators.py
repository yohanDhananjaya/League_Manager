from django.http import HttpResponse
from league.models import User


def allowed_users(allowed_roles=[]):
    def decorator(view_func):  # View function in views.py
        def wrapper_func(request, *args, **kwargs):
            try:
                user = User.objects.get(email=request.data['email'])
                if user.type.id in allowed_roles:
                    if user.is_online == 1:
                        return view_func(request, *args, **kwargs)
                    else:
                        return HttpResponse('You are not logged in')
                else:
                    return HttpResponse('You are not authorized to this request')
            except Exception as e:
                print(e)
                return HttpResponse('Invalid user data')
        return wrapper_func
    return decorator
