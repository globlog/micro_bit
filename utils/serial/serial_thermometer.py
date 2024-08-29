import tkinter as tk

min_v = -20
max_v = 30
stepsize = 10
steps = (max_v - min_v)//stepsize + 1

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.canvas = GradientFrame(self, "red", "blue", borderwidth=1, relief="sunken")
        self.canvas.pack(side="bottom", fill="both", expand=True)

class GradientFrame(tk.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="red", color2="black", **kwargs):
        tk.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self._level = None
        self.bind("<Configure>", self._draw_gradient)


    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        self.delete("texts")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = height
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(0,i,width,i, tags=("gradient",), fill=color)
        self.lower("gradient")
        for i in range(steps):
            value = str(min_v+(max_v-min_v)*i//(steps-1))
            dy = ((i+1/2) * limit)/steps
            self.create_text(0.9*width, limit - dy , text = value, tags=("texts",))
        self._draw_rect()

    def update(self,level):
        self._level = level
        self._draw_rect()

    def _draw_rect(self):
        if not self._level is None:
            self.delete("rects")
            self.delete("text")
            perc = (self._level-min_v)/(max_v-min_v)
            width = self.winfo_width()
            height = self.winfo_height()
            limit = height
            dy = (perc - 1/(2*steps))*limit
            self.create_rectangle(0.7*width, limit, 0.8*width, limit-dy, fill='white', tags=("rects",))
            self.create_text(0.6*width, limit - dy, text = str(self._level), tags=("text",))

#To read CPU levels instead
#import psutil
#level = psutil.cpu_percent(frames/1000)


frames = 100
import serial

def update(root, canvas):
    level = b''
    while level == b'':
        with serial.Serial('/dev/cu.usbmodem102', 115200, timeout=1) as ser:
            level = ser.readline()   
    level = int(level)
    canvas.update(level)
    root.after(frames, update, root, canvas)


if __name__ == "__main__":
    root = tk.Tk()
    x = Example(root)
    x.pack(fill="both", expand=True)
    root.after(frames, update, root, x.canvas)
    root.mainloop()
    