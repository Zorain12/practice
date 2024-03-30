## Zorain Bin khalid###
### 2019-MC-41 #### 
from tkinter import*
import random
from tkinter import messagebox
import datetime,csv
class Block:
    def __init__(self):
        self.root=Tk()
        self.root.title('Memory Block')               ### Title of game ###
        self.root.geometry("500x550")                 ### Geometry ###      
        self.root.configure(background='black')       ### Background color ###
        self.a=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
        random.shuffle(self.a)
        self.count=0
        self.ans_dict={}
        self.ans_list=[]
        self.window1()
### Buttons for first Window ###
    def window1(self):
        newEntryButton=Button(self.root,text='Play Game',command=self.window2,font=("Helvetica",15),bg='green')  
        newEntryButton.place(x = 130, y = 270, width=250, height=60)
        z=Label(self.root,text='Player Name:2019-MC-41',font=("Helvetica",15),bg='olive')
        z.place(x = 130, y = 200, width=250, height=65)
        r=Label(self.root,text='Game Name:Memory Block',font=("Helvetica",15),bg='peru')
        r.place(x = 130, y = 150, width=250, height=60)
        self.move=0 
### Function for 2nd window #### 
    def window2(self):
        self.root.withdraw()
        self.root1=Toplevel()
        self.root1.title('Memory Block')
        self.root1.geometry("500x550")
        self.root1.configure(background='black')
        self.f=0
        top_frame=Frame(self.root1)
        top_frame.pack(pady=50)
        #####  Grid Buttons #####
        b0=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b0,0))
        b0.grid(row=0,column=0)

        b1=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b1,1))
        b1.grid(row=0,column=1)

        b2=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b2,2))
        b2.grid(row=0,column=2)

        b3=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b3,3))
        b3.grid(row=0,column=3)

        b4=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b4,4))
        b4.grid(row=1,column=0)

        b5=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b5,5))
        b5.grid(row=1,column=1)

        b6=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b6,6))
        b6.grid(row=1,column=2)

        b7=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b7,7))
        b7.grid(row=1,column=3)

        b8=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b8,8))
        b8.grid(row=2,column=0)

        b9=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b9,9))
        b9.grid(row=2,column=1)

        b10=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b10,10))
        b10.grid(row=2,column=2)

        b11=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b11,11))
        b11.grid(row=2,column=3)

        b12=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b12,12))
        b12.grid(row=3,column=0)

        b13=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b13,13))
        b13.grid(row=3,column=1)

        b14=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b14,14))
        b14.grid(row=3,column=2)

        b15=Button(top_frame,text=' ',fg=('black'),bg='dark green',height=3,width=8,font=("Helvetica",15),command=lambda: self.Button_click(b15,15))
        b15.grid(row=3,column=3)
        self.my_label=Label(self.root1,text="Memory block",fg=('black'),bg='light green',font=("Helvetica",15))
        self.my_label.place(x = 180, y = 445,width=150,height=70)
### Function for clicking buttons ####    
    def Button_click(self,button,number):
        if button['text']==' ' and self.count<2:
            button['text']=self.a[number]
            # add number in ans list
            self.ans_list.append(number)
            # add number in ans dict
            self.ans_dict[button]=self.a[number]
            self.count+=1
            if len(self.ans_list)==2:
                self.move+=1
                if self.a[self.ans_list[0]]==self.a[self.ans_list[1]]:
                    self.my_label.config(text="match")
                    self.count=0
                    self.ans_list=[]
                    self.ans_dict={}
                    if self.my_label["text"]=="match":
                        self.f+=1
                        self.nick()
                else:
                    self.my_label.config(text="Not match")
                    self.count=0
                    self.ans_list=[]
                    messagebox.showinfo("wrong","wrong")
                    for key in self.ans_dict:
                        key['text']=" "
                    self.ans_dict={} 
### Function for 3rd window ####                           
    def window3(self):                    
        self.root1.destroy()
        self.root2=Toplevel()
        self.root2.title('Memory Block')
        self.root2.geometry("500x550")
        self.root2.configure(background='black')
        self.root2.protocol("WM_DELETE_WINDOW",self.exitgame2)
        self.time=datetime.datetime.now()
        with open("highscore.csv","a", newline="") as f:
                o = csv.writer(f)
                o.writerow([str(self.time),str(self.move)])
        j=Label(self.root2,text="Congratulations for Winner",font=("Helvetica",15),bg='darkmagenta')
        j.place(x = 80, y = 150, width=350, height=70)
        t=Button(self.root2,text='Play again',font=("Helvetica",15),bg='cornflowerblue',command=self.again)
        t.place(x = 130, y = 300, width=250, height=70)
        w=Button(self.root2,text='Check: High score',font=("Helvetica",15),bg='slategrey',command=self.scores)
        w.place(x = 130, y = 230, width=250, height=65)
    def nick(self):
        if self.f==8:
            self.window3()
    def scores(self):
        with open("highscore.csv","r",newline="") as f:
            List_1=list(csv.reader(f))
            List_3=[i[1] for i in  List_1]  
            high_score=min(List_3)
        m=Label(self.root2,text=(f'The best Score is : {high_score}'),font=("Helvetica",15),bg='aqua')
        m.place(x =70, y = 450, width=380, height=30) 
    def again(self):
        self.root2.destroy()
        self.move=0   
        self.window2()
    def exitgame1(self):
        self.root1.destroy()
        exit()
    def exitgame2(self):
        self.root2.destroy()
        exit()   
first=Block()   
mainloop()