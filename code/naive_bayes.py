from nltk import bigrams
import nltk
import os
import math



#5=pop, 38=indie, 95=rock, 138=electronic, 238=love, 1149=Classical

#courpus of each genre
unigram_pop = {}
unigram_indie = {}
unigram_rock = {}
unigram_electronic = {}
unigram_love = {}
unigram_class = {}


#main hash to save genre corpus and count
main_hash = {}
main_count = {}

def trainData():
    #read all files from a directory (training data)
    path = '/Users/sameergupta/PycharmProjects/NLP_final/my_feature_vector'
    file = open(path, 'r')
    while 1:
        line = file.readline()
        if not line:
            break
        tokenize = line.split()
        #print tokenize
        count = 0
        current_hash = {}
        genre_value = ''
        for token in tokenize:
            if(count == 0):
                genre_value = token
                current_hash = main_hash[token]
            else:
                current_hash[count] = int(token)
                main_count[genre_value] += int(token)
            count = count + 1
        '''for keys in current_hash:
            print("****")
            print(genre_value)
            print(keys)
            print(current_hash[keys])'''
            #print current_hash[1]

def calculateProbability(hash_val,token,count):
      smoothing = 2
      value = 0
      if(main_hash[hash_val].get(count) is not None and main_hash[hash_val].get(count) > 0 and int(token) > 0):
                '''print("####")
                print(main_hash[hash_val][count])
                print(token)
                print(main_count[hash_val])'''
                value = math.log((main_hash[hash_val][count])* (int(token))) - math.log((main_count[hash_val]))
      else:
                #print "smoothing"
                #print(main_count[hash_val])
                value = math.log(smoothing) - math.log((main_count[hash_val]))
      return value


def testDataOnClassifier():
    correct_pred = 0
    total_pred = 0
      #read all files from a directory (training data)
    path = '/Users/sameergupta/PycharmProjects/NLP_final/my_feature_vector'
    file = open(path, 'r')
    genre_value = 0

    while 1:
        final_probability = -99999999
        final_genre_index = 0

        line = file.readline()
        if not line:
            break
        tokenize = line.split()
        #print tokenize
        for hash_val in main_hash:
            doc_probability = 0

            #print( hash_val)
            count = 0
            for token in tokenize:
                if(count == 0):
                   genre_value = int(token)
                else:
                   '''print("******")
                   print(hash_val)
                   print(token)
                   print(count)'''
                   doc_probability = doc_probability + calculateProbability(hash_val,token,count)
                count = count + 1
            '''print("######")
            print(genre_value)
            print(doc_probability)
            print(hash_val)'''
            print(final_probability)
            print(doc_probability)
            if(float(final_probability) < float(doc_probability)):
                final_probability = doc_probability
                final_genre_index = int(hash_val)

            #print doc_probability
            #return (doc_probability)
            #print 10 ** doc_probability
            #print doc_probability
        print("####")
        print(final_genre_index)
        print(genre_value)
        print("$$$$")
        if(final_genre_index == genre_value):
            print("hello")
            correct_pred +=1
        total_pred +=1
    print(correct_pred)
    print(total_pred)
        #return 0

def main():
    main_hash['5'] = unigram_pop
    main_hash['38'] = unigram_indie
    main_hash['95'] = unigram_rock
    main_hash['138'] = unigram_electronic
    main_hash['238'] = unigram_love
    #main_hash['1149'] = unigram_class

    main_count['5'] = 1
    main_count['38'] = 1
    main_count['95'] = 1
    main_count['138'] = 1
    main_count['238'] = 1
    #main_count['1149'] = 1

    #train data
    trainData()
    #test data
    testDataOnClassifier()


main();