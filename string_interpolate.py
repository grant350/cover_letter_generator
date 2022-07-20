import json

def interpolate(variables):
   with open ("./template.txt", "r", encoding='utf-8') as f:
      textfile = f.read()
      for key in variables.keys():
         value= variables[key]
         if (type(value) in (tuple, list) ):
            newstring=""
            for string in value:
               string=string.format(**variables)
               newstring+=string
            variables[key]=newstring
         else:
            variables[key] = value.format(**variables)
      text = textfile.format(**variables)
      return text