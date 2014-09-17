
import nltk


tagdict = nltk.data.load('help/tagsets/upenn_tagset.pickle')
for tag in tagdict:
    print(tag)
token_temp = (nltk.word_tokenize("This is test demo for POS"))
tag_dict = {}
for tags in tagdict:
    tag_dict[tags] = 0
pos_tagged = nltk.pos_tag(token_temp)
for tag in pos_tagged:
    print(tag[1])
    #tag_dict[tag] = tag_dict[tag]+1