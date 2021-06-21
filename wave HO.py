''' 
Author  :   Akash Yadav 
            1710003
            Integrated M.Sc Physics 
            National Institute of technology, Patna

Title   :   wave equation solution using finite difference method 

Comment :             
'''

import numpy as np 
import matplotlib.pyplot as plt 
import math 
import matplotlib.animation as animation
pi = math.pi 
e = math.e
#end point 
open = "yes"
# oscillator 
A = 0 # amplitude
w = 20  # frequency

x_init = 0
x_final= 1
t_init = 0
t_final= 10
c =1 
h = 0.005
k = 0.004
p = (c*k/h)**2
steps_x  =int( (x_final - x_init)/h +1 )
steps_t  =int( (t_final - t_init)/k +1 )

# make grid 
grid = np.zeros([steps_t,steps_x],float)
x_val = np.linspace(x_init,x_final,steps_x)
t_val = np.linspace(t_init,t_final,steps_t)


# def f(x):
#     if x<0.5:
#         val = 10*x
#     if x>=0.5:
#         val = -10*(x-1) 
#     return val

def f(x):
    if x > 0.3 and x < 0.5 : 
        val = 10*e**-((x-0.4)/0.05)**2
        return val

    else :
        return 0 

# def f(x):
#     return 0 


        


# updating grid except at  boundary points 
for i in range(0,steps_x):
    grid[0,i] = f(x_val[i])

for j in range(1,steps_x-1):
    grid[1,0] = A*math.sin(w*t_val[1])  # adding oscillator on left end 
    grid[1,j] = (p/2)*( f(x_val[j+1]) + f(x_val[j-1])) + (1-p)* f(x_val[j]) 
    # end -- open/ closed 
    if open == "yes":
      grid[1,-1] = grid[1,-2]
    
i = 0
j = 0 

for i in range (1,steps_t-1):
    for j in range(1,steps_x-1):
        grid[i+1,0] = A*math.sin(w*t_val[i+1]) # adding oscillator on left end 
        grid[i+1,j] = p*grid[i,j+1] +  2*(1-p)*grid[i,j] + p*grid[i,j-1] - grid[i-1,j]
        # end - open/closed 
        if open == "yes":
            grid[i,-1] = grid[i,-2]
    


fig,ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [],linewidth=5,color='black')


def init():
    ax.set_xlim(x_init,x_final)
    ax.set_ylim(-15, 15)
    return ln,

def update(N):
    xdata=  x_val
    ydata = grid[N]
    ln.set_data(xdata, ydata)
    
    return ln,

ani = animation.FuncAnimation(fig, update,
                    init_func=init, blit=True,interval= 10)
plt.show()












