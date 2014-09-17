from nltk import bigrams
import nltk
import os
import math

unigram_pos = {}
bigram_pos = {}
unigram_neg = {}
bigram_neg = {}
total_count = 0
total_count_log = 0
total_bigram = 0
total_bigram_log = 0


def trainData(isPositiveClassifier):
    #read all files from a directory (training data)
    if isPositiveClassifier:
         path = '../language_model/data/data_pos'
    else:
         path = '../language_model/data/data_neg'

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
        if isPositiveClassifier:
            if(unigram_pos.get(token) is not None) :
                unigram_pos[token] = unigram_pos[token]+1
            else:
                unigram_pos[token] = 1
        else:
            if(unigram_neg.get(token) is not None) :
                unigram_neg[token] = unigram_neg[token]+1
            else:
                unigram_neg[token] = 1

    for bi_token in bigram_tokens:
        if isPositiveClassifier:
            if(bigram_pos.get(bi_token) is not None) :
                bigram_pos[bi_token] = bigram_pos[bi_token]+1
            else:
                bigram_pos[bi_token] = 1
        else:
            if(bigram_neg.get(bi_token) is not None) :
                bigram_neg[bi_token] = bigram_neg[bi_token]+1
            else:
                bigram_neg[bi_token] = 1

    return (total_count_log,total_bigram_log)

def calculateProbability(token ,isUnigram,isPostiveDataSet,total_c):
        smoothing = 1
        if isUnigram:
          if isPostiveDataSet:
            if(unigram_pos.get(token) is not None):
                value = (math.log(unigram_pos[token]) - total_c)
            else:
                #print "smoothing"
                value = (math.log(smoothing) - total_c)
            #print unigram_pos[token]
            #print total_c
            #print value
            return value
          else:
            if(unigram_neg.get(token) is not None):
                value = (math.log(unigram_neg[token]) - total_c)
            else:
                #print "smoothing"
                value = (math.log(smoothing) - total_c)
            #print unigram_neg[token]
            #print total_c
            #print value
            return value
        else:
          if isPostiveDataSet:
            if(bigram_pos.get(token) is not None):
                value = (math.log(bigram_pos[token]) - total_c)
            else:
                #print "bi gram smoothing"
                value = (math.log(smoothing) - total_c)
            return value
          else:
            if(bigram_neg.get(token) is not None):
                value = (math.log(bigram_neg[token]) - total_c)
            else:
                #print "bi gram smoothing"
                value = (math.log(smoothing) - total_c)
            return value

def testDataOnClassifier(isUnigram,isPositiveDataSet,total_count,new_path):
    doc_probability = 0

    file = open(new_path, 'r')
    token_temp = (nltk.word_tokenize(file.read()))
    tokens = token_temp
    #print tokens
    if isUnigram:
        for token in tokens:
            doc_probability = doc_probability + calculateProbability(token,True,isPositiveDataSet,total_count)
        #print doc_probability
        return (doc_probability,len(tokens))
        #print 10 ** doc_probability
    else:
        bigram_token = bigrams(tokens)
        for bigram in bigram_token:
            doc_probability = doc_probability + calculateProbability(bigram,False,isPositiveDataSet,total_count)
        #print doc_probability
        return (doc_probability,len(bigram_token))

        #return 0

def main():
   total_count_pos,total_bigram_log_pos = trainData(True)
   total_count_neg,total_bigram_log_neg = trainData(False)
   isPos = True
   total_docs = 0
   r_prediction_docs = 0
   r_prediction_bdocs = 0
   for i in range(0,2):
       if i%2:
         path = '../language_model/data/data_test_pos'
         isPos = True
       else:
         path = '../language_model/data/data_test_neg'
         isPos = False

       listing = os.listdir(path)
       tokens = []    #list to store all the tokens
       for infile in listing:
             if infile != '.DS_Store':
                new_path_ = path +'/' + infile

                #for unigram

                #positive data set
                positive_prob_u,t_size = testDataOnClassifier(True,True,total_count_pos,new_path_)
                #negative dataset
                negative_prob_u,t_size = testDataOnClassifier(True,False,total_count_neg,new_path_)

                #for bigram

                #positive dataset
                #print '********************'
                #print total_bigram_log_pos
                #print total_bigram_log_neg
                positive_prob_b,bt_size = testDataOnClassifier(False,True,total_bigram_log_pos,new_path_)
                #print positive_prob_b
                #negative dataset
                negative_prob_b,bt_size = testDataOnClassifier(False,False,total_bigram_log_neg,new_path_)
                #print negative_prob_b
                if(positive_prob_u > negative_prob_u):
                    #print "Positive Document"
                    if(isPos):
                        r_prediction_docs = r_prediction_docs + 1
                else:
                    #print "Negative Document"
                    if(isPos == False):
                        r_prediction_docs = r_prediction_docs + 1

                if(positive_prob_b > negative_prob_b):
                    #print "Positive B Document"
                    #print isPos
                    if(isPos):
                        r_prediction_bdocs = r_prediction_bdocs + 1
                else:
                    #print "Negative B Document"
                    #print isPos
                    if(isPos == False):
                        r_prediction_bdocs = r_prediction_bdocs + 1
                total_docs = total_docs + 1
   print "Document Predicted Accurately Using Unigram"
   print r_prediction_docs
   print "Document Predicted Accurately Using Bigram"
   print r_prediction_bdocs
   print "Total Documents"
   print total_docs
   final_probability = (r_prediction_docs*100)/total_docs
   #print "Unigram"
   #print final_probability
   n = t_size
   perplexity = (float(1)/final_probability)
   #print perplexity
   unigram_root = perplexity**(1.0/n)
   #print unigram_root
   final_b_probability = (r_prediction_bdocs*100)/total_docs
   #print "Bigram"
   n = bt_size
   #print final_b_probability
   b_perplexity = (float(1)/final_b_probability)
   bigram_root = b_perplexity**(1.0/n)
   #print bigram_root
main();