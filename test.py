def convert(s):
    try:
        x = int(s)
        print("conversion was successful x =", x)
    except ValueError:
        print('conversion Failed')
        x = -1
    return  x


s = 123

convert(s)
print('i want to see some crazy stuff')