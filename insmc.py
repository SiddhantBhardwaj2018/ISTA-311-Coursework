'''
Final Exam Submission - Siddhant Bhardwaj
'''

import random

def simulate_markov_chain(s):
    val = random.random()
    if s == 'P':
        if val <= 0.4:
            return 'S'
        else:
            return 'P'
    elif s == 'S':
        if val <= 0.1:
            return 'P'
        elif val <= 0.4:
            return 'E'
        else:
            return 'S'
    else:
        if val <=  0.2:
            return 'S'
        else:
            return 'E'

def main():
    lst = ['S']
    for i in range(1000):
        lst.append(simulate_markov_chain(lst[-1]))
    print('-----------------')
    print('Poor: ' + str(lst.count('P') / len(lst)))
    print('Satisfactory: ' + str(lst.count('S') / len(lst)))
    print('Excellent: ' + str(lst.count('E') / len(lst)))
    print('-----------------')
    
if __name__ == "__main__":
    main()