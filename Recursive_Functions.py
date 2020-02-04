## WITH A LIST

# look = [4, 5, 6, 7, 8, 'kjlsdhgfissacklgjsheu', 'ld', 'sd;']


# def recursive(a):
#   for x in a:
#       if isinstance(x, str):
#           if 'issac' in x:
#               return x

# find = recursive(look)

# print(find)

## WITH A DICTIONARY

g = {'sdf':'kkisaacd','dlk':432,'324':'dslkisaacl','dflkj':2343}

def find(a):
    lst = []
    for value in a.values():
        if isinstance(value, str):
            if 'isaac' in value:
                lst.append(value)
 
    return lst

find = find(g)
print(find)