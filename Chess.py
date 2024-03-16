from tkinter import *
import sys
import winsound
import asyncio
tk = Tk()
tk.title('Chess')
tk.iconbitmap(default='C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\pedone.ico')
import time
tk.wm_attributes('-topmost',1)
tk.resizable(0,0)
canvas = Canvas(tk,width = 480,height = 480)
c = -1
turn = 1
pezzi = []
pd = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
canvas.pack()
class bg():
    def __init__(self):
        self.canvas = canvas
        self.wh = PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\wh.gif')
        self.b = PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\n.gif')
        self.bw = self.b.width()
        self.bh = self.b.height()
        for a in range(0,8):
            for b in range(0,8):
                global c
                c = c + 1
                if((c % 2) == 0):
                    pezzi.append([self.bw * b,self.bh * a])
                    self.canvas.create_image(self.bw * b,self.bh * a,image = self.wh,anchor = 'nw')
                else:
                    pezzi.append([self.bw * b,self.bh * a])
                    self.canvas.create_image(self.bw * b,self.bh * a,image = self.b,anchor = 'nw')
            c = c - 1
class piece(bg):
    def __init__(self):
        self.pimg = [[PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\pedone.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\pedone_nero.gif')], \
                      [PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\re.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\re_nero.gif')], \
                      [PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\regina.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\regina_nera.gif')], \
                      [PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\torre.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\torre_nera.gif')], \
                      [PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\alfiere.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\alfiere_nero.gif')], \
                      [PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\cavallo.gif'),PhotoImage(file = 'C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\Python312\\cavallo_nero.gif')]]
        self.bianchi = \
        [canvas.create_image(pezzi[48][0] + 10,pezzi[48][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[49][0] + 10,pezzi[49][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[50][0] + 10,pezzi[50][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[51][0] + 10,pezzi[51][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[52][0] + 10,pezzi[52][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[53][0] + 10,pezzi[53][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[54][0] + 10,pezzi[54][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[55][0] + 10,pezzi[55][1] + 7,image = self.pimg[0][0], anchor = 'nw'), \
         canvas.create_image(pezzi[56][0] + 10,pezzi[56][1] + 7,image = self.pimg[3][0], anchor = 'nw'), \
         canvas.create_image(pezzi[57][0] + 10,pezzi[57][1] + 7,image = self.pimg[5][0], anchor = 'nw'), \
         canvas.create_image(pezzi[58][0] + 10,pezzi[58][1] + 7,image = self.pimg[4][0], anchor = 'nw'), \
         canvas.create_image(pezzi[59][0] + 10,pezzi[59][1] + 7,image = self.pimg[2][0], anchor = 'nw'), \
         canvas.create_image(pezzi[60][0] + 10,pezzi[61][1] + 7,image = self.pimg[1][0], anchor = 'nw'), \
         canvas.create_image(pezzi[61][0] + 10,pezzi[63][1] + 7,image = self.pimg[4][0], anchor = 'nw'), \
         canvas.create_image(pezzi[62][0] + 10,pezzi[63][1] + 7,image = self.pimg[5][0], anchor = 'nw'), \
         canvas.create_image(pezzi[63][0] + 10,pezzi[63][1] + 7,image = self.pimg[3][0], anchor = 'nw'), \
            ]
        self.neri = \
        [canvas.create_image(pezzi[8][0] + 10,pezzi[8][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[9][0] + 10,pezzi[9][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[10][0] + 10,pezzi[10][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[11][0] + 10,pezzi[11][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[12][0] + 10,pezzi[12][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[13][0] + 10,pezzi[13][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[14][0] + 10,pezzi[14][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[15][0] + 10,pezzi[15][1] + 7,image = self.pimg[0][1], anchor = 'nw'), \
         canvas.create_image(pezzi[0][0] + 10,pezzi[0][1] + 7,image = self.pimg[3][1], anchor = 'nw'), \
         canvas.create_image(pezzi[1][0] + 10,pezzi[1][1] + 7,image = self.pimg[5][1], anchor = 'nw'), \
         canvas.create_image(pezzi[2][0] + 10,pezzi[2][1] + 7,image = self.pimg[4][1], anchor = 'nw'), \
         canvas.create_image(pezzi[3][0] + 10,pezzi[3][1] + 7,image = self.pimg[2][1], anchor = 'nw'), \
         canvas.create_image(pezzi[4][0] + 10,pezzi[4][1] + 7,image = self.pimg[1][1], anchor = 'nw'), \
         canvas.create_image(pezzi[5][0] + 10,pezzi[5][1] + 7,image = self.pimg[4][1], anchor = 'nw'), \
         canvas.create_image(pezzi[6][0] + 10,pezzi[6][1] + 7,image = self.pimg[5][1], anchor = 'nw'), \
         canvas.create_image(pezzi[7][0] + 10,pezzi[7][1] + 7,image = self.pimg[3][1], anchor = 'nw'), \
            ]
class move(piece):
    def __init__(self):
        pass
    def istpiece(self,d,pk = '😊',wt = False):
       l = 0
       if pk == '😊':
           for k in range(65,97):
            if canvas.coords(k)[0] >= pezzi[d][0] and canvas.coords(k)[1] >= pezzi[d][1] and canvas.coords(k)[0] < (pezzi[d][0] + 60) and canvas.coords(k)[1] < (pezzi[d][1] + 60):
                if wt == False:
                    return True
                else:
                    return k
       elif pk == 'b':
           for k in range(65,81):
            if canvas.coords(k)[0] >= pezzi[d][0] and canvas.coords(k)[1] >= pezzi[d][1] and canvas.coords(k)[0] < (pezzi[d][0] + 60) and canvas.coords(k)[1] < (pezzi[d][1] + 60):
                if wt == False:
                    return True
                else:
                    return k  
       elif pk == 'n':
           for k in range(80,97):
            if canvas.coords(k)[0] >= pezzi[d][0] and canvas.coords(k)[1] >= pezzi[d][1] and canvas.coords(k)[0] < (pezzi[d][0] + 60) and canvas.coords(k)[1] < (pezzi[d][1] + 60):
                if wt == False:
                    return True
                else:
                    return k
       return False
    def calc(self,evt):
        x = evt.x
        y = evt.y
        print(f'{x},{y}')
        for n in range(0,64):
            if x >= pezzi[n][0] and y >= pezzi[n][1] and x < (pezzi[n][0] + 60) and y < (pezzi[n][1] + 60):
              s.info = 1
              self.move(n,bianco)
    def move(self,list,b):
        global turn
        turn = 1 - turn
        l = b[3]
        l1 = l - 1
        n1 = l + 1
        l8 = l - 8
        l7 = l - 7
        l9 = l - 9
        n8 = l + 8
        n7 = l + 7
        n9 = l + 9
        l16 = l - 16
        n16 = l + 16
        if turn == 0:
            pezz = bianco[1]
            lezz = bianco[0]
        else:
            pezz = nero[1]
            lezz = nero[0]
        if (pezz == 'pedone'):
            if turn == 0:
                if   l8 == list and self.istpiece(l8) == False:
                    #def ol():
                     #winsound.PlaySound('C:\\Users\\pietr\\AppData\\Local\\Programs\\Python\\m.wav',0)
                    #ol()
                    for b in range(1,16):
                     canvas.move(lezz,0,-4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[bianco[0]] = False
                elif  l7 == list and self.istpiece(l7,'n',True) != False:
                    canvas.itemconfig(self.istpiece(l7,'n',True),state = 'hidden')
                    canvas.move(self.istpiece(l7,'n',True),800,800)
                    for b in range(1,16):
                     canvas.move(lezz,4,-4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[bianco[0]] = False
                elif  l9 == list and self.istpiece(l9,'n',True) != False:
                    canvas.itemconfig(self.istpiece(l9,'n',True),state = 'hidden')
                    canvas.move(self.istpiece(l9,'n',True),800,800)
                    for b in range(1,16):
                     canvas.move(lezz,-4,-4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[bianco[0]] = False
                elif l16 ==  list and self.istpiece(l16) == False and self.istpiece(l8) == False and pd[bianco[0]] == True:
                    for b in range(1,16):
                     canvas.move(lezz,0,-8)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[bianco[0]] = False
                else:
                    turn = 1 - turn
            else:
                if   n8 == list and self.istpiece(n8) == False:
                    for b in range(1,16):
                     canvas.move(lezz,0,4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[nero[0]] = False
                elif  n7 == list and self.istpiece(n7,'b',True) != False:
                    canvas.itemconfig(self.istpiece(n7,'b',True),state = 'hidden')
                    canvas.move(self.istpiece(n7,'b',True),800,800)
                    for b in range(1,16):
                     canvas.move(lezz,-4,4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[nero[0]] = False
                elif  n9 == list and self.istpiece(n9,'b',True) != False:
                    canvas.itemconfig(self.istpiece(n9,'b',True),state = 'hidden')
                    canvas.move(self.istpiece(n9,'b',True),800,800)
                    for b in range(1,16):
                     canvas.move(lezz,4,4)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01) 
                    pd[bianco[0]] = False 
                elif n16 == list and self.istpiece(n16) == False and pd[nero[0]] and self.istpiece(n8) == False:
                    for b in range(1,16):
                     canvas.move(lezz,0,8)
                     tk.update_idletasks()
                     tk.update()
                     time.sleep(0.01)
                    pd[nero[0]] = False
                else:
                    turn = 1 - turn
        elif (pezz == 'alfiere'):
            lop = 0
            d = l - 7
            for c in range(65,97):
              if canvas.coords(lezz)[0] > pezzi[c][0] and canvas.coords(lezz)[1] > pezzi[c][1] and canvas.coords(lezz)[0] < (pezzi[c][0] + 60) and canvas.coords(lezz)[1] < (pezzi[c][0] + 60):
                lop = c
                break
            pass
        elif (pezz == 'cavallo'):
            c1 = l - 17
            c2 = l - 15
            c3 = l - 6
            c4 = l - 10
            c5 = l + 17
            c6 = l + 15
            c7 = l + 6
            c8 = l  + 10
            if turn == 0:
                if c1 == list:
                    if self.istpiece(c1) == False:
                     for b in range(1,16):
                      canvas.move(lezz,0,-8)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                     for b in range(1,16):
                      canvas.move(lezz,-4,0)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(c1,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c1,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c1,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c2 == list:
                    if self.istpiece(c2) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,-8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c2,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c2,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c2,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c3 == list:
                    if self.istpiece(c3) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c3,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c3,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c3,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c4 == list:
                    if self.istpiece(c4) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c4,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c4,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c4,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c5 == list:
                    if self.istpiece(c5) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c5,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c5,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c5,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c6 == list:
                    if self.istpiece(c6) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,8)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c6,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c6,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c6,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c7 == list:
                    if self.istpiece(c7) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c7,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c7,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c7,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,-8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif c8 == list:
                    if self.istpiece(c8) == False:
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                    else:
                     if self.istpiece(c8,'n',True) != False:
                      canvas.itemconfig(self.istpiece(c8,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(c8,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                      for b in range(1,16):
                       canvas.move(lezz,8,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn       
                else:
                   turn = 1 - turn
        elif (pezz == 're'):
            if turn == 0:
                if l8 == list:
                    if self.istpiece(l8) == False:
                     for b in range(1,16):
                      canvas.move(lezz,0,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l8,'n',True) != False:
                      canvas.itemconfig(self.istpiece(l8,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(l8,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif l9 == list:
                    if self.istpiece(l9) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l9,'n',True) != False:
                      canvas.itemconfig(self.istpiece(l9,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(l9,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,-4)
                       tk.update_idletasks()
                       tk.update()     
                       time.sleep(0.01) 
                     else:
                       turn = 1 - turn
                elif l7 == list:
                    if self.istpiece(l7) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l7,'n',True) != False:
                      canvas.itemconfig(self.istpiece(l7,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(l7,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n8 == list:
                    if self.istpiece(n8) == False:
                     for b in range(1,16):
                      canvas.move(lezz,0,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n8,'n',True) != False:
                      canvas.itemconfig(self.istpiece(n8,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(n8,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n9 == list:
                    if self.istpiece(n9) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n9,'n',True) != False:
                      canvas.itemconfig(self.istpiece(n9,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(n9,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,4)
                       tk.update_idletasks()
                       tk.update()     
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n7 == list:
                    if self.istpiece(n7) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n7,'n',True) != False:
                      canvas.itemconfig(self.istpiece(n7,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(n7,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif l1 == list:
                    if self.istpiece(l1) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,0)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l1,'n',True) != False:
                      canvas.itemconfig(self.istpiece(l1,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(l1,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n1 == list:
                    if self.istpiece(n1) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,0)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n1,'n',True) != False:
                      canvas.itemconfig(self.istpiece(n1,'n',True),state = 'hidden')
                      canvas.move(self.istpiece(n1,'n',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01) 
                     else:
                       turn = 1 - turn              
                else:
                   turn = 1 - turn
            else:
                if n8 == list:
                    if self.istpiece(n8) == False:
                     for b in range(1,16):
                      canvas.move(lezz,0,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n8,'b',True) != False:
                      canvas.itemconfig(self.istpiece(n8,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(n8,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n9 == list:
                    if self.istpiece(n9) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n9,'b',True) != False:
                      canvas.itemconfig(self.istpiece(n9,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(n9,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,4)
                       tk.update_idletasks()
                       tk.update()     
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn 
                elif n7 == list:
                    if self.istpiece(n7) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n7,'b',True) != False:
                      canvas.itemconfig(self.istpiece(n7,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(n7,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif l9 == list:
                    if self.istpiece(l9) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l9,'b',True) != False:
                      canvas.itemconfig(self.istpiece(l9,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(l9,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,-4)
                       tk.update_idletasks()
                       tk.update()     
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn 
                elif l7 == list:
                    if self.istpiece(l7) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l7,'b',True) != False:
                      canvas.itemconfig(self.istpiece(l7,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(l7,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif l8 == list:
                    if self.istpiece(l8) == False:
                     for b in range(1,16):
                      canvas.move(lezz,0,-4)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l8,'b',True) != False:
                      canvas.itemconfig(self.istpiece(l8,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(l8,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,0,-4)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif l1 == list:
                    if self.istpiece(l1) == False:
                     for b in range(1,16):
                      canvas.move(lezz,-4,0)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(l1,'b',True) != False:
                      canvas.itemconfig(self.istpiece(l1,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(l1,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,-4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn
                elif n1 == list:
                    if self.istpiece(n1) == False:
                     for b in range(1,16):
                      canvas.move(lezz,4,0)
                      tk.update_idletasks()
                      tk.update()
                      time.sleep(0.01)
                    else:
                     if self.istpiece(n1,'b',True) != False:
                      canvas.itemconfig(self.istpiece(n1,'b',True),state = 'hidden')
                      canvas.move(self.istpiece(n1,'b',True),800,800)
                      for b in range(1,16):
                       canvas.move(lezz,4,0)
                       tk.update_idletasks()
                       tk.update()
                       time.sleep(0.01)
                     else:
                       turn = 1 - turn 
                else:
                   turn = 1 - turn
        elif (pezz == 'regina'):
            pass
        elif (pezz == 'torre'):
          global lopp
          global pollo
          lopp = 0
          if turn == 0:
            lopp = bianco[3]
            lk = bianco[0]
          else:
            lopp = nero[3]
            lk = bianco[0]
          pollo = 2
          if turn == 0:
            pollo = (lopp % 8)
          else:
            pollo = (lopp % 8)
          pillo =  7 - pollo
          pillo = pillo + 2
          pollo = pollo + 2
          if turn == 0:
            pello = divmod(bianco[3],8)[0]
          else:
            pello = divmod(nero[3],8)[0]
          pello = pello + 2
          pallo = 7 - (pello - 2)
          for v in range(1,pollo):
            if pollo == 1:
                break
            if (lopp - (v - 1)) == list:
                    if self.istpiece((lopp - (v - 1))) == False:
                      for a in range(1,v):
                        for b in range(1,6):
                         canvas.move(lk,-12,0)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                    else:
                     if self.istpiece((lopp - (v - 1)),'n',True) != False:
                      canvas.itemconfig(self.istpiece((lopp - (v - 1)),'n',True),state = 'hidden')
                      canvas.move(self.istpiece((lopp - (v - 1)),'n',True),800,800)
                      for a in range(1,v):
                        for b in range(1,6):
                         canvas.move(lk,-12,0)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                     else:
                       turn = 1 - turn
          for a in range(1,pillo):
            if (lopp + (a - 1)) == list:
                    if self.istpiece((lopp - (a - 1))) == False:
                      for a in range(1,a):
                        for b in range(1,6):
                         canvas.move(lk,12,0)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                    else:
                     if self.istpiece((lopp - (a - 1)),'n',True) != False:
                      canvas.itemconfig(self.istpiece((lopp - (a - 1)),'n',True),state = 'hidden')
                      canvas.move(self.istpiece((lopp - (a - 1)),'n',True),800,800)
                      for a in range(1,a):
                        for b in range(1,6):
                         canvas.move(lk,12,0)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                     else:
                       turn = 1 - turn 
          for n in range(1,pello):
            if (lopp - (8 * (n - 1))) == list:
                    if self.istpiece((lopp - (8 * (n - 1)))) == False:
                      for a in range(1,n):
                        for b in range(1,6):
                         canvas.move(lk,0,-12)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                    else:
                     if self.istpiece((lopp - (8 * (n - 1))),'n',True) != False:
                      canvas.itemconfig(self.istpiece((lopp - (8 * (n - 1))),'n',True),state = 'hidden')
                      canvas.move(self.istpiece((lopp - (8 * (n - 1))),'n',True),800,800)
                      for a in range(1,n):
                        for b in range(1,6):
                         canvas.move(lk,0,-12)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                     else:
                       turn = 1 - turn
          for s in range(1,pallo):
            if (lopp +  (8 * (s - 1))) == list:
                    if self.istpiece((lopp + (8 * (s - 1)))) == False:
                      for a in range(1,s):
                        for b in range(1,6):
                         canvas.move(lk,0,12)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                    else:
                     if self.istpiece((lopp + (8 * (s - 1))),'n',True) != False:
                      canvas.itemconfig(self.istpiece((lopp + (8 * (s - 1))),'n',True),state = 'hidden')
                      canvas.move(self.istpiece((lopp + (8 * (s - 1))),'n',True),800,800)
                      for a in range(1,s):
                        for b in range(1,6):
                         canvas.move(lk,0,12)
                         tk.update_idletasks()
                         tk.update()
                         time.sleep(0.01)
                     else:
                       turn = 1 - turn
class selection(move):
    def __init__(self):
        self.info = 1
        global nero
        nero = [1,1,1,1]
        global bianco
        bianco = [1,1,1,1]
    def call(self,evt):
      self.g = 0
      self.x = evt.x
      self.y = evt.y
      for m in range(0,64):
            if self.x >= pezzi[m][0] and self.y >= pezzi[m][1] and self.x < (pezzi[m][0] + 60) and self.y < (pezzi[m][1] + 60):
                bianco[3] = m
                nero[3] = m
      for d in range(65,81):
          ciao = canvas.coords(d)
          if self.y >= ciao[1] and self.y <= ciao[1] + 40 and self.x >= ciao[0] and self.x <= ciao[0] + 48:
              if (d >= 65 and d <= 72):
                  bianco[0] = d
                  bianco[1] = 'pedone'
                  bianco[2] = 'bianco'
                  self.g = 1
              elif (d == 73 or d == 80):
                  bianco[0] = d
                  bianco[1] = 'torre'
                  bianco[2] = 'bianco'
                  self.g = 1
              elif (d == 74 or d == 79):
                  bianco[0] = d
                  bianco[1] = 'cavallo'
                  bianco[2] = 'bianco'
                  self.g = 1
              elif (d == 75 or d == 78):
                  bianco[0] = d
                  bianco[1] = 'alfiere'
                  bianco[2] = 'bianco'
                  self.g = 1
              elif (d == 76):
                  bianco[0] = d
                  bianco[1] = 'regina'
                  bianco[2] = 'bianco'
                  self.g = 1
              else:
                  bianco[0] = d
                  bianco[1] = 're'
                  bianco[2] = 'bianco'
                  self.g = 1
              if self.g == 1:
               self.g = 0
               self.info = 0
      for c in range(81,97):
          ciao = canvas.coords(c)
          if self.y >= ciao[1] and self.y <= ciao[1] + 40 and self.x >= ciao[0] and self.x <= ciao[0] + 48:
              if (c >= 81 and c <= 88):
                  nero[0] = c
                  nero[1] = 'pedone'
                  nero[2] = 'nero'
                  self.g = 1
              elif (c == 89 or c == 96):
                  nero[0] = c
                  nero[1] = 'torre'
                  nero[2] = 'nero'
                  self.g = 1
              elif (c == 90 or c == 95):
                  nero[0] = c
                  nero[1] = 'cavallo'
                  nero[2] = 'nero'
                  self.g = 1
              elif (c == 91 or c == 94):
                  nero[0] = c
                  nero[1] = 'alfiere'
                  nero[2] = 'nero'
                  self.g = 1                  
              elif (c == 92):
                  nero[0] = c
                  nero[1] = 'regina'
                  nero[2] = 'nero'
                  self.g = 1                  
              else:
                  nero[0] = c
                  nero[1] = 're'
                  nero[2] = 'nero'
                  self.g = 1
              if self.g == 1:
               self.g = 0
               self.info = 0
      if turn == 1:
        print(bianco)
      else:
        print(nero)
g = bg()
s = selection()
p = piece()
m = move()
print(pezzi)
print(p.bianchi)
print(p.neri)
#for b in range(1,6):
                         #canvas.move(73,24,-24)
                         #tk.update_idletasks()
                         #tk.update()
                         #time.sleep(0.01)
tk.update_idletasks()
tk.update()
while True:
    if s.info == 1:
     try:
         canvas.bind_all('<Button-1>',s.call)
     except:
        sys.exit()
    else:
     try:
         canvas.bind_all('<Button-1>',m.calc)
     except:
        sys.exit()         
    tk.update_idletasks()
    tk.update()
    time.sleep(0.1)