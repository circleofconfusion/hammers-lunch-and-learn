#
#
# Code for using the merge sort algorithm to sort an array of 100000 elements 
#  using 1 Raspberry Pi.  This code will be used in the other programs so have 
#  them in the same directory before running them.
#
#
import MergeSort #Imports mergesort functions
import random
import time

#Create an array to be sorted
arraylength = 100000 #Length of array to be sorted
print 'Length of array is', arraylength
array = range(arraylength) #Creates array
random.shuffle(array) #Jumbles up array

#Sort and time sorting process
start_time = time.time() #Records start time
print 'Sorting array...'
array = MergeSort.mergesort(array) #Sorts array
print 'Array sorted.'
time_taken = time.time() - start_time #Calculates and records time_taken

print 'Time taken to sort is ', time_taken, 'seconds.' 

