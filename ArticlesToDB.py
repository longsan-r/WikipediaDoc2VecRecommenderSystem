import psycopg2
import wikipediaapi
import os

wiki_wiki = wikipediaapi.Wikipedia('en')


def create_tables(table_name):
    """ create tables in the PostgreSQL database"""
    sql = f"""
        CREATE TABLE {table_name} (
            article_id serial PRIMARY KEY,
            article_name TEXT,
            en_url TEXT,
            ja_url TEXT
        )
        """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            database="wikipedia_feature_articles", user="postgres", password="postgres")
        cur = conn.cursor()
        # create table
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_into_table(table_name, art_name, eng_url, jp_url):
    sql = f"""
        INSERT INTO {table_name} (article_name, en_url, ja_url)
        VALUES ('{art_name}', '{eng_url}', '{jp_url}')
        """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
            database="wikipedia_feature_articles", user="postgres", password="postgres")
        cur = conn.cursor()
        # create table
        cur.execute(sql)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


os.chdir("Topic")

listdir = os.listdir()

for fileName in listdir:
    fname = os.path.splitext(fileName)
    table_name = fname[0]
    create_tables(table_name)
    with open(fileName, 'r') as f:
        contents = f.readlines()
        for article in contents:
            article = article.split("\n")
            article = article[0]
            page_py = wiki_wiki.page(article)
            if page_py.exists():
                en_url = page_py.fullurl
                try:
                    langlink = page_py.langlinks
                    ja = langlink['ja']
                    ja_url = ja.fullurl
                except:
                    ja_url = "null"
                article = article.replace("'", "''")
                insert_into_table(table_name, article, en_url, ja_url)
