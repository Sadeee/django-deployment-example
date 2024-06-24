from django import template

regiser = template.Library()

@regiser.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of  "arg" from the string
    """
    return value.replace(arg,'')

# regiser.filter('cut', cut)