import os

en_file_list = list()
jp_file_list = list()
os.chdir(R"C:\Users\ipc39015\Desktop\FAtest\ArticleContentEnglish_copy")

for folder in os.listdir():
    en_path = "C:\\Users\\ipc39015\\Desktop\\FAtest\\ArticleContentEnglish_copy\\" + folder
    os.chdir(en_path)
    en_file_list = os.listdir()

    jp_path = "C:\\Users\\ipc39015\\Desktop\\FAtest\\ArticleContentJapanese_copy\\" + folder
    os.chdir(jp_path)
    jp_file_list = os.listdir()

    i = 0
    j = 0
    while (i < len(en_file_list)) and (j < len(jp_file_list)):
        print(en_file_list[i], "---", jp_file_list[j])
        if en_file_list[i] == jp_file_list[j]:
            i = i + 1
            j = j + 1
        else:
            os.chdir(en_path)
            os.remove(en_file_list[i])
            i = i + 1

    while j < len(en_file_list):
        os.chdir(en_path)
        os.remove(en_file_list[j])
        j = j + 1
