'''
    Python 2 syntax, this will not work in Python 3, because print is a
    function and therefore cannot be called without parenthesis.

    Python 2:
        "1 + 1 = 2"

    Python 3:
        SyntaxError: invalid syntax
'''
print "1 + 1 = ", 1 + 1

'''
    Python 3 syntax, this will produce a different output for Python 2.

    Python 2:
        "(' 1 + 1 = ', 2)"

    Python 3:
        "1 + 1 = 2"
'''
print("1 + 1 = ", 1 + 1)
