# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


# Core modules
import datetime

# Pip modules
import camelcase

# Custom modules
import validator

today = datetime.date.today()

camel = camelcase.CamelCase()
text = 'hello there world'

print(camel.hump(text))
