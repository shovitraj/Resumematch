import spacy
import json
from collections import Counter
import numpy as np

nlp = spacy.load('en_core_web_sm')

def sent_tokenization(text):
    text = ''.join(c for c in text if not c.isnumeric())
    text = ''.join([x.replace('●','') for x in text])
    text = ''.join([x.replace('•','') for x in text])
    text = ''.join([x.replace('_','') for x in text])
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    sentences = [x.replace('\n','') for x in sentences]
    sentences = [x.replace('\n\n','') for x in sentences]
    return sentences
