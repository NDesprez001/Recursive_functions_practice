# WITH A LIST

look = [4, 5, 6, 7, 8, 'kjlsdhgfissacklgjsheu', 'ld', 'sd;']


def recursive(a):
  for x in a:
      if isinstance(x, str):
          if 'issac' in x:
              return x

# find = recursive(look)

# print(find)

# WITH A DICTIONARY

g = {'sdf':'kkisaacd','dlk':432,'324':'dslkisaacl','dflkj':2343}

def find(a):
    lst = []
    for value in a.values():
        if isinstance(value, str):
            if 'isaac' in value:
                lst.append(value)
 
    return lst

# find = find(g)
# print(find)

# IDENTIFIYING WETHER THE PARAM IS A LIST OR A DICT.

n = [4, 5, 6, 7, 8, 'kjlsdhgfissacklgjsheu', 'ld', 'sd;']
d = {'sdf':'kkisaacd','dlk':432,'324':'dslkisaacl','dflkj':2343}


def find_lst_dict   (a):
    if isinstance(a, list):
        return recursive(a)
    if isinstance(a, dict):
        return find(a)
    else:
        return 'That is not a list'
 

# def find_dict(a):
#     if isinstance(a, dict):
#         return find(a)
#     else:
#         return 'That is not a dictionary'




# print(find_lst(n))
# print(find_dict(d))

# print(find_lst_dict(d))

## RECURSIVE

n = [4, 5, 6, 7, 8, 'kjlsdhgfisaacklgjsheu', 'ld', 'sd;', 'akjfhisaacdslkajfh', ['isaac'], {'sdf':'kkisaacd','dlk':432,'324':'dslkisaacl','dflkj':2343}]
d = {'sdf':'kkisaacd','dlk':432,'324':'dslkisaacl','dflkj':2343}
str_to_find = 'isaac'

def rec(a):
    if isinstance(a, str):
        if str_to_find in a:
            print(a)
    if isinstance(a, list):
        for i in a:
            rec(i)
    if isinstance(a, dict):
        for value in a.values():
            rec(value)


rec(n)
