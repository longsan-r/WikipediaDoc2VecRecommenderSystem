import wikipediaapi
import io
import os


wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)
os.chdir(r"C:\Users\ipc39015\Desktop\FAtest\Topic")
for fileName in os.listdir():
    path_fileName = fileName
    fileName = os.path.splitext(fileName)[0]
    print("\n", fileName)

    dir_path = f"C:\\Users\\ipc39015\\Desktop\\FAtest\\content\\{fileName}"
    os.mkdir(dir_path)
    with open(path_fileName, "r") as f:
        content = f.readlines()
        for article_name in content:
            try:
                article_name = article_name.strip('\n')
                print(article_name)

                p_wiki = wiki_wiki.page(article_name)
                p_wiki = p_wiki.langlinks['ja']
                f_path = f"{dir_path}\\{article_name}.txt"
                with io.open(f_path, "w", encoding="utf-8") as f:
                    f.write(p_wiki.text)
            except Exception as e:
                print(e)
                continue

print("done!")
