with open('C:\\Users\\ipc39015\\Desktop\\FAtest\\wiki_feature_articles.txt', 'r') as r:
    with open('C:\\Users\\ipc39015\\Desktop\\FAtest\\TopicList.txt', 'w') as w:
        content = r.readlines()
        for line in content:
            if line[0] == "=":
                line = line.strip("=")
                line = line.split("=")
                line = line[0].strip()
                w.write(line + '\n')

                print(line)
                fileName = 'C:\\Users\\ipc39015\\Desktop\\FAtest\\Topic\\'+line+".txt"
                print(fileName)
                f = open(fileName, 'w')
    
            elif line[:21] == "* {{FA/BeenOnMainPage":
                line = line.split("[[")
                line = line[1].split("]]")
                f.write(line[0]+'\n')

