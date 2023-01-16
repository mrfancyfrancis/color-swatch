import random


def rgbtohex(input={}):
    params = (input['red'], input['green'], input['blue'])
    return '%02x%02x%02x' % params


def random_number(max):
    return random.randint(0, max)


def random_byte():
    return random.randint(0, 255)


def random_percentage():
    return str(random.randint(0,100))+'%'


def random_type():
    from colors.models import Color
    return random.choice(Color.choices)
