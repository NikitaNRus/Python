import requests
import io

word_list=[]
response = requests.get('https://github.com/LussRus/Rus_words/blob/master/UTF8/txt/nouns/summary.txt').text



word_list.append(response)
print(word_list)


#
#for i in range(len(ru)):
#    if len(ru[i])==5:
#        word_list.append(ru[i])

#print(len(word_list))
