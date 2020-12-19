'''
Name: Siddhant Bhardwaj
Assignment: ISTA 311 Programming Assignment 1
Course: ISTA 311
Collaborators: Vibhor Mehta
'''

# Imports: we need numpy for np.log2()
import numpy as np

# Functions

def entropy(dist):
    return sum([i * np.log2(1/i) for i in dist.values()])

def expected_length(code, dist):
	return sum([len(code[i]) * dist[i] for i in dist.keys()])    

def cross_entropy(distp, distq):
    return sum([list(distp.values())[i] * np.log2(1/ list(distq.values())[i]) for i in range(len(distp))])

def kldiv(distp, distq):
    return sum([list(distp.values())[i] * (np.log2(1/list(distq.values())[i]) - np.log2(1/list(distp.values())[i])) for i in range(len(distp))])

def create_frequency_dict(string):
    freq = dict()
    for i in string:
    	if i not in freq:
    		freq[i] = string.count(i) / len(string)
    return freq

def invert_dict(code):
    return {val:key for (key,val) in code.items()}

def encode(message, code):
    string = ''
    for i in message:
    	string += code[i]
    return string

def decode(message, code):
	reverse_dict = invert_dict(code)
	string = ''
	print(reverse_dict)
	i = 0
	lst1 = list(set([len(i) for i in list(reverse_dict.keys())]))
	while i <= len(message) - 1:
		string1, i = helper(lst1, message, reverse_dict,i)
		string += string1
	return string

def helper(lst, message,dict1,i):
	strn = ''
	lst = lst[::-1]
	for num in lst:
		if message[i:i + num] in dict1.keys():
			strn = dict1[message[i:(i + num)]]
			i = i + num
			return strn, i


	
