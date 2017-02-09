x = [0, 1, 2, 3, 4, 5]

# def update_list(x):
#     new_list = x[x[1]:len(x)-1]
#     print new_list

# update_list(x)

def chop(x):
    del x[0]
    del x[len(x)-1]
    return None

chop(x)
