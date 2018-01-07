# To be able to run this you need to have installed the google-cloud-sdk and credentials

# --- This code was taken from Google Cloud tutorial, it's not mine ---

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import sys

if __name__=='__main__':
    # Instantiates a client
    language_client = language.LanguageServiceClient()

    # The text to analyze
    if len(sys.argv) == 1:
        raise Exception('Insert the text to analyze as an argument in the terminal')
    text = sys.argv[1]
    if type(text) != str and type(text) != unicode:
        raise Exception('Wrong input format')

    document = types.Document(
    language='es', # Change language here
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = language_client.analyze_sentiment(document)
    #print sentiment # See full output here

    print('Score: {}'.format(sentiment.document_sentiment.score))
    print('Magnitude: {}'.format(sentiment.document_sentiment.magnitude))
