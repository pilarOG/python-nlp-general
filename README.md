# NLP general Python scripts

This is a collection of little scripts and functions I have been writing and using since ~2016 for the different NLP tasks I've had to do.
Probably all of them were thought and used to work only with Spanish.

# In this repo

1) child_orth_errors: generating text with orthographic errors similar to children mistakes

Children make orthographic errors that follow a different pattern from adult typos. Their errors follow patterns related to the stage at where they are in learning language.
This code performs a series of transformation by rules with random probabilities, applying those errors to some input text. The collection of errors was retrieved from different papers and analysis on the subject.
The original goal was to use this code to create data with errors and then train models to identify them and apply it to a QnA systems for children.

2) train_ngrams: code to train word level or character level n-grams

This code was used to build language models either at the word level or at the character level from a collection of text. 

3) phonetic_distance: score distance between two strings phonetically

This code was written to compare two strings and score their similarity in terms of phonetic similarity for Chilean Spanish. originally this code was written as part of a spell correction module.
The csv file contains a matrix of the distance score for the different phones in the language, which can be change according to necessity.

4) phonetic_transcription: simple phonetic transcriber for Chilean Spanish

Collection of replace rules to transcribe quickly a string in Chilean Spanish to a phone representation. 
