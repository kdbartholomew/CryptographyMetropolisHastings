# metropolis hasting algorithm for crypography

import numpy as np
import math
import pandas as pd
import random


# M is our 27x27 probability matrix that describes transitions between letters and spaces
# T is our 27!x27! matrix that describes the probability of all permutations of letters and spaces

# start with any coding function (f), they used identity to start
# coding function maps encoded text to decoded text
# coding functions that are closer to the cipher have a higher score

# initialize coding function to map encoded to encoded (no changes to original message)
#coding fucntion takes input message as input and uses a dic to generate swapped message:

class Cryptography:

    def __init__(self,input_message): # initializes coding function to input message
        self.input_message = input_message
        self.coding_function_initial = {char: char for char in input_message}
        #{char: char for char in input_message}: This is a dictionary comprehension that iterates over
        # each character (char) in the input_message. For each character, it creates a key-value pair
        # where both the key and the value are the same character. This effectively initializes the
        # dictionary with each character mapping to itself.


#should it take coding function as input?? acceptance returns it
    def coding_function(self): #coding fucntion takes input message as input and uses a dic to generate swapped message:
        #uses dictionary to generate swapped message
        proposed_coding_function = self.coding_function_initial.copy()
        # pick 2 letters uniformly at random
        letter_1, letter_2 = random.sample(self.input_message, 2) #ensures different letters ?
        # switch the values that the coding function assigns to these 2 letters
            # ie.) where i mapped to i and j mapped to j initially, now i maps to j and j maps to i
        temp = proposed_coding_function[letter_1]  # accesses the value associated with letter1 and stores to temp
        proposed_coding_function[letter_1] = proposed_coding_function[letter_2]
        proposed_coding_function[letter_2] = temp
        #call this new proposed coding function "proposed_coding_function"
        return proposed_coding_function

        # # check acceptance of the proposed coding function
        # if self.acceptance_function(self.coding_function, proposed_coding_function): #wrong
        #     # if accepted, update the internal coding function
        #     self.coding_function = proposed_coding_function
        # else:
        #     self.coding_function = self.coding_function
        #
        # return self.coding_function

#does self.coding_function reference the initial or the updated?
    def acceptance_function(self, coding_function, proposed_coding_function): #acceptance function takes coding function and outputs proposal function
        #score is calculated in here
        acceptance_ratio = self.score(proposed_coding_function) / self.score(coding_function)
        acceptance_min = min(1, acceptance_ratio)
        u = np.random.uniform(0, 1) #random number between 0, 1 uniformly dist
        if u < acceptance_min: #ratio or min?
            #accept proposal
            coding_function = proposed_coding_function
        else:
            #stay at this coding function
            coding_function = coding_function

        return coding_function # if proposal is accepted, we update coding funct with proposed chnage

#pass M as argument?
    def score(self, coding_function):
        score = 1
        M = pd.read_csv('matrix-spacefirst.csv')
        for i in range(len(input_message-1)):
            score = score * M[coding_function[i], coding_function[i+1]]
        return score



input_message = input("Enter the string you would like to decode: ")
crypto = Cryptography(input_message)

#running MH Algo
#for _ in range(10000): #error
    #decoded_message =
    #print("Decoded message:", decoded_message)

#test input message
#tahis si a trbuly oevly dnjugmle tesnrig to tset yuor mlaogrtip-eas naolghrtim











