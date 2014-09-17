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

# electronic, fork, metal, rock, pop, festival


def createCorpus():
    #read all files from a directory (training data)
    path = "../NLP_final/NLP/corpus"

    listing = os.listdir(path)
    tokens = []    #list to store all the tokens
    bigram_tokens = []; #for bigram tokens

    for infile in listing:
        if infile != '.DS_Store':
            new_path = path +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            tokens.extend(token_temp)
            bigram_tokens_temp = bigrams(token_temp)
            bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

    total_count = len(tokens)
    total_count_log = math.log(total_count)

    total_bigram = len(bigram_tokens)
    total_bigram_log = math.log(total_bigram)

    #print "Total Count"
    #print total_count
    #print total_count_log

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


def createFinalHash():
    for un in unigram:
        # unigram frequnecy required for feature vector
        if unigram[un] > 0:
            final_unigram[un] = unigram[un]
    for bi in bigram:
        # bigram frequnecy required for feature vector
        if bigram[bi] > 5:
            final_bigram[bi] = bigram[bi]

def writeFeatureVector():
     #read all files from a directory (training data)
    path = "../NLP_final/NLP_train/alternative/alternative"
    path_m = "../NLP_final/NLP_train/metal/metal"
    path_f =  "../NLP_final/NLP_train/folk/folk"
    path_c =  "../NLP_final/NLP_train/country/country"
    path_e =  "../NLP_final/NLP_train/electronic/electronic"
    path_j =  "../NLP_final/NLP_train/jazz/jazz"

    f = open('../NLP_final/fv_naive_bigram_train','w')

   #alternate
    listing = os.listdir(path)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("A ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n\n")

    #folk
    listing = os.listdir(path_f)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_f +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("B ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n\n")

    #metal
    listing = os.listdir(path_m)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_m +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("C ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n")
   #country
    listing = os.listdir(path_c)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_c +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("D ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n\n")

   #electronic
    listing = os.listdir(path_e)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_e +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("E ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n\n")

   #jazz
    listing = os.listdir(path_j)
    for infile in listing:
        if infile != '.DS_Store':
            #tokens = []    #list to store all the tokens
            #bigram_tokens = []; #for bigram tokens

            new_path = path_j +'/' + infile
            file = open(new_path, 'r')
            token_temp = (nltk.word_tokenize(file.read()))
            #tokens.extend(token_temp)

            bigram_tokens_temp = bigrams(token_temp)

            #bigram_tokens.extend(bigram_tokens_temp)
            #print tokens

            unigram_dict = {}
            bigram_dict = {}

            for token in token_temp:
                if(unigram_dict.get(token) is not None):
                     unigram_dict[token] = unigram_dict[token]+1
                else:
                     unigram_dict[token] = 1

            for bi_token in bigram_tokens_temp:
                  if(bigram_dict.get(bi_token) is not None):
                     bigram_dict[bi_token] = bigram_dict[bi_token]+1
                  else:
                    bigram_dict[bi_token] = 1
            f.write("F ")
            for tkn in final_bigram:
                if bigram_dict.get(tkn) is not None:
                    f.write(str(bigram_dict[tkn]))
                else:
                    f.write("0")
                f.write(str(" "))
            f.write("\n\n")

def main():
    createCorpus()
    createFinalHash()
    writeFeatureVector()

main()