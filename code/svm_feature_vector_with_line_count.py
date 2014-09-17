
from nltk import bigrams
import nltk
import os
import math

unigram = {}
bigram = {}

final_unigram = {}
final_bigram = {}


total_count = 0
total_count_log = 0
total_bigram = 0
total_bigram_log = 0

#List to store words per document for each of the genres
word_per_line_alter = []
word_per_line_country=[]
word_per_line_electronic=[]
word_per_line_folk=[]
word_per_line_jazz=[]
word_per_line_metal=[]

num_line_alter = []
num_line_country=[]
num_line_electronic=[]
num_line_folk=[]
num_line_jazz=[]
num_line_metal=[]

# electronic, fork, metal, rock, pop, festival


def createCorpus():
    #read all files from a directory (training data)
    path = "../NLP_final/NLP/corpus"

    listing = os.listdir(path)

    tokens = []    #list to store all the tokens
    bigram_tokens = []; #for bigram tokens

    count=0

    for infile in listing:
        if infile != '.DS_Store':
            #Initialize two variables to maintain count of no. of lines and no. of words in each line
            num_words=0
            num_lines=0

            new_path = path +'/' + infile
            file = open(new_path, 'r')
            f = open(new_path,'r')
            token_temp = (nltk.word_tokenize(file.read()))
            tokens.extend(token_temp)
            bigram_tokens_temp = bigrams(token_temp)
            bigram_tokens.extend(bigram_tokens_temp)


    total_count = len(tokens)
    total_count_log = math.log(total_count)

    total_bigram = len(bigram_tokens)
    total_bigram_log = math.log(total_bigram)


    for token in tokens:
            if(unigram.get(token) is not None) :
                unigram[token] = unigram[token]+1
            else:
                unigram[token] = 1

    for bi_token in bigram_tokens:
            if(bigram.get(bi_token) is not None) :
                bigram[bi_token] = bigram[bi_token]+1
            else:
                bigram[bi_token] = 1


    return (total_count_log,total_bigram_log)
'''            #Calculate average number of words per line for each of the files
            for line in list(f):
                if (line == '\n' or line == ' '):
                    continue
                #print line
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1
                #print num_words


            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            if(count<240):
                word_per_line_alter.append(avg_words_per_line)
            elif(count<480):
                word_per_line_country.append(avg_words_per_line)
            elif(count<720):
                word_per_line_electronic.append(avg_words_per_line)
            elif(count<960):
                word_per_line_folk.append(avg_words_per_line)
            elif(count<1200):
                word_per_line_jazz.append(avg_words_per_line)
            else:
                word_per_line_metal.append(avg_words_per_line)

            print avg_words_per_line

            count += 1'''



def createFinalHash():
    for un in unigram:
        # unigram frequnecy required for feature vector
        if unigram[un] > 10:
            final_unigram[un] = unigram[un]
    for bi in bigram:
        # bigram frequnecy required for feature vector
        if bigram[bi] > 5:
            final_bigram[bi] = bigram[bi]




