#Antonio Maniscalco
#CS351 Assignment 4: Benchmark File
#3/11/2022
#Instructor: Dr. Ben McCamish
#Language: Python Version: 3.8
import hw4 as a


def printInput():
    print("-----------------------------------------------------------------------------")
    print("Literal Count: "+str(a.litCount) +"\nRuns of 1 Count: " + str(a.oneCount) +"\nRuns of 0 Count: " +str(a.zeroCount))
    print("-----------------------------------------------------------------------------")

def main():
   
    a.create_index("./data/animals.txt", "./data/bitmaps", 1)
    a.create_index("./data/animals_small.txt", "./data/bitmaps", 1)
    
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals.txt_sorted", "./data/compressed/", "WAH", 8)
    print("animals.txt_sorted: WAH_8")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals", "./data/compressed/", "WAH", 8)
    print("animals: WAH_8")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small.txt_sorted", "./data/compressed/", "WAH", 8)
    print("animals_small.txt_sorted: WAH_64")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small", "./data/compressed/", "WAH", 8)
    print("animals_small: WAH_8")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals.txt_sorted", "./data/compressed/", "WAH", 16)
    print("animals.txt_sorted: WAH_16")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals", "./data/compressed/", "WAH", 16)
    print("animals: WAH_16")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small.txt_sorted", "./data/compressed/", "WAH", 16)
    print("animals_small.txt_sorted: WAH_16")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small", "./data/compressed/", "WAH", 16)
    print("animals_small: WAH_16")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals.txt_sorted", "./data/compressed/", "WAH", 32)
    print("animals.txt_sorted: WAH_32")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals", "./data/compressed/", "WAH", 32)
    print("animals: WAH_32")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small.txt_sorted", "./data/compressed/", "WAH", 32)
    print("animals_small.txt_sorted: WAH_32")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small", "./data/compressed/", "WAH", 32)
    print("animals_small: WAH_32")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals.txt_sorted", "./data/compressed/", "WAH", 64)
    print("animals.txt_sorted: WAH_64")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals", "./data/compressed/", "WAH", 64)
    print("animals: WAH_64")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small.txt_sorted", "./data/compressed/", "WAH", 64)
    print("animals_small.txt_sorted: WAH_64")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0
    a.compress_index("./data/bitmaps/animals_small", "./data/compressed/", "WAH", 64)
    print("animals_small: WAH_64")
    printInput()
    a.litCount, a.oneCount, a.zeroCount = 0,0,0


    
    #**************DELETE WHEN DONE DEBUGGING***********************
    #result = filecmp.cmp("./data/compressed/animals_small_WAH_8", "./answers/data/compressed/animals_small_WAH_8", shallow=False)
    #print(result)
    #result = filecmp.cmp("./data/compressed/animals_small_WAH_16", "./answers/data/compressed/animals_small_WAH_16", shallow=False)
    #print(result)
    
if __name__ == "__main__":
    
    main()