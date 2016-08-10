from django.conf import settings  # import the settings file


def site_settings_to_templates(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {
        'site': settings.SITE
    }
