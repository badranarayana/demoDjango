from django import template

register = template.Library()

full_name = "badra narayana"


# {first_name}
# {last_name}

# all custom tags going to be here
def modify_name(value, arg):
 # if arg is first_name: return the first string before space
 if arg == "first_name":
     return value.split(" ")[0]
 # if arg is last_name: return the last string before space
 if arg == "last_name":
     return value.split(" ")[-1]
 # if arg is title_case: return the title case of the string
 if arg == "title_case":
     return value.title()
 return value


# USA
# US
#
# IND
# IN

def get_chars(value, num):
    return value[0:num]

register.filter('modify_name', modify_name)
register.filter('get_chars', get_chars)

