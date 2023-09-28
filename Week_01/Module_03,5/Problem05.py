#-----------------------------------------------------------------------------------------------------------------------
# Q. Reverse Words
# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q
#-----------------------------------------------------------------------------------------------------------------------
#Taking full sentence directly as a string and saved in a variable.
sentence = list(map(str, input().split()))

#Extracting each word of the sentence, reversing it, and then printing it.
reversed_sentence_list = []
for word in sentence:
    reversed_sentence_list.append(word[::-1])

#Now we'll take all words from the list and will join them using 'space'. To avoid the tailing space.
reversed_sentence = ' '.join(reversed_sentence_list)

#Printing the final modified sentence.
print(reversed_sentence)
