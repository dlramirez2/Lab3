#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 08:53:43 2018

@author: Diana Ramirez 88604827
Professor: Diego Aguire
Class: CS 2302 TR 1:30PM
Lab 3B
"""
from NodeAVL import Node,AVLTree
from RedBlackTree import RedBlackTree
#########################################################################################
def print_anagrams(word, prefix=""): 
 
    if len(word) <= 1:
        str = prefix + word
        if engish_words.search(str) == str:##str in engish_words: 
            print(prefix + word)
            
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated. 
                print_anagrams(before + after, prefix + cur)
               
###########################################################################################
def count_anagrams(counterL,treename,word,prefix=""):
    if len(word) <= 1:
        str = prefix + word
        if treename.search(str) == str : ##str in engish_words: 
            counterL +=1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.   
                counterL = count_anagrams(counterL,treename,before + after, prefix + cur) 
    return counterL                 
##########################################################################################
def greatest_anagrams(file,tree_type):
    counterL = -1
    max_anagrams = -1
    max_word = ''
    ##reading the file and creating a list
    fileT = open(file)
    list_w = fileT.readlines()
    
    for i in range(len(list_w)):
        list_w[i] = list_w[i][:-1]
    if tree_type == 'AVL':
        new_tree = AVLTree()
        for ln in list_w:
            words = Node(ln)
            new_tree.insert(words) 
    if tree_type  == 'RBT':
        new_tree = RedBlackTree()
        for ln in list_w:
            new_tree.insert(ln)
            
    for word in list_w:
        counterL = count_anagrams(0,new_tree,word)
        if(counterL > max_anagrams):
            max_anagrams = counterL
            max_word = word

    print('The word with the most anagrams is',max_word,'it has',max_anagrams,'anagrams')      
###########################################################################################
    
##first I saved all the lines in the file in a list
g= open("words.txt")
word_list = g.readlines()

tree_type = input('what type of tree do you want to use?, AVL or RBT ')
##based on the input of the user I created a an AVL or RBT called engish_words
if tree_type == 'AVL':
    engish_words = AVLTree()
    for ln in word_list:
        ln = ln.replace('\n','')
        words = Node(ln)
        engish_words.insert(words)
    ##print(engish_words)
    
if tree_type  == 'RBT':
    engish_words = RedBlackTree()
    for ln in word_list:
        ln = ln.replace('\n','')
        engish_words.insert(ln)
    ##print( 'tree has height ' + str(engish_words.get_height()))
word = input("Write word to generate anagrams ")
print_anagrams(word)
count = count_anagrams(0,engish_words,word)
print("Number of anagrams",count)
##checks for the last word with the greatest number of anagrams
greatest_anagrams('words.txt',tree_type)

        