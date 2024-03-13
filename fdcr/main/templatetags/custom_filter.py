from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter() 
def para(description):
    text = ''
    is_new_line = False
    descriptions = description.split('\n')
    for i in descriptions:
        if is_new_line:
            text += ('<p class="txt-sec2 ">' + i + '</p>')
    
        else:
            if (len(descriptions)) == 1:
                text += ('<p class="txt-sec2 pt-lg-3 pb-5 pt-5">' + i + '</p>')
            else:
                text += ('<p class="txt-sec2 pt-lg-3 pt-5">' + i + '</p>')
            is_new_line = True
    print(text)
    return mark_safe(text)

@register.filter() 
def para_2(description):
    text = ''
    for i in description.split('\n'):
        text += ('<p>' + i + '</p>')
    return mark_safe(text)



register.filter('para', para)
register.filter('para_2', para_2)