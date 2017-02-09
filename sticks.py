def check_sticks():
    print "I need 3 values for sticks!"
    a = int(raw_input("1st stick length:"))
    b = int(raw_input("2nd stick length:"))
    c = int(raw_input("3rd stick length:"))
    is_triangle(a, b, c)      


def is_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print "No"
    else:
        print "Yasssss"

check_sticks()
