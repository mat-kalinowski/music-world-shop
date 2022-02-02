from django import template

register = template.Library()

def check_active_url(value, arg):
    # if arg is first_name: return the first string before space
    print("filter")
    if value == arg:
        return "c-profile-button-active"

    return ""
    
register.filter('check_active_url', check_active_url)