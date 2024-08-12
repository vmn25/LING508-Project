# English to Vietnamese Noun Translator

## Get a word from the database
You can translate an English noun into a Vietnamese noun and its classifier (if applicable) using the "Get a word from the database" interface.
Enter a word such as `bird` in the box and click "Submit".
The page will display the parse for that word as a JSON string, for example
```json
  {
    "noun": {
      "english": "bird",
      "classifier": "con",
      "vietnamese": "chim",
    }
  }
```

## Add a word to the database
You can add an English noun and its Vietnamese translation to the database using the "Add a word to the database" interface.
There are three input boxes: one for the English translation of the noun, one for the Vietnamese classifier, and one for the Vietnamese translation of the noun.
For example, you would enter `pig` in the English Input, `con` in the Classifier Input, and `heo` in the Vietnamese input.
The page will respond that the noun has been added successfully or that it already exists in the database.
