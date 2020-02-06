import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'deepak maurya is a good boy. he is an engineering student')
print(doc)
for token in doc:
    print(token.text, token.pos_ , token.dep_)
for sentence in doc.sents:
    print(sentence)