#!/usr/bin/python
import datetime
import math

aaa = 10
bbb = f"{aaa}string"
print(bbb)

print(f"arithmetic expression = {5 * 5}")


val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
print(f'{today:%Y-%m-%d %H:%M}')

### Backslash Cannot be used in format string directly.

### https://www.datacamp.com/community/tutorials/f-string-formatting-in-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9062578&gclid=EAIaIQobChMImYK3xdWt8QIVQeN3Ch0y0w8MEAAYASAAEgJ-mfD_BwE

### https://zetcode.com/python/fstring/


### = has special meaning get value
x = 0.8
print(f'{math.cos(x) = }')
print(f'{math.sin(x) = }')


### multiline fstring
msg = (
    f'Name: {name}\n'
    f'Age: {age}\n'
)

print(msg)

val = 12.3
print(f'{val:.2f}')
print(f'{val:.5f}')


for x in range(1, 11):
    print(f'{x:02} {x*x:3} {x*x*x:4}')


s1 = 'a'
s2 = 'ab'
s3 = 'abc'
s4 = 'abcd'
print(f'{s1:>10}')
print(f'{s2:>10}')
print(f'{s3:>10}')
print(f'{s4:>10}')


a = 300
# hexadecimal
print(f"{a:x}")

# octal
print(f"{a:o}")

# scientific
print(f"{a:e}")