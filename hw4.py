#Antonio Maniscalco
#CS351 Assignment 4
#3/11/2022
#Instructor: Dr. Ben McCamish
#Language: Python Version: 3.8

import csv
import os


#function to sort our text file lexicographically
def fileSort(inputFile):
    sortList = open(inputFile).read().split('\n')
    sortList.sort()
    sortedFile = open((inputFile + "_sorted"), "w")
    for row in sortList:
        if row != "": sortedFile.write((row + "\n"))
    sortedFile.close()
    return((inputFile + "_sorted"))

#function for creating bitmap files
def create_index(input_path, output_path, sorted):
    if sorted: inFile = fileSort(input_path)
    else: inFile = input_path

    #define animals and range concatinate name of file to our output directory
    animalType = ["1000", "0100", "0010", "0001"]
    ageRange = ["1000000000", "0100000000", "0010000000", "0001000000", "0000100000", 
    "0000010000", "0000001000", "0000000100", "0000000010", "0000000001"]

    outFile = ""
    outFile += inFile.split('/')[-1]
    if not sorted: outFile = outFile[ :outFile.index('.')]
    outFile = output_path + "/" + outFile
    writeFp = open(outFile, "w")

    #open input file as a csv file where each row is seperated by a comma
    with open(inFile) as csv_file:
        fileRead = csv.reader(csv_file, delimiter = ',')
        for row in fileRead:
            writeString = "" 
            animal, age, adopted = row[0], row[1], row[2]

            #check animals
            if("cat" in animal):
                writeString += animalType[0] 
            elif("dog" in animal):
                writeString += animalType[1]
            elif("turtle" in animal):
                writeString += animalType[2]
            elif("bird" in animal):
                writeString += animalType[3]

            #set our age range 
            intAge = int(age)
            if intAge >=1 and intAge <= 10:
                writeString += ageRange[0]
            elif intAge >= 11 and intAge <=20:
                writeString += ageRange[1]
            elif intAge >= 21 and intAge <= 30:
                writeString += ageRange[2]
            elif intAge >= 31 and intAge <= 40:
                writeString += ageRange[3]
            elif intAge >= 41 and intAge <= 50:
                writeString += ageRange[4]
            elif intAge >= 51 and intAge <= 60:
                writeString += ageRange[5]
            elif intAge >= 61 and intAge <= 70:
                writeString += ageRange[6]
            elif intAge >= 71 and intAge <= 80:
                writeString += ageRange[7]
            elif intAge >= 81 and intAge <= 90:
                writeString += ageRange[8]
            elif intAge >= 91 and intAge <= 100: 
                writeString += ageRange[9]

            #add adopted or not bits to end of string and new line
            if("True" in adopted): writeString += "10\n"
            else: writeString += "01\n"
            writeFp.write(writeString)
    writeFp.close()
    csv_file.close()
    #if it's sorted we need to also create an unsorted bitmap so remove sorted textfile and call create index again
    if sorted:
        os.remove(inFile)
        create_index(input_path, output_path, 0)

#Function to compress our given bitmap index
def compress_index(bitmap_index, output_path, compression_method, word_size):
    #generate name for output file open our files and store contents from bitmap index 
    writeFp = open((output_path+"/"+(bitmap_index.split("/")[-1])+"_"+compression_method+"_"+str(word_size)), "w")
    sortList = open(bitmap_index).read().split('\n')
    for i in range(0, len(sortList)): sortList[i] = list(sortList[i])

    #pop last empty element in sort list and calculate our max num of runs for wordsize(2^(n-2)) Then transpose columns to rows and store in newTable
    sortList = sortList[:-1]
    runOverflow = (2**(word_size-2))
    newTable = [[sortList[y][x] for y in range(len(sortList))] for x in range(len(sortList[0]))]

    #loop through our rows and join lists to make them strings, compress these lines and write to our file
    for row in newTable:
        tmpStr = ''.join(str(i) for i in row)
        compLine(writeFp, tmpStr, (word_size-1), runOverflow)
        writeFp.write("\n")
    writeFp.close()

#Function to compress each line for output file
def compLine(writeFp, mystr, wordSize, runOverflow):
    
    #Init values and generate format str for our runs depending on word size-2
    compressedLine = ''
    isZero, isOne = False, False
    runCount, i = 0, 0
    formatSpecifier = '{0:0' + (str((wordSize-1))) +'b}'

    #Iterate through passed string grabbing word size -1 each iteration
    while i < len(mystr):
        tmp = mystr[i: i+(wordSize)]

        #Check for Run of zeros or ones
        if tmp.count('0') == wordSize or tmp.count('1') == wordSize:
            if tmp[0] == '0':
                #***Global for benchmark nothing to do with compression***
                #global zeroCount
                #zeroCount +=1

                #Check if we had another run of 1's if so append prev run str to comp line and adjust values
                isZero = True
                if(isOne == True):
                    isOne, compressedLine, runCount = diffRunHandler(isOne, compressedLine, runCount, 1, formatSpecifier)

                #Increment values and if we end on a run append to compressed str before we exit loop
                runCount += 1 
                i += wordSize
                if(i >= len(mystr)): compressedLine += ("10" + formatSpecifier.format(runCount, "b")) 

            elif tmp[0] == '1':
                ##***Global for benchmark nothing to do with compression***
                #global oneCount
                #oneCount +=1

                #Check if we had another run of 0's if so append prev run str to comp line and adjust values
                isOne = True
                if isZero == True:
                    isZero, compressedLine, runCount = diffRunHandler(isZero, compressedLine, runCount, 0, formatSpecifier)

                #Increment values and if we end on a run append to compressed str before we exit loop    
                runCount += 1
                i += (wordSize)
                if(i >= len(mystr)): compressedLine += ("11" + formatSpecifier.format(runCount, "b"))

            #Check for overflow. If our run count is 2^(wordcount-2)-1, append full run str and reset our values
            if runCount == (runOverflow-1):
                if isZero == True: compressedLine += ("10" + "1"*(wordSize-1))
                else: compressedLine += ("11" + "1"*(wordSize-1))
                isZero = False
                isOne = False
                runCount = 0

        #If we reach this case we have a literal so check for previous runs then append our literal                  
        else:
            #***Global for benchmark nothing to do with compression***
            #global litCount
            #litCount += 1

            if runCount > 0:
                if isOne == True:
                    isOne, compressedLine, runCount = diffRunHandler(isOne, compressedLine, runCount, 1, formatSpecifier)
                elif isZero == True:
                    isZero, compressedLine, runCount = diffRunHandler(isZero, compressedLine, runCount, 0, formatSpecifier)        
            compressedLine += ("0" + tmp)
            runCount = 0
            i += (wordSize)

    #Check if we need to pad the end of the str once we are done compressing then write to output file    
    if(padding := (len(mystr)) % wordSize) != 0: 
        compressedLine += ("0"*(wordSize - padding))
    writeFp.write(compressedLine)
    

#Function for handling previous runs of a different value from the current. Returns tuple to reset and adjust values
def diffRunHandler(flg, compressedLine, runCount, runNum, formatSpec):
    flg = False
    if runNum == 1: compressedLine += ("11" + formatSpec.format(runCount, "b"))
    else: compressedLine += ("10" + formatSpec.format(runCount, "b"))
    return(flg, compressedLine, 0)


