from django.shortcuts import redirect


def pet_only(view_func):

    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'pets':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')

    return wrapper_function


def not_auth_pet(view_func):

    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'pets':
            return redirect('pet_home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function
