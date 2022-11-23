from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

#this is a custom filter 

register = template.Library()
user_model = get_user_model()



@register.filter
def author_details(author, current_user=None):
    if not isinstance(author, user_model):  #to see if we are working with User object
        return ""

    if author == current_user:
      return format_html("<strong>me</strong>") #marking the return string as safe with format_html

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

