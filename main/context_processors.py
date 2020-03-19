from django.conf import settings


# def get_setting(setting_name, default):
#     if hasattr(settings, setting_name):
#         return getattr(settings, setting_name)
#     return default

def main(request):
    return {
        'LOGIN_URL_FOR_LINK': 'accounts/login/',
        'LOGOUT_URL_FOR_LINK' : 'accounts/logout/',
    }