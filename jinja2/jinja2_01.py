#!/usr/bin/python
import sys, io, collections, six, json, requests, subprocess

from jinja2 import Template


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
input_jinja2_template = '''
{% for key, value in parameters.items() %}
<p>{{key}}<input type = "{{value}}" name = "{{key}}" /></p>{% endfor %}
'''

t = Template(input_jinja2_template)
tr = t.render(parameters=parameters)
print(tr)