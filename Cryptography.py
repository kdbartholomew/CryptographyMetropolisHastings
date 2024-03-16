# metropolis hasting algorithm for crypography

import numpy as np
import math
import pandas as pd
import random

class Cryptography:
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    # initializes coding function so that every letter of the alphabet maps to itself
    def __init__(self,input_message, alphabet):
        self.input_message = input_message
        self.coding_function_initial = {char: char for char in alphabet}
        self.proposed_coding_function = self.coding_function_initial.copy()
# notes:
        # {char: char for char in input_message}: This is a dictionary comprehension that iterates over
        # each character (char) in the alphabet. For each character, it creates a key-value pair
        # where both the key and the value are the same character. This effectively initializes the
        # dictionary with each character mapping to itself.

# randomly picks 2 letters in the alphabet and proposes a swap of the values that the coding function assigns
    # updates proposed coding function... see acceptance method for if coding function gets overwritten by proposed if accepted
    def coding_function(self):
        letter_1, letter_2 = random.sample(self.alphabet, 2)  #random.sample ensure distinct elements
        temp = self.proposed_coding_function[letter_2] # temp gets the value that letter 2 maps to
        self.proposed_coding_function[letter_2] = letter_1
        self.proposed_coding_function[letter_1] = temp
        #print(self.proposed_coding_function) #its updating correctly!!
        #print("in coding function") #works
        print("in coding function, heres proposed: ", self.proposed_coding_function)
        return self.proposed_coding_function

    # acceptance function takes coding function and outputs updated coding function
    def acceptance_function(self, coding_function, proposed_coding_function):
        acceptance_ratio = self.score(proposed_coding_function) / self.score(coding_function)
        acceptance_min = min(1, acceptance_ratio)
        u = np.random.uniform(0, 1) #random number between 0, 1 uniformly dist
        if u < acceptance_min: #ratio or min?
            #accept proposal
            coding_function = proposed_coding_function #...perhaps a pass my reference error?
        else:
            #stay at this coding function
            coding_function = coding_function
        print("in acceptance function: ", coding_function) #doesnt work
        return coding_function # if proposal is accepted, we update coding funct with proposed change

# score function takes some coding function and calculates the score
    def score(self, coding_function):
        score = 1
        M = pd.read_csv('/Users/catalinabartholomew/Desktop/matrix-spacefirst.csv', header=None)
        M_copy = M.copy()
        # Rename the index and columns to integers from 0 to 26
        M_copy.index = range(27)
        M_copy.columns = range(27)
        decoded = self.get_decoded_message(coding_function)  # decoded stores decoded message string
# take decoded message, iterate over each char and convert to M loc, stored in map
        map = []
        for char in decoded: # for loop generates map which contains location in M (digit 0 for space - 26 for z)
            # space maps to 0
            if ord(char) == 32: # if char is space
                mapped_value = 0
                map.append(mapped_value)
            if (ord(char)>= 97 and ord(char)<=122): # if char is a letter
                # a maps to 1...z maps to 26
                mapped_value = ord(char) - 96 # mapped value now gives number in m
                map.append(mapped_value) # at the end of for loop map should contain the message in terms of m locations( int)
# converting to M entry
        #map contains the M location of letters in the decoded message based on the current coding function...
        for i in range(len(map)-1): # for loop generates score, iterates over map... map should be the same length as decoded message and input message
            #M_entry = M_copy[map[i],map[i+1]]
            M_entry = M_copy.iloc[map[i], map[i + 1]]
            score = score * M_entry # computes score
        print("map: ", map) #is map of current and proposed always the same?
        return score

    def get_decoded_message(self,coding_function): # can be used to decode any dictionary
        decoded_message = ''
        for char in self.input_message:
            # look up char (key) in coding function
            # get value associated with the key in the coding function (the mapped value aka decoded char)
            value = coding_function[char] # is this the final coding function?
           # print("value: ", value)
            decoded_message += value
            #decoded_message.append(value)
        return decoded_message

input_message = str.lower(input("Enter the string you would like to decode: ")) #only considers lower case letters
alphabet = " abcdefghijklmnopqrstuvwxyz"
crypto = Cryptography(input_message, alphabet) # calls constructor and initializes a coding function
string_decoded = ''
#1st iter

#what i want: my constructor creates an initial and a copy of it called proposed. on the first iteration
# proposed is sent to the coding function method and is updated, that proposed and the initial conding function are
# then sent to acceptance and the new coding function is returned

#coding function method is then called on a copy of this new coding function that was returned
# by acceptance (dont know if this is actually what happens)

#i think that if i fix my main (below) my code will work the way i want it to...
    # this is the logic i think i want but im runninng into issues with how to access objects created by my constructor...
#  the below code has issues with the way im using crypto.proposed_coding_function.coding_method()
        #i get that i cant call a method on a disctionary, it needs to be on an instance of the class but
#  crypto (instance of class) contains 2 things (coding function initial and proposed coding function) that need to be treated differently
# i think that when i use crypto.coding function i send both? idk dawg... when i use crypto directly the dictionaries coding function and proposed become the same
# i need help editing main so that the dictionaries coding function and proposed are not identical and deterministic
coding_function_initial = crypto.coding_function_initial
proposed_coding_function = crypto.proposed_coding_function.coding_function()
current_coding_function = crypto.acceptance_function(crypto.coding_function_initial, crypto.proposed_coding_function)
for l in range(1000):
    # Update the current coding function based on acceptance
    proposed_coding_function = crypto.proposed_coding_function.coding_function()
    current_coding_function = crypto.acceptance_function(current_coding_function, proposed_coding_function)


    #identical and non unique values ie.) qrs all map to e
    print("MAIN proposed_coding_function: ", crypto.proposed_coding_function)
    print("MAIN current_coding_functionn: ", current_coding_function)


    decoded_message = crypto.get_decoded_message(crypto.coding_function())
    print("Decoded message:", decoded_message)
# M = pd.read_csv('/Users/catalinabartholomew/Desktop/matrix-spacefirst.csv', header=None)
# M_copy = M.copy()
#
# # Rename the index and columns to integers from 0 to 26
# M_copy.index = range(27)
# M_copy.columns = range(27)
# print("m shape:", M.shape)
# print("m copy shape:", M_copy.shape)
# print("Row Index Names:", M_copy.index)
# print("Column Index Names:", M_copy.columns)

#error in cols and rows of M... rows are indexed  1-27 and cols A- AA (google sheets)
    # different in desktop .. that hoe has no headers?

#test input message
#ibqqz cjsuiebz #happy birthday but every letter is 1 over
#tahis si a trbuly oevly dnjugmle tesnrig to tset yuor mlaogrtip-eas naolghrtim
#ahicainqcaqx ic zqcqwbl bwq zwqbj xjustlicz tlhamx ic jyq kbr ho jybj albxx ho

#HOMEWORK:
# get a working algo,,,
# maybe redo in java!!!


#doesnt work:(


