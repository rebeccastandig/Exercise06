#open a file named on the command line = done
#read the file = done
#split based on " " = done
#get rid of punctuation= done
#lowercase everything= done
#count each word = done
#print the counts = done
#sort from highest frequency to lowest frequency
#sort words with same frequency alphabetically

from sys import argv
script, first = argv

def make_dict():
    f = open(first)
    filetext = f.read()
    f.close()

    filetext = filetext.split()
    dict_words = {}

    for word in filetext:
        word = word.strip(",.!?-")
        word = word.lower()

        if word not in dict_words:
            dict_words[word] = 1
        elif word in dict_words:
            dict_words[word] += 1
        else:
            return False

    return dict_words

   # for word, count in dict_words.iteritems():
    #    print word, count
    
        # alphabetized_keys = sorted(dict_words.iteritems())
        # print alphabetized_keys

def frequency_list():
    dict_words = make_dict()
    keys = dict_words.keys()
    values = dict_words.values()

    maxval = 0
    ordered_list = []

    while len(keys) > 0:

        for value in values:
            if value > maxval:
                maxval = value
                
        index = values.index(maxval)
        ordered_list.append([keys[index], maxval])
        del values[index]
        del keys[index]
        maxval  = 0

    return ordered_list


def listing_data():
    ordered_list = frequency_list()
    sep_alpha_list_4 = []
    sep_alpha_list_3 = []
    sep_alpha_list_2 = []
    sep_alpha_list_1 = []
    for item in ordered_list:
        if item[1] == 4:
            sep_alpha_list_4.append(item)
            list_4 = sorted(sep_alpha_list_4)

    for item in ordered_list:
        if item[1] == 3:
            sep_alpha_list_3.append(item)
            list_3 = sorted(sep_alpha_list_3)

    for item in ordered_list:
        if item[1] == 2:
            sep_alpha_list_2.append(item)
            list_2 = sorted(sep_alpha_list_2)

    for item in ordered_list:
        if item[1] == 1:
            sep_alpha_list_1.append(item)
            list_1 = sorted(sep_alpha_list_1)



    print list_4, list_3, list_2, list_1

listing_data()
