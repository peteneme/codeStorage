#!/usr/bin/python

add_one = lambda x: x + 1
print(add_one(2))

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

sum = lambda x, y: x + y
print(sum(1,6))