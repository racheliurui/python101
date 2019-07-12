# the static global config
from random import randrange


def getRandom():
    return randrange(10)

# this will run only once when included with other function multiple times or being reference across multiple modules
a=getRandom()