''' 
Author  :   Akash Yadav 
            1710003
            Integrated M.Sc Physics 
            National Institute of technology, Patna

Title   :   for solving partial differential equation using finite 
            difference method.

Comment :             
'''

import numpy as np
import math
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
import matplotlib.animation as animation

import akash_interact as itr
import akash_tridiagonal as tri
pi = math.pi 
e = math.e

class finite_diff():
    """   General class for different types of pde """
    # stuff like creating mesh common to all problems 
    pass 

class parabolic_explicit(finite_diff):
    h = 0.01
    k = 0.00005
    sigma = k/h**2

    def __init__(self):
        self.x_init  = 0  #depends on boundary cond
        self.x_final = 1  #depends on boundary cond

        self.t_init  = 0  #depends on boundary cond
        self.t_final = 1 # that I'm free to choose 

        self.create_grid()
        self.update_grid_init()

    def create_grid(self):
        #let's make domain_grid  ---> grid(x,t)
        self.num_x = int((self.x_final - self.x_init)/self.h ) +1 
        self.num_t = int((self.t_final - self.t_init)/self.k ) +1
        self.x_values = np.linspace(self.x_init, self.x_final,self.num_x)
        print(self.x_values)
        self.grid = np.zeros([self.num_t,self.num_x]) # empty grid of desired size 

    def update_grid_init(self):
        # assigning initial values ( t = 0)
        print(self.grid)
        for i in range(0,self.num_x):
            self.grid[0,i] = (math.e**(self.x_values[i]))**2
        print(self.grid)


    def solve(self):
        """
        this function uses explicit mehod to move forward the values to u(x,t) in time 
        by 'one time step' that is 'k'
        """      
        for j in range(0,self.num_t -1):
            # setting boundary values i = 0 & i = n 
            self.grid[j+1,0] = 0 
            self.grid[j+1,-1]= 0
            # we need to update values for i = 1 to i = n-1
            for i in range(1,self.num_x-1):
                self.grid[j+1,i] = self.sigma*self.grid[j,i+1] + (1-2*self.sigma )*self.grid[j,i] + self.sigma*self.grid[j,i-1]   

        self.fig = itr.gui(self.grid,self.h,self.k,self.t_init,self.t_final,self.x_values)
        self.fig.interact()


class parabolic_crank(finite_diff):
    '''
    This class is for solving parabolic pde problem using crank-nichelson method 
    '''
    def __init__(self,func):
        self.x_init = 0      #given in the problem
        self.x_final   = 1   #given in the problem
        self.t_init    = 0   #given in the problem
        self.t_final   = 0.1 #given in the problem
        self.D = 0.1         #diffusion constant 
        # grid parameters 
        self.h = 0.001
        self.k = 0.001
        self.s = (1/self.D)*(self.h**2) / self.k 
        self.r = 2 + self.s 
        self.setup_grids(func)
        self.set_tridiagonal_matrix()

    def setup_grids(self,func):
    
        # calculating the size of grid 
        self.steps_x = int((self.x_final- self.x_init)/self.h + 1 )
        self.steps_t = int((self.t_final -self.t_init)/self.k + 1 )
        #making an empty grid of calulated dimensions 
        self.grid = np.zeros([self.steps_t,self.steps_x])
        self.x = np.linspace(self.x_init,self.x_final,self.steps_x)
        # setup the initial condition u(x,0) = f(x)
        for i in range(0,self.steps_x):
            # grid[0,i] = math.sin(pi*x[i])
            self.grid[0,i] =  func(self.x[i])
            
    def set_tridiagonal_matrix(self):           
        # make a tridiagonal matrices 
        self.tri_matrix = np.zeros([self.steps_x-2,self.steps_x-2])
        for i in range(0,self.steps_x -2):
            self.tri_matrix[i,i] = self.r 
            self.tri_matrix[i-1,i] = -1
            self.tri_matrix[i,i-1] = -1
        #print(tri_matrix)

    def update_grid(self,b):
        # this function accepts b and gives values of u on step forward in time - 
        matrix_problem = tri.tridiagonal(self.tri_matrix,b,self.steps_x-2)
        result = matrix_problem.solve()
        print(result)
        return result 

    def solve(self):
        
        for i in range(0,self.steps_t-1):
            b = self.s*self.grid[i,1:self.steps_x-1]
            u_next = self.update_grid(b)
            self.grid[i+1,1:self.steps_x-1] = u_next
            # plt.plot(x,grid[i,0:])
    
        self.fig = itr.gui(self.grid,self.h,self.k,self.t_init,self.t_final,self.x)
        self.fig.interact()




    #....................................................................................

class hyperbolic(finite_diff):

    def __init__(self,u0,u0_t):
        #  here u0 = u(x,0) and u0_t = u_t(x,0) 
        #  you need to define and pass functions u0 and u0_t, during object creation
    
        self.x_init = 0       #given in the problem
        self.x_final   = 1   #given in the problem
        self.t_init    = 0    #given in the problem
        self.t_final   = 1    #given in the problem
        self.c = 1            # speed of wave 

        #boundary values 
        self.ux_init = 0 
        self.ux_final= 0 
        # grid parameters 
        self.h = 0.01    # step in position 
        self.k = 0.001   # time step
        self.p = (self.c**2)*(self.k**2)/(self.h**2)
    
        self.setup_grids(u0,u0_t)

    def setup_grids(self,u0,u0_t):
    
        # calculating the size of grid 
        self.steps_x = int((self.x_final- self.x_init)/self.h + 1 )
        self.steps_t = int((self.t_final -self.t_init)/self.k + 1 + 1 )  # adding extra row for (t = -k)
        #making an empty grid of calulated dimensions 
        self.grid = np.zeros([self.steps_t,self.steps_x])
        self.x = np.linspace(self.x_init,self.x_final,self.steps_x)
        # setup the initial condition u(x,0) = f(x)
        for i in range(1,self.steps_x):
            # grid[0,i] = math.sin(pi*x[i])
            self.grid[1,i] =  u0(self.x[i])                             # updating  t = 0  row 
            self.grid[0,i] =  self.grid[1,i] - self.k * u0_t(self.x[i]) # updating  t = - k row 

        

    def solve(self):
        for i in range(1,self.steps_t-1):
            self.grid[i,0]  = self.ux_init
            self.grid[i,-1] = self.ux_final
            for j in range (1,self.steps_x-1):
                self.grid[i+1,j] = ( self.p * self.grid[i,j+1] + (self.p -2) *self.grid[i,j] +  self.p * self.grid[i,j-1] - self.grid[i-1,j])
        
       
    def gui(self):
       
        fig = itr.gui(self.grid,self.h,self.k,self.t_init,self.t_final,self.x)
        fig.plot_setting("solution of wave-equation","x","u(x,t)",(self.x_init,self.x_final),(-15,15))
        fig.interact()

        

def u0(x):
    val= math.sin((pi)*x)
    return val

def u0_t(x):
    val = 0
    return val

prob1 = hyperbolic(u0,u0_t)
prob1.solve() 


fig = plt.figure()
myplot = fig.add_subplot(111)
print(prob1.grid)

def anim(N):
  
    u_data = prob1.grid[N,0:]
    myplot.clear()
    myplot.plot(prob1.x,u_data)
    myplot.set_xlim(0,prob1.x_final)
    myplot.set_ylim(-15,15)
    N = N + 1 

ani = animation.FuncAnimation(fig,anim,interval =1000)
plt.show()









    