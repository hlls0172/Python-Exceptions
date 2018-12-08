
p = '/path/to/datafile.dat'
real = '/home/hill/Python/test/src/readme.md'
files = [p, real]

for file in files:
    try:
        f = open(file, 'r')
        print("this will not print")
        print(f.read())
    except OSError as e:
        print('Could not process file because{}'.format(str(e)))

