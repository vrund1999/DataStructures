from re import L
from sys import hash_info


#Implemented a HashMap using Python lists that uses chaining

class HashMap:
    def __init__(self, arraySize = 100):
        self.array = [[] for i in range(0, arraySize)]
    
    def getHash(self, key):
        sum = 0

        for char in key:
            sum += ord(char)
        return sum % len(self.array)

    def __setitem__(self, key, value):
        hashIndex = self.getHash(key)

        arraySection = self.array[hashIndex]

        keyFound = False

        for index, element in enumerate(arraySection):
            if(element[0] == key):
                keyFound = True
                break
        
        if(keyFound):
            arraySection[index] = [key, value]
        else:
            arraySection.append([key, value])


    def __getitem__(self, key):
        hashIndex = self.getHash(key)
        keyFound = False

        arraySection = self.array[hashIndex]

        for index, element in enumerate(arraySection):
            if(len(element) > 0 and element[0] == key):
                keyFound = True
                break
        
        if (keyFound):
            return element[1]
        else:
            return "Key not found"

    def __delitem__(self, key):  
        hashIndex = self.getHash(key)
        keyFound = False

        arraySection = self.array[hashIndex]

        for index, element in enumerate(arraySection):
            if(element[0] == key):
                keyFound = True
                break
        
        if(keyFound):
            arraySection[index] = []
        else:
            print("Key not found")

if __name__ == '__main__':
    hashMap = HashMap()

    hashMap["march 6"] = 310
    hashMap["march 7"] = 420
    hashMap["march 8"] = 67
    hashMap["march 17"] = 63457
    hashMap["march 6"] = 1

    del hashMap["march 6"]

    print(hashMap["march 6"])



