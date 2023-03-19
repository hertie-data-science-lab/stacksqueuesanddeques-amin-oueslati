# -*- coding: utf-8 -*-
"""
Submitted on 19th March 2022

@author: Oskar Krafft | Paul Sharratt | Fabian Mertz | Amin Oueslati
"""

from ArrayDeque import ArrayDequeMaxlen

          
AQM = ArrayDequeMaxlen(20)

#print('Adding last')
#for i in range(100):
 #   AQM.enqueue_last(i)
  #  print (i, AQM._data)
    
print ('\nAdding first')
# for i in range(20, 10, -1):
for i in range(0, 50):
    AQM.enqueue_first(i)
    print (i, AQM._data)
    
print(AQM._front)

print('\nPerforming the removals')
while not AQM.is_empty():
    print ('Remove first', AQM.first(), AQM.dequeue_first(), 'Remove last', AQM.last(),  AQM.dequeue_last())