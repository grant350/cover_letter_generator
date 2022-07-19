import json

def interpolate(variables):
   with open ("./template.txt", "r", encoding='utf-8') as f:
      textfile = f.read()
      for key in variables.keys():
         text = textfile.format(**variables)
         return text