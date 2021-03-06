#!/usr/bin/python
import sys, io, collections, six, json, requests, subprocess

from jinja2 import Template, Environment, BaseLoader, FileSystemLoader


txt = """My favorite numbers: {% for n in range(1,10) %}
{{n}} {% endfor %}"""
t = Template(txt)
tr = t.render()
print(tr)


colors = ["red", "blue"]
txt = """colors: {% for color in colors %} 
{{color}} {% endfor %}"""
t = Template(txt)
tr = t.render(colors=colors)
print(tr)


NAMES = ["Melinda", "Thomas", "Zac"]
txt = "{% for name in NAMES %}Hello {{ name }} \n{% endfor %}"
t = Template(txt)
tr = t.render(NAMES=NAMES)
print(tr)


parameters = {'parameter1':'text', 'parameter2':'text', 'parameter3':'text', 'parameter4':'text'}
input_jinja2_template = '''{% for key, value in parameters.items() %}<p>{{key}}<input type = "{{value}}" name = "{{key}}" /></p>
{% endfor %}'''
t = Template(input_jinja2_template)
trm = t.render(parameters=parameters)
print(trm)

### https://stackoverflow.com/questions/39288706/jinja2-load-template-from-string-typeerror-no-loader-for-this-environment-spec
with open('menu.html','w') as f:
    f.write(tr)
    
# txt ="""<HTML>
# <HEADER>header</HEADER>
# <BODY>body
#    {% include 'menu.html' %}
# </BODY>
# </HTML>
# """
# t = Environment(loader=FileSystemLoader(searchpath="./")).get_template('menu.html')
# tr = t.render()
# print(tr)


txt ="""<HTML>
<HEADER>header</HEADER>
<BODY>body
   {% include 'menu.html' %}
</BODY>
</HTML>
"""
t = Environment(loader=FileSystemLoader(searchpath="./")).from_string(txt)
tr = t.render()
print(tr)




txt ="""<HTML>
<HEADER>header</HEADER>
<BODY>body
{{ menu }}</BODY>
</HTML>
"""
t = Template(txt)
tr = t.render(menu=trm)
print(tr)




### https://www.youtube.com/watch?v=bxhXQG1qJPM


colors = ["red", "blue"]
txt = """Colors: {% if truth %}{% for color in colors %} 
{{color}}{% endfor %}{% else %}No colors{% endif %}"""
t = Template(txt)
tr = t.render(colors=colors, truth = True)
print(tr)

t = Template(txt)
tr = t.render(colors=colors, truth = False)
print(tr)