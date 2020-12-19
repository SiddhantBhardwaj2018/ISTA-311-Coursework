'''
Name - Siddhant Bhardwaj

Collaborator - Vibhor Mehta
'''

import random

class Distribution(object):
    '''
        Initializes the distribution.
        After initialization, the instance has a single instance variable d (a dictionary), which represents a probability distribution.
        The keys of the dictionary are the outcomes; the values are the probabilities. Keys may have any (immutable) type, but values should always be floats.

        The dictionary is constructed:
        1. if dist is a dict, it becomes the dictionary
        2. if dist is any other object, we attempt to iterate through, assuming equal probabilities. This allows passing a single list, range, etc.
    '''


    def __init__(self, dist):
        '''
        Initializes the distribution. The only task is to initialize the dictionary.
        Parameters:
        dist: either a dict or an iterable (e.g. list).
        1. if dist is a dict, we use this dictionary directly.
        2. if dist is any other object, we attempt to iterate through and use the elements of the sequence as keys (outcomes). We assign equal probability 1/n to each outcome.
        '''

        if isinstance(dist, dict):
            self.dist = dist
        else:
            self.dist = {}
            n = len(dist)
            for elem in dist:
                self.dist.setdefault(elem, 1/n)
        return None

    def prob(self, set1):
    	val = 0
    	for i in set1:
    		val += self.dist[i]
    	return val

    def normalize(self):
    	denom  = sum(list(self.dist.values()))
    	for i in self.dist:
    		self.dist[i] = self.dist[i] / denom

    def condition(self, set2):
    	self.normalize()
    	for i in list(self.dist.keys()):
    		if i not in set2:
    			del self.dist[i]
    	denom2 = sum(list(self.dist.values()))
    	for i in self.dist.keys():
    		self.dist[i] = self.dist[i] / denom2

    def sample(self):
    	cutoff = 0
    	pred = random.random()
    	for i in self.dist.keys():
    		cutoff += self.dist[i]
    		if pred < cutoff:
    			return i
