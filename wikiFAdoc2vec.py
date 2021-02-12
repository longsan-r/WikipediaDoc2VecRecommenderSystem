import logging
import multiprocessing
import io
import os
from nltk.corpus import stopwords
from nltk import RegexpTokenizer
from gensim.test.utils import get_tmpfile
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

cores = multiprocessing.cpu_count()
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
tokenizer = RegexpTokenizer(r"\w+")  # remove punctuation marks

corpus = []
# iterate over and tokenize all articles
dirPath = "/Users/longsan/Desktop/doc2vecFAwiki/ArticleContentEnglish"
os.chdir(dirPath)
for folder in os.listdir():
    folderPath = os.path.join(dirPath, folder)
    os.chdir(folderPath)
    for fileName in os.listdir():
        filePath = os.path.join(folderPath, fileName)
        try:
            print("tokenizing articles...")
            with io.open(file=filePath, mode="r", encoding="utf-8") as f:
                contents = f.read()
                text_tokens = tokenizer.tokenize(contents)
                tokens_without_sw = [
                    word for word in text_tokens if not word in stopwords.words()]
                corpus.append(tokens_without_sw)
        except Exception as e:
            print(e)
print("done, tokenizing articles!")

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(corpus)]

# models definition
# PV-DBOW
pv_dbow_model = Doc2Vec(documents, dm=0, dbow_words=0, size=200, window=8,
                        min_count=19, workers=cores),
# PV-DM w/average
pv_dm_model = Doc2Vec(documents, dm=1, dm_mean=1, size=200, window=8,
                      min_count=19, workers=cores),

# training
pv_dbow_model.train(
    documents, total_examples=pv_dbow_model.corpus_count, epochs=pv_dbow_model.epochs)
pv_dm_model.train(
    documents, total_examples=pv_dbow_model.corpus_count, epochs=pv_dbow_model.epochs)

# save the models for later use
pv_dbow_model.save(get_tmpfile("pv_dbow_model"))
pv_dm_model.save(get_tmpfile("pv_dm_model"))
