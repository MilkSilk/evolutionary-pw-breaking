# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 22:12:54 2018

@author: Jacek
"""

import sys
import random

def getRandomPassword(length):
    password = 0
    for i in range(length):
        password += random.randrange(0,9,1)* 10**i
    return password

def randomGeneration(generationSize):
    randomGeneration = [[]for i in range(generationSize)]
    for i in range(generationSize):
        randomGeneration[i].append(getRandomPassword(passwordLength))
        randomGeneration[i].append(0)
    return randomGeneration

def getDigit (number, digit_index):
    if((10**digit_index)!=0):
        number = number//(10**(digit_index))
    return number%10

def generatePassword(parent1,parent2):
    newPass = 0
    for i in range(len(str(password))):
        seed = random.random()
        if (seed<=0.5-mutationPropability/2):
            added = getDigit(parent1,i)*(10**i)
            newPass += added
        elif(seed<=1-mutationPropability):
            added = getDigit(parent2,i)*(10**i)
            newPass += added
        else:
            newPass += random.randrange(0,9,1)*(10**i)
    return newPass

def nextGeneration(previousGeneration):
     newGeneration = [[]for i in range(generationSize)]
     sortedGeneration = sorted(previousGeneration, key=lambda kv: kv[1], reverse=True)
     for i in range(generationSize):
         parent1_index = random.randrange(0,generationSize/2,1)
         parent1 = sortedGeneration[parent1_index][0]
         parent2_index = parent1_index
         while(parent1_index==parent2_index):
             parent2_index = random.randrange(0,generationSize/2,1)
         parent2 = sortedGeneration[parent2_index][0]
         newGeneration[i].append(generatePassword(parent1,parent2))
         newGeneration[i].append(0)
     return newGeneration

generationSize = 100
passwordLength = 20
mutationPropability = 0.005
mutationPropabilityDelta = 0.0001
historicMutationPropabilites = []
password = getRandomPassword(passwordLength)
howManyGenerations = []
wasMedianWorsened = False
wasPreviousFaulty = False
for m in range (100):
    """
    if(m<30):
        mutationPropabilityDelta = 0.01
    elif(m<50):
        mutationPropabilityDelta = 0.001
    else:
        mutationPropabilityDelta = 0.0001
    """
    if(wasPreviousFaulty or wasMedianWorsened):
        mutationPropability -= mutationPropabilityDelta
    else:
        mutationPropability += mutationPropabilityDelta
    if m>4:
        for i in range(4):
            if(historicMutationPropabilites[m-i-2][1]!=historicMutationPropabilites[m-i-1][1]):
                break
            if(i==3):
                print("The optimal mutation propability is: "+str(historicMutationPropabilites[m-4][0]))
                quit()
    historicMutationPropabilites.append([mutationPropability,0,0])
    for l in range (100): #how many simulations
        currentGeneration = randomGeneration(generationSize)
        for i in range (100): #max number of generations
            for j in range(generationSize): #number of passwords in a generation
                for k in range(len(str(password))):
                    if (getDigit(currentGeneration[j][0],k)==getDigit(password,k)):
                        currentGeneration[j][1]+=1
            if (currentGeneration[0][0]==password):
                #print("Done! Needed "+str(i)+" generations to get the password")
                howManyGenerations.append(i)
                wasPreviousFaulty = False
                break
            if (i == 99):
                #print("Couldn't break the password! :c")
                wasPreviousFaulty = True
            previousGeneration = currentGeneration
            currentGeneration = nextGeneration(previousGeneration)
    howManyGenerations.sort()
    historicMutationPropabilites[m][1]=howManyGenerations[int(len(howManyGenerations)//2)]
    if(historicMutationPropabilites[m-1][1]<historicMutationPropabilites[m][1]):
        wasMedianWorsened = True
    else:
        wasMedianWorsened = False
    historicMutationPropabilites[m][2]=len(howManyGenerations)
    print(historicMutationPropabilites[m])
    howManyGenerations.clear()
print(mutationPropability)
    
        
    