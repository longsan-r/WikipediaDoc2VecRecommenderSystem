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
dirPath = r"/Users/longsan/Desktop/doc2vecFAwiki/ArticleContentEnglish"
os.chdir(dirPath)
for folder in os.listdir():
    folderPath = os.path.join(dirPath, folder)
    os.chdir(folderPath)
    for fileName in os.listdir():
        filePath = os.path.join(folderPath, fileName)
        with io.open(r"C:\Users\HenzesburgBenz\Desktop\doc2vecFAwiki\articles.txt", "a", encoding="utf-8") as w:
            w.write(fileName)
            w.write("\n")
        try:
            print("tokenizing articles...")
            with io.open(file=filePath, mode="r", encoding="utf-8") as f:
                contents = f.read()
                text_tokens = tokenizer.tokenize(contents)
                tokens_without_sw = [
                    word for word in text_tokens if not word in stopwords.words()]
                tokens_without_sw = list(tokens_without_sw)
                corpus.append(tokens_without_sw)
        except Exception as e:
            print(e)
print("done, tokenizing articles!")

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(corpus)]

# models definition
# PV-DBOW
pv_dbow_model = Doc2Vec(dm=0, dbow_words=0, vector_size=200,
                        window=5, min_count=4, epochs=10, workers=cores)
# PV-DM w/average
pv_dm_model = Doc2Vec(dm=1, dm_mean=1, vector_size=200,
                      window=5, min_count=4, epochs=10, workers=cores)

pv_dbow_model.build_vocab(documents)
pv_dm_model.reset_from(pv_dbow_model)

print("Start training process...")

# training
pv_dbow_model.train(
    documents, total_examples=pv_dbow_model.corpus_count, epochs=pv_dbow_model.epochs)
pv_dm_model.train(
    documents, total_examples=pv_dm_model.corpus_count, epochs=pv_dm_model.epochs)

print("Finish training!")
# save the models for later use
pv_dbow_model.save(get_tmpfile("pv_dbow_model"))
pv_dm_model.save(get_tmpfile("pv_dm_model"))
