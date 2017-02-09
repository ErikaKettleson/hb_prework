def get_Fermet_values():
    a = int(raw_input("Give me a value for a: "))
    b = int(raw_input("Give me a b: "))
    c = int(raw_input("Give me a c: "))
    n = int(raw_input("Give me a value for n larger than 2: "))
    check_fermat(a, b, c, n)


def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print "Holy smokes, Fermat was wrong!"
        else:
            print "No, that doesn\'t work."
    else:
        print "n has to larger than 2 to test this out!"

get_Fermet_values()
