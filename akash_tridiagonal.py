''' 
Author  :   Akash Yadav 
            1710003
            Integrated M.Sc Physics 
            National Institute of technology, Patna

Title   :   for solving systems with tridiagonal matrices  
            
Comment :   use this script only for diagonally dominant matrix.
            -working properly(tested)
            
          
'''
import numpy as np 


class tridiagonal(): 
    '''
    This class is for solving system of equation 
    where, we get tridiagonal matrix, 
    [A][x] =[b]
    you have to provide matrix(A) and vector (b) and you will get solution [x] in the form of array

    '''
    def __init__(self,matrix,vector,order):
        self.order = order
        self.matrix= np.array(matrix,float)
        self.vector = np.array(vector,float)
        self.x = np.zeros(self.order)


    def eliminate(self):
        for i in range(1,self.order):
            #updating diagonal term- 
            self.matrix[i,i] = self.matrix[i,i] - (self.matrix[i,i-1] * self.matrix[i-1,i])/self.matrix[i-1,i-1]
            
            #updating vector - 
            self.vector[i]= self.vector[i] - (self.matrix[i,i-1] /self.matrix[i-1,i-1])*self.vector[i-1]
            #updating upper diagonal remains same - 
            #updating lower diagonal- 
            self.matrix[i,i-1] = 0 
            

    def subst(self):
        self.x[-1] = self.vector[-1]/self.matrix[-1,-1]
        for n in range(self.order-2,-1,-1):
            self.x[n] = (self.vector[n] - self.matrix[n,n+1]* self.x[n+1])/self.matrix[n,n]
           

    def solve(self):
        self.eliminate()
        # print("matrix=\n",self.matrix)
        # print("solution for given system is :\n ",self.vector)
        self.subst()
        return self.x

        
    


     











           











