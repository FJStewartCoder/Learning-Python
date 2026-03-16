# MODULES
# modules are a set of variables, functions and classes that are externally imported
# modules provide you with new functionality instead of creating it yourself

# IMPORT
# to import a module, use the import keyword

# the random module allows for random generation
# random will not be covered here
import random

# to use functions from a module use module_name.function

# use a function from random
random.randint(1, 10)

# IMPORT AS
# if you don't like the module name, you can change its alias
# use import module_name as module_alias to change the alias

# import the random module using the r alias
import random as r

# use a function from random but with r alias
r.randint(1, 20)

# FROM ... IMPORT
# if you don't want to import all functions, use from ... import
# import as can be also used here
# you can import several functions

# import random.randint and random.random
from random import randint, random

# we now don't need to use any alias
random()
randint(10, 100)

# FROM ... IMPORT *
# use the * to import all functions/classes/vars from a module

# imports all functions from random and you don't need any alias
from random import *


# FROM ... IMPORT ... as ...
# need more? use this

# import the random.randint function as a new alias rint
from random import randint as rint

# please don't give the alias a bad name like "rint"
rint(10, 50)


# CREATING A MODULE
# you may want more modular code; so, you can make your own modules
# any Python file you make can be imported using the file name

# for example, "menus.py" can be imported as
# import menus

# all code in the module will be run when you import it
# any global scope code will be run; be careful