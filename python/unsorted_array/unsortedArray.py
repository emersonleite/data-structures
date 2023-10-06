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

    def addItem(self, valor):
        if self.lastPosition == self.vectorLength -1:
            print('Capacidade máxima atingida')
        else:
            self.lastPosition += 1 
            self.values[self.lastPosition] = valor

    # O(n)
    def searchItem(self, valor):
        for i in range(self.lastPosition + 1):
            if(valor == self.values[i]):
                return i
        return -1
    
    # O(n)
    def removeItem(self, valor):
        position = self.searchItem(valor)
        if position == -1:
            return -1
        else:
            for i in range(position, self.lastPosition):
                self.values[i] = self.values[i + 1]
            self.lastPosition -= 1
        
            
        

vetor = UnsortedArray(10)
vetor.addItem(3)
vetor.addItem(2)
vetor.addItem(4)
vetor.addItem(5)
vetor.addItem(6)
vetor.addItem(1)

vetor.printValues()

vetor.searchItem(5)
vetor.searchItem(9)

vetor.removeItem(5)
  