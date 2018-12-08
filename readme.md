Exceptions defined:

The **try** block lets you test a block of code for errors.

The **except** block lets you handle the error.

The **finally** block lets you execute code, regardless of the result 
of the try- and except block

Main Code required for defined exception:
    try:
        #Code
    except ValueError as e:
        print(e, file=sys.stderr)
    #ValueError is one type of exception type:
    
    

[Exception types](https://docs.python.org/3.6/library/exceptions.html):

asdf

ValueError
1. object is of the right type, but contains an inappropriate value
example: converting to an int from a non numeric string

KeyError
1. Look-up in a mapping fails
example: looking up a non existing key in a dictionary.

IndexError
1. integer index is out of range
example: you can see this when indexing out of a list

TyperError:
1. Raised when an operation or function is applied to an object of 
inappropriate type. The associated value is a string giving details 
about the type mismatch.

