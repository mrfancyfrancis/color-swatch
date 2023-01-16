
def rgbtohex(input={}):
    params = (input['red'], input['green'], input['blue'])
    return '%02x%02x%02x' % params
