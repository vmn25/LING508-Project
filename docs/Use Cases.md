# Use Cases
For this project, only Use Case #2 has been implemented.

## 1. Part of Speech
The app takes a sentence in Vietnamese as input and returns the part of speech for each word.

Example:
Input = Tôi ăn cá.
Output = (Tôi, Noun), (ăn, Verb), (cá, Noun).

## 2. Noun Classifier
The app takes a noun in English as input and returns the input, the Vietnamese translation, and the appropriate classifier if applicable.

Example:
Input = dog
Output = English: dog, classifier: con, Vietnamese: chó

## 3. Parse a Pronoun
The app takes a pronoun in Vietnamese as input and returns information on gender, person, number, and context.

Example:
Input = minh
Output = unisex, first-person, singular, familiar

Input = tôi
Output = unisex, first-person, singular, formal
