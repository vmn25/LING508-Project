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

The API can be called directly without the UI, using a GET request.
The endpoint for this example is `http://localhost:5000/noun_data/bird`.
The GET request must contain the desired word in English at the end of the URL.
A complete `curl` command looks like this:
```shell
curl -i -X GET localhost:5000/noun_data/bird
```

## Add a word to the database
You can add an English noun and its Vietnamese translation to the database using the "Add a word to the database" interface.
There are three input boxes: one for the English translation of the noun, one for the Vietnamese classifier, and one for the Vietnamese translation of the noun.
For example, you would enter `pig` in the English Input, `con` in the Classifier Input, and `heo` in the Vietnamese input.
The page will respond that the "Noun has been added successfully" or that the "Noun is already added" in the database.

The endpoint can also be called directly via `curl`.
The endpoint is `http://localhost:5000/noun_storage`, and expects a JSON body with the `"noun"` key and a value that is a dictionary containing the attributes (English form, classifier, Vietnamese form) of the noun.

For example:
```json
{"noun":{"english": "bird", "classifier": "con", "vietnamese": "chim"}}
```
A complete `curl` command looks like this.
```shell
curl -i -X POST "http://localhost:5000/noun_storage" -H "Content-Type: application/json" -d '{"noun":{"english": "bird", "classifier": "con", "vietnamese": "chim"}}'
```
