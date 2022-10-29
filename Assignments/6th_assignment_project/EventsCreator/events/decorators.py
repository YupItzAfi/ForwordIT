from django.http import HttpResponse

from .models import Event


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_roles=[], action="view"):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            event = None
            sensitive_actions = ['edit', 'delete', 'add_events']
            not_sensitive_actions = ['book', 'refund', 'create_object']

            if 'pk' in kwargs:
                event = Event.objects.get(id=kwargs['pk'])

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if (group in allowed_roles and event and request.user == event.user) or group == 'admin':
                return view_func(request, *args, **kwargs)
            elif action in sensitive_actions and event and request.user == event.user or action in not_sensitive_actions:
                return view_func(request, *args, **kwargs)
            else:
                if event:
                    return HttpResponse(status=403, content=f"<!DOCTYPE html>403, You are not allowed to this page. Only <em>{event.user}</em> (or some users) and the admins can {action} <b>{event.title}</b>")
                else:
                    return HttpResponse(status=403, content=f"<!DOCTYPE html>403, You are not allowed to {action} this.")

        return wrapper_func
    return decorator
