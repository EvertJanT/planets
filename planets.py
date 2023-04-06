import tkinter as tk
import time, random
import numpy as np
from tkinter import IntVar

#teller = 0

class Scherm1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title('Gravitatie')
        master.geometry("250x700+400+50")
        self.logo = tk.PhotoImage(file="galaxy.gif")
        self.label = tk.Label(image=self.logo).pack()
        self.button1 = tk.Button(self.frame, text = 'Nieuw Scherm', width = 25, command = self.new_window)
        self.button1.pack()
        global gebruiker_invoer1 
        gebruiker_invoer1 = 700
        label1 = tk.Label(self.frame, text='hoogte')
        label1.pack()
        self.invoerSpinner1 = tk.Spinbox(self.frame,
                                        from_=650,
                                        to=2000,
                                        increment=25,
                                        textvariable = gebruiker_invoer1,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner1.pack()
        global gebruiker_invoer2 
        gebruiker_invoer2 = 500
        label2 = tk.Label(self.frame, text='breedte')
        label2.pack()
        self.invoerSpinner2 = tk.Spinbox(self.frame,
                                        from_=450,
                                        to=2000,
                                        increment=25,
                                        textvariable = gebruiker_invoer2,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner2.pack()
        global gebruiker_invoer3
        gebruiker_invoer3 = 9.8
        label3 = tk.Label(self.frame, text='gravitatie')
        label3.pack()
        self.invoerSpinner3 = tk.Spinbox(self.frame,
                                        from_=-40.0,
                                        to=100.0,
                                        increment=5,
                                        textvariable = gebruiker_invoer3,
                                        command=self.invoer,
                                        wrap=True)
        self.invoerSpinner3.pack()
        global gebruiker_invoer4
        gebruiker_invoer4 = IntVar()
        gebruiker_invoer4.set(0)
        self.checkbox1 = tk.Checkbutton(self.frame, text='zon',variable=gebruiker_invoer4,
                            onvalue=1, offvalue=0, command=self.invoer)
        self.checkbox1.pack()



        
        self.button2 = tk.Button(self.frame, text='stop', width = 25)
        self.button2['command'] = self.button_clicked
        self.button2.pack()
        self.frame.pack()

    def invoer(self):
        global gebruiker_invoer1, gebruiker_invoer2, gebruiker_invoer3, gebruiker_invoer4
        huidige_invoer1 = self.invoerSpinner1.get()
        huidige_invoer2 = self.invoerSpinner2.get()
        huidige_invoer3 = self.invoerSpinner3.get()
        gebruiker_invoer1 = huidige_invoer1
        gebruiker_invoer2 = huidige_invoer2
        gebruiker_invoer3 = huidige_invoer3
        
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Scherm2(self.newWindow)
    def button_clicked(self):
        self.master.destroy()

class Scherm2:
    def __init__(self, master):
        breedte = 700
        hoogte  = 500
        hoogte = int(gebruiker_invoer1)
        breedte = int(gebruiker_invoer2)
        
        self.master = master
        self.frame = tk.Frame(self.master)
        master.title('canvas')
        master.geometry(str(breedte) + 'x'+ str(hoogte) + '+650+50')
        self.quitButton = tk.Button(self.frame, text = 'Stop', width = 25,
                                    command = self.close_windows)

        self.quitButton.pack()
        mijnCanvas = tk.Canvas(self.frame, bg="white", height=hoogte, width=breedte)
        mijnCanvas.pack()
        while gebruiker_invoer4.get() == 1:
            mijnCanvas.create_oval(300-15, 300-15,300+15,300+15, fill='blue')
            break
        self.frame.pack()    
            
   
        class Bol:
            def __init__(self, kleur):
                self.size = random.randrange(2, 7)
                self.xpos = random.randrange(15,breedte-15)
                self.ypos =random.randrange(15,hoogte-15)
                self.vorm = mijnCanvas.create_oval(self.xpos-self.size, self.ypos -self.size,self.xpos +self.size,self.ypos+self.size, fill=kleur)
                self.vx = random.randrange(-2, 2)
                self.vy = random.randrange(-2, 2)
                self.massa = self.size

            def update_zijkanten(self):
                mijnCanvas.move(self.vorm, self.vx, self.vy)
                pos = mijnCanvas.coords(self.vorm)
                if pos[2] >= (breedte-10) or (pos[0] ) <= 10:
                    self.vx *= -1
                if pos[3] >= (hoogte-40) or (pos[1]) <= 10:
                    self.vy *= -1

            def update_beweging(self,t):
                mijnCanvas.move(self.vorm, self.vx, self.vy)
                self.xpos += abs(self.vx * t)
                self.ypos += abs(self.vy * t)
                while gebruiker_invoer4.get() == 1:
                    bol_list[4].massa = 1000
                    bol_list[4].size == 100
                    bol_list[4].kleur = 'blue'
                    bol_list[4].xpos = 300
                    bol_list[4].ypos = 300
                    break 
                

        bol_list = []
        #Functie om de positie vector tussen 2 bollen te bepalen:
        def afstand(x1, y1, x2, y2):
            dist_x = (x2 - x1)
            dist_y = (y2 - y1)
            return dist_x, dist_y

        #functie om de snelheid van een bol te bepalen onder invloed van zwaartekracht:
        def zwaartekracht(m1,m2, rx, ry, velx , vely, t):
      	    #   F = G.(m1xm2)/r^2 (Newton universele zwaartkracht)
            #   a^2+b^2 = c^2 (driekhoeksvergelijing)
            #   F = m x a (waar a is de zwaartekrachtversnelling)
            #   v = a x delta(t)

            G = 3.8
            G = float(gebruiker_invoer3)
            soft = 0.001
            r = np.sqrt((rx**2) + (ry **2))
            Fx = (G * m1 * m2 * rx)/(soft + r **2)
            Fy = (G * m1 * m2 * ry)/(soft + r **2)
            gx = Fx/m1
            gy = Fy/m1    
            velx = gx * t
            vely = gy * t      
            return [velx, vely]

        # main - scherm2
        for i in range(80):
            bol_list.append(Bol('white'))
        for j in range(20):
            bol_list.append(Bol('red'))
        radx = []
        rady = []

        while True:
            global t
            t=0.001
            for bol1 in bol_list:
                dx =[]
                dy= []
                bol1.update_zijkanten()
                for bol2 in bol_list:
                    if bol1 != bol2:
                        drx, dry = afstand(bol1.xpos, bol1.ypos, bol2.xpos, bol2.ypos)
                        velx,vely = zwaartekracht(bol1.massa,bol2.massa, drx, dry, bol1.vx, bol1.vy, t)
                        dx.append(velx)
                        dy.append(vely)
 
                radx.append(sum(dx))
                rady.append(sum(dy))

                bol1.vx += radx[bol_list.index(bol1)]
                bol1.vy += rady[bol_list.index(bol1)]
                    
                bol1.update_beweging(t)

            self.frame.update()    
                

    def close_windows(self):
        bol_list = []
        self.master.destroy()

#https://stackoverflow.com/questions/60101910/python-tkinter-bouncing-ball-game
def main(): 
    root = tk.Tk()
    app = Scherm1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
