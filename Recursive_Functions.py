look = [4, 5, 6, 7, 8, 'kjlsdhgfissacklgjsheu', 'ld', 'sd;']


def recursive(a):
  for x in a:
      if isinstance(x, str):
          if 'issac' in x:
              return x

find = recursive(look)

print(find)
