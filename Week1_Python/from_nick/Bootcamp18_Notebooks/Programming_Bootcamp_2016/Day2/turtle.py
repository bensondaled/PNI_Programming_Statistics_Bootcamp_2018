import numpy as np
import matplotlib.pyplot as pl

class Turtle():
    """Matplotlib-based turtle class for teaching basic programming

    Implements an agent that can be moved around the screen using commands.
    """

    def __init__(self):

        # turtle
        self.angle = 0 # heading angle in degrees
        self.x = self.y = 0 # x and y positions
        self.radius = 10
        self.colour = 'green'
        self._line_colour = self.colour
        self.alpha = 0.5

        # graphics params
        self._fignum = 'Turtle Land'
        self._lim = 200
        self._setup_graphics()

    def _setup_graphics(self):
        self._fig = pl.figure(self._fignum)
        self._ax = self._fig.add_subplot(111)
        self._ax.set_aspect('equal')
        self._ax.set_xlim([-self._lim-self.radius, self._lim+self.radius])
        self._ax.set_ylim([-self._lim-self.radius, self._lim+self.radius])

        # init turtle
        self._patch = pl.Circle((self.x, self.y), radius=self.radius, fc=self.colour, alpha=self.alpha)
        self._ax.add_patch(self._patch)
        self._draw()

    def move(self, dist):
        """ Move the turtle *dist* distance """
        self._draw()

        x_new = self.x + dist*np.sin(self.angle * np.pi/180.)
        y_new = self.y + dist*np.cos(self.angle * np.pi/180.)

        # prevent from going off screen
        if abs(x_new) > self._lim:
            x_new -= x_new - np.sign(x_new) * self._lim
        if abs(y_new) > self._lim:
            y_new -= y_new - np.sign(y_new) * self._lim

        # draw the path
        line = pl.Line2D((self.x, x_new), (self.y, y_new), color=self._line_colour)
        self._ax.add_line(line)

        # update the position
        self.x, self.y = x_new, y_new

        self._draw()

    def set_color(self, col):
        """
        set_color(col)     sets the pen color to col. 
        
        Example: >> set_color[0, 1, 0]   sets the pen color to green
        
        PARAMS:
            col     a 3-element list, [r, g, b], where each element is
                    between 0 and 1, and they represent the amount of red,
                    green, and blue in the pen color respectively.
        RETURNS:
            none
        """
        self._line_colour = col

    def turn(self, angle):
        """ 
        Rotate the heading direction of the turtle *angle* degrees clockwise 
        
        PARAMS:
            angle   a scalar, in degrees (not radians), indicating the angle to turn by
            
        RETURNS:
            the resulting heading angle of the turtle
        
        """
        self.angle += angle
        if self.angle >= 360:
            self.angle -= 360
        return self.angle
    
    def get_angle(self, angle):
        """ Returns the current heading angle of the turtle"""
        return self.angle
    
    def get_position(self):
        """ Returns two outputs, x, y, the current position of the turtle"""
        return self.x, self.y

    def go_home(self):
        """ Move turtle to (0,0) """
        self.x = self.y = self.angle = 0
        self._draw()

    def reset(self):
        """ Move turtle to (0,0) and clear the graphics panel"""
        self.go_home()
        pl.close(self._fig)
        self._setup_graphics()

    def _draw(self):
        if not pl.fignum_exists(self._fignum):
            self._setup_graphics()
        self._patch.center = (self.x, self.y)
        self._fig.canvas.draw()
        try:
            self._fig.canvas.flush_events()
            self._fig.canvas.manager.show()
            self._fig.canvas.manager.window.raise_()
        except:
            pass
