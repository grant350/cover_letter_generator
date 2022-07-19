# cover_letter_generator

## generate coverletter in pdf so that mistakes don't happen

## install dependencies
### pip or pip3  install -r requirements.txt

## run program
### python or python3 cover_letter_gen.py

## edit variables or add variables
### inside the template.txt use {} to place a variable key which should be in the json file. Add more keys as you wish, just make sure you add them to the template and cover_letter_gen.json

## change the template as needed to fit what you need, reccomended to start it in google docs and past into the template


## How to use paragraphs in template to better organize the template?
### any value thats an array will be made as a paragraph

```json
{
    "paragraph1":[
    "im a sentence 1",
    "im a sentence 2",
    "im a sentence 3"
  ],
  "paragraph2":[
    "im a sentence 1",
    "im a sentence 2",
    "im a sentence 3"
  ]
}

```