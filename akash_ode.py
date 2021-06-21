'''
Author - Akash Yadav
         1710003
         Integrated M.Sc. Physics
         National Institute of Technology ,Patna

AIM -    second order ode solver.
Comment- 
'''
import math
import matplotlib.pyplot as plt 
import numpy as np

class ode:
    """
    
    This class is intended to solve system of differential equation.
    Numerical scheme used -> predictor corrector method
    Setup initial conditions.
    Note - enter functions in string format only  
    if you want to solve only one equation --
    ode('func1','0')
    """
  
    def __init__(self,init):
       # intial conditions informat --[(x0,y0),(x1,y1)]

       # default 
        
        self.__xlim = 10
        self.__h = 0.1
        self.init = init
        self.x_data  = [self.init[0][0]]
        self.y1_data = [self.init[0][1]]
        self.y2_data = [self.init[1][1]]
        self.steps  = int((self.__xlim - self.init[0][0])/self.__h) # default number of self.steps 
    
    def flash_data(self):
        self.x_data  = [self.init[0][0]]
        self.y1_data = [self.init[0][1]]
        self.y2_data = [self.init[1][1]]


    def set_xlim(self,xlim,h):
        self.__x_lim = xlim
        self.__h = h 
        self.steps  = int((self.__x_lim - self.init[0][0])/self.__h)



    def func(self,x,y_vec):
        self.x = x 
        self.y1 = y_vec[0]
        self.y2 = y_vec[1]
        # f1 = eval(self.f1)
        # f2 = eval(self.f2)
        f1,f2 = self.set_func()
        f = np.array([f1,f2])
        return f
        

    def set_func(self):
        x = self.x 
        y1 =self.y1 
        y2 =self.y2 
        # setup your function 
        f1 = 0
        f2 = 0
        if f1 ==0 and f2 == 0 :
            print("WARNING:: valid functions f1 and f2 are required for proceeding" 
            "\n  HINT --->>> introduce set_func() in your code") 
            quit()

        return f1, f2 

        
    def solve(self,show_plot='no'):
        '''
        for solving initial value problem 
        Numerical Method used : Heun's method (predictor corrector method)
        
        '''
        for i in range(0,self.steps):
            h = self.__h
    
            y_vec = np.array([self.y1_data[i] , self.y2_data[i]])
         
            y_pre  = y_vec + h*self.func (self.x_data[i],y_vec)
            y_vec_next = y_vec + (h/2) *(self.func (self.x_data[i],y_vec) + self.func(self.x_data[i] + h , y_pre))
            self.x_data.append(self.x_data[i] + h)
            self.y1_data.append(y_vec_next[0])
            self.y2_data.append(y_vec_next[1])
        if show_plot =="yes":
            self.result()
            self.show()



    def result(self):
        
        plt.plot(self.x_data,self.y1_data)
        # plt.xlim(0,8)
        # plt.ylim(-4,4)
        
    @staticmethod
    def show():
        plt.show()


class ode_initial(ode):
    '''
    initial value problem
    '''
    pass
   

class ode_boundary(ode):

#########################################################################
########################## under development ############################
#########################################################################
 

    '''boundary value problem
    '''
    def __init__(self,init):
        ode.__init__(self,init)
        self.init = init 
        self.x1 = self.init[0][0]
        self.y1 = self.init[0][1]
        self.x2 = self.init[1][0]
        self.y2 = self.init[1][1]
        

        self.x_data  = [self.x1]
        self.y1_data = [self.y1]
        self.y2_data = [0] # we have to choose y'(0) by his and trial
        
       


    def shoot(self,trial_slope):
        # for solving boundary value problem
        self.set_xlim(self.x2,0.1) # setting x2 as x-limit
        self.y2_data[0] = trial_slope
        ode.solve(self)
        phi = self.y1_data[-1]  #  where phi is the y_hitting point 
        self.flash_data()
        # plt.scatter(self.x2,self.y2,color='red',linewidths=1)
        return phi

    def error (self):
        z1 = 0.1  # z1 and z1 are trial slopes( y'(0)) at initial point
        z2 = 2
        error = 1000
        while abs(error) > 0.001:
            phi_1 =  self.shoot(z1)
            phi_2  = self.shoot(z2)
            slope = (phi_2 - phi_1 )/(z1 - z1)
            guessed_z = ( self.y2 - phi_1)/(slope) + z1
            guessed_phi = self.shoot(guessed_z)
            
            error =  self.y2 - guessed_phi
            z1 = z2 
            z2 = guessed_z
            print("error = ",error)
        return error

    

    def solve (self):
        self.error()


    def show_hits(self):
        print("hit points are :",self.hit_points)

        


        




        












        












        



