import sys
def convert(s):
    x = -1
    try:
        if x == -1:
            x = int(s)
        print("conversion was successful x =", x)
    except (ValueError, TypeError) as e:
        print('Conversion error: {}'.format(str(e)),file=sys.stderr)
    return  x


s = '123'

convert(s)