def writeFeatureVector():
     #read all files from a directory (training data)
    '''path = "../NLP_final/NLP/alternative"
    path_m = "../NLP_final/NLP/metal"
    path_f =  "../NLP_final/NLP/folk"
    path_c =  "../NLP_final/NLP/country"
    path_e =  "../NLP_final/NLP/electronic"
    path_j =  "../NLP_final/NLP/jazz"'''

    path = "../NLP_final/NLP_train/alternative/alternative"
    path_m = "../NLP_final/NLP_train/metal/metal"
    path_f =  "../NLP_final/NLP_train/folk/folk"
    path_c =  "../NLP_final/NLP_train/country/country"
    path_e =  "../NLP_final/NLP_train/electronic/electronic"
    path_j =  "../NLP_final/NLP_train/jazz/jazz"


    f = open('../NLP_final/fv_uni_svm_train_line_count_words_pos','w')

    #available POS tags
    tagdict = nltk.data.load('help/tagsets/upenn_tagset.pickle')
    #for tag in tagdict:
        #print(tag)


    #alternate
    listing = os.listdir(path)
    # Initialize a variable to maintain the count of the document being read
    count_alter=0
    for infile in listing:
        if infile != '.DS_Store':

            new_path = path +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))

            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("1 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
                if(tag_dict[t] > 0):
                    f.write(str(count)+":"+str(tag_dict[t]))
                    f.write(str(" "))
                    count = count+1'''

            f.write(str(count)+":"+str(num_line_alter[count_alter]))
            count_alter += 1

            f.write("\n")

    #folk
    listing = os.listdir(path_f)
    count_folk=0
    for infile in listing:
        if infile != '.DS_Store':

            new_path = path_f +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            #unigram_tokens_temp = unigram(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens


            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''


            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("2 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
             if(tag_dict[t] > 0):
                f.write(str(count)+":"+str(tag_dict[t]))
                f.write(str(" "))
                count = count+1'''

            f.write(str(count)+":"+str(num_line_folk[count_folk]))
            count_folk += 1
            f.write("\n")

    #metal
    listing = os.listdir(path_m)
    count_metal=0
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_m +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            #unigram_tokens_temp = unigram(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens


            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("3 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
              if(tag_dict[t] > 0):
                f.write(str(count)+":"+str(tag_dict[t]))
                f.write(str(" "))
                count = count+1'''

            f.write(str(count)+":"+str(num_line_metal[count_metal]))
            count_metal += 1
            f.write("\n")


   #country
    listing = os.listdir(path_c)
    count_country=0
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_c +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            #unigram_tokens_temp = unigram(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens


            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("4 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
             if(tag_dict[t] > 0):
                f.write(str(count)+":"+str(tag_dict[t]))
                f.write(str(" "))
                count = count+1'''

            f.write(str(count)+":"+str(num_line_country[count_country]))
            count_country += 1
            f.write("\n")

   #electronic
    listing = os.listdir(path_e)
    count_electronic=0
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_e +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            #unigram_tokens_temp = unigram(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens


            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("5 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
             if(tag_dict[t] > 0):
                f.write(str(count)+":"+str(tag_dict[t]))
                f.write(str(" "))
                count = count+1'''


            f.write(str(count)+":"+str(num_line_electronic[count_electronic]))
            count_electronic += 1
            f.write("\n")

   #jazz
    listing = os.listdir(path_j)
    count_jazz = 0
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_j +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            #unigram_tokens_temp = unigram(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens


            #POS tag code
            '''tag_dict = {}
            for tags in tagdict:
                tag_dict[str(tags)] = 0
            pos_tagged = nltk.pos_tag(token_temp)
            for tag in pos_tagged:
                if(tag_dict.has_key(str(tag[1]))):
                    tag_dict[str(tag[1])] = tag_dict[str(tag[1])]+1'''

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            f.write("6 ")
            count = 1
            for tkn in final_unigram:
                if unigram_dict.get(tkn) is not None:
                    f.write(str(count)+":"+str(unigram_dict[tkn]))
                #else:
                    #f.write(str(count),":0")
                    f.write(str(" "))
                count = count+1

            '''for t in tag_dict:
             if(tag_dict[t] > 0):
                f.write(str(count)+":"+str(tag_dict[t]))
                f.write(str(" "))
                count = count+1'''


            f.write(str(count)+":"+str(num_line_jazz[count_jazz]))
            count_jazz += 1
            f.write("\n")



def createWordCount():
    print "hii"
    #read all files from a directory (training data)
    path_a = "../NLP_final/NLP_train/alternative/alternative"
    path_m = "../NLP_final/NLP_train/metal/metal"
    path_f =  "../NLP_final/NLP_train/folk/folk"
    path_c =  "../NLP_final/NLP_train/country/country"
    path_e =  "../NLP_final/NLP_train/electronic/electronic"
    path_j =  "../NLP_final/NLP_train/jazz/jazz"



    '''path_a = "../NLP_final/NLP/alternative"
    path_m = "../NLP_final/NLP/metal"
    path_f =  "../NLP_final/NLP/folk"
    path_c =  "../NLP_final/NLP/country"
    path_e =  "../NLP_final/NLP/electronic"
    path_j =  "../NLP_final/NLP/jazz"'''


#alternate
    listing = os.listdir(path_a)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_a +'/' + infile
            file = open(new_path, 'r')

            for line in list(file):
                if (line == '\n' or line == ' '):
                    continue
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1

            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            word_per_line_alter.append(avg_words_per_line)
            num_line_alter.append(num_lines)

#folk
    listing = os.listdir(path_f)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_f +'/' + infile
            file = open(new_path, 'r')

            for line in list(file):
                if (line == '\n' or line == ' '):
                    continue
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1

            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            word_per_line_folk.append(avg_words_per_line)
            num_line_folk.append(num_lines)


#metal
    listing = os.listdir(path_m)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_m +'/' + infile
            file = open(new_path, 'r')

            for line in list(file):
                if (line == '\n' or line == ' '):
                    continue
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1

            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            word_per_line_metal.append(avg_words_per_line)
            num_line_metal.append(num_lines)


#country
    listing = os.listdir(path_c)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_c +'/' + infile
            file = open(new_path, 'r')

            for line in list(file):
                if (line == '\n' or line == ' '):
                    continue
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1

            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            word_per_line_country.append(avg_words_per_line)
            num_line_country.append(num_lines)


#electronic
    listing = os.listdir(path_e)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_e +'/' + infile
            file = open(new_path, 'r')

            for line in list(file):
                if (line == '\n' or line == ' '):
                    continue
                words = line.split(' ')
                num_words += len(words)
                num_lines += 1

            avg_words_per_line = ((num_words)/(num_lines))

            #Append the respective genre array with avg_words_per_line value
            word_per_line_electronic.append(avg_words_per_line)
            num_line_electronic.append(num_lines)

#jazz
    listing = os.listdir(path_j)

    for infile in listing:
        if infile != '.DS_Store':
            num_words=0
            num_lines=0

            new_path = path_j +'/' + infile
            file = open(new_path, 'r')

        for line in list(file):
            if (line == '\n' or line == ' '):
                continue
            words = line.split(' ')
            num_words += len(words)
            num_lines += 1

        avg_words_per_line = ((num_words)/(num_lines))

        #Append the respective genre array with avg_words_per_line value
        word_per_line_jazz.append(avg_words_per_line)
        num_line_jazz.append(num_lines)



def main():
    createCorpus()
    createFinalHash()
    createWordCount()
    writeFeatureVector()

main()