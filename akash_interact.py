''' 
Author  :   Akash Yadav 
            1710003
            Integrated M.Sc Physics 
            National Institute of technology, Patna

Title   :   for data visualization 
Comment :   

'''
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.widgets import Slider


class gui():
    '''
    This class is for visualization of data, you have to provide aleady processed data 
    the data in the form of matix or array.
    ''' 
    def __init__(self,grid,h,k,t_init,t_final,x_values):
        self.t_init = t_init
        self.t_final = t_final 
        self.grid = grid 
        self.h = h 
        self.k = k 
        self.x_values = x_values
    
    def plot_setting(self,title,x_label,y_label,xlim,ylim):
        # this function allows to set plot characterstics from another module  
        self.title = title 
        self.x_label = x_label
        self.y_label = y_label
        self.xlim = xlim
        self.ylim = ylim 


    def interact(self):
        # this function is for slider interface 
        self.fig,self.ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        axcolor = 'lightgoldenrodyellow'
        axtime =  plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)   
        self.slider_time = Slider(axtime, 'time',valinit= self.t_init, valmin=self.t_init,valmax= self.t_final , valstep=self.k)

        self.j= 0
        self.ax.plot(self.x_values,self.grid[self.j,:])
        
        self.slider_time.on_changed(self.update)
        self.ax.set_ylim(self.ylim)
        self.ax.set_xlim(self.xlim)
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)



    def update(self,val):
        self.ax.clear()
        self.j = int(self.slider_time.val / self.k)
        self.ax.plot(self.x_values,self.grid[self.j,:])
        self.ax.set_ylim(self.ylim)
        self.ax.set_xlim(self.xlim)
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)

        
        
        self.fig.canvas.draw_idle()


class animate():

    def __init__(self,grid,h,k,t_init,t_final,x_values):
        self.t_init = t_init
        self.t_final = t_final 
        self.grid = grid 
        self.h = h 
        self.k = k 
        self.x_values = x_values
        self.fig  = plt.figure()
        self.my_plot = self.fig.add_subplot(111)
        self.ani = animation.FuncAnimation(self.fig,self.anim)
        
        

    def anim(self,N=1):
    
        self.u_data = self.grid[N,0:]
        self.my_plot.plt(self.x_values,self.u_data)
        N = N + 1


        

        



        






   


        




