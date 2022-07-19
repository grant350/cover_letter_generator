import json

def interpolate(variables):
   with open ("./template.txt", "r", encoding='utf-8') as f:
      textfile = f.read()
      for key in variables.keys():
         value= variables[key]
         print('value: '+ str(value))
         print(type(value) in (tuple, list))
         if (type(value) in (tuple, list) ):
            newstring=""
            for string in value:
               print("string"+string)
               newstring+=string+". "
            variables[key]=newstring
         print(variables[key])
      text = textfile.format(**variables)
      return text