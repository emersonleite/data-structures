import numpy as np

class UnsortedArray:
    def __init__(self, vectorLength): 
        self.vectorLength = vectorLength
        self.lastPosition = -1
        self.values = np.empty(self.vectorLength, dtype=int)
      
    def printValues(self):
        if self.lastPosition == -1:
            print('O vetor está vazio')
        else: 
            for i in range(self.lastPosition + 1):
                print(i, '-', self.values[i])

    # O(n)
    def addItem(self, value):
        if self.lastPosition == self.vectorLength -1:
            print('Capacidade máxima atingida')
            return
        
        position = 0
        for i in range(self.lastPosition + 1):
            position = i
            if self.values[i] > value:
                break
            if i == self.lastPosition:
                position = i + 1

        x = self.lastPosition
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -= 1

        self.values[position] = value
        self.lastPosition += 1


    # O(n)
    def linearSearch(self, value):
        for i in range(self.lastPosition + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.lastPosition:
                return -1

    # O(log n)     
    def binaySearch(self, value):
        bottomLimit = 0
        topLimit = self.lastPosition

        while True:
            currentPosition = int((bottomLimit + topLimit) / 2)
            if self.values[currentPosition] == value:
                return currentPosition
            elif bottomLimit > topLimit:
                return -1
            else:
                if self.values[currentPosition] < value:
                    bottomLimit = currentPosition + 1 
                else:
                    topLimit = currentPosition - 1

            
    # O(n)
    def removeItem(self, value):
        position = self.linearSearch(value)
        if position == -1:
            return -1
        else:
            for i in range(position, self.lastPosition):
                self.values[i] = self.values[i + 1]
            self.lastPosition -= 1 
        
            
        

vetor = UnsortedArray(10)

vetor.addItem(6)
vetor.addItem(4)
vetor.addItem(3)
vetor.addItem(5)
vetor.addItem(1)
vetor.addItem(8)



vetor.printValues()

print(vetor.linearSearch(3))
print(vetor.linearSearch(8))
print(vetor.linearSearch(2))
print(vetor.linearSearch(9))

print(vetor.binaySearch(3))

vetor.removeItem(5)
vetor.removeItem(1)
vetor.removeItem(8)
vetor.removeItem(9)

vetor.printValues()

  