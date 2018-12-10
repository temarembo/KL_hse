import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
download_stopwords = stopwords.words('russian')
text = '''
Ходят по земле с инструментами, маленькими метелочками и кисточками люди и отыскивают места обитания
удивительных животных динозавров, живших миллионы лет назад. Никто никогда их не видел, но в горных породах сохранились их кости.
Ученые-палеонтологи раскапывают, промывают и восстанавливают скелет, а потом воссоздают внешний вид динозавра.
Это долгая и скрупулезная работа, ведь за миллионы лет кости стали хрупкими.
'''
stop_text = []
tokens = word_tokenize(text)
for i in tokens:
	if i not in download_stopwords:
		stop_text.append(i)
from nltk.stem import PorterStemmer

stemsPorter = []
porter = PorterStemmer()
for w in tokens:
    a = w
    w = porter.stem(w)
    if w != "":
        stemsPorter.append(w)
print