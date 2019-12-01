#!/usr/bin/env python
# coding: utf-8

#Exercice 2

#Question 1


def numbers_sort(nums):

    max_num = max(nums) #getting the max number of the list
    n = max_num + 1 #adding 0
    occur = [0] * n  #initializing the occurence of each number at 0

    for num in nums: #browsing the numbers of the list
        occur[num] += 1 #increasing the occurence by 1 everytime it encounters the number

    sorted_list = []
    for num in range(n): #for each number we append it n times to a new list (n being the occurence of the number)
        sorted_list += [num] * occur[num]

    return sorted_list



#Question 2


letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz" #choosing and creating my order of letters
dic1 = dict(enumerate(letters)) #creating my dictionary by affecting a key value to each letter
dic = dict((v, k) for k, v in dic1.items()) #inversing my dictionary mapping



def max_letter(lst): #creating a function getting the max value of the given list
    max_letter = lst[0]
    for k in range(len(lst)):
        if dic[lst[k]] >= dic[max_letter]:
            max_letter = lst[k]
    return max_letter



def letters_sort(lst):
    a = max_letter(lst) #getting the maximum value of the list
    ind_a = letters.index(a) #now getting the index of this one

    letters_list = [] #creating an empty letters list
    for i in range(ind_a+1): #browsing
        letters_list.append(letters[i]) #storing all letters

    occur = [0] * len(letters_list) #initialization of all letters to 0 such as the number method we used earlier

    for letter in lst:   #browsing the letters of the list
        ind = letters_list.index(letter)
        occur[ind] += 1 #increasing the occurence by 1 everytime it encounters the letter

    sorted_letters_list = []
    for ind in range(len(occur)): #for each letter we append it n times to a new list (n being the occurence of the number)
        sorted_letters_list += occur[ind] * [letters_list[ind]]


    return sorted_letters_list



#Question 3


#Our order of letters change because we use python order in a recursive function
#Our function uses the following order : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz

def words_sort(arr):

    if len(arr) < 2: #if there is only one word in our list
        return arr
    else:
        pivot = arr[0] #initialization
        less = [i for i in arr[1:] if i <= pivot] #creating a list with the elements inf
        more = [i for i in arr[1:] if i > pivot] #creating a list with the elements supp

        return words_sort(less) + [pivot] + words_sort(more)
        #he function is reapplied recursively on more and less until it remains only one element


#complexity O(n2)
