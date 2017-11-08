#GUI ex
from tkinter import *
def windowEx():
      window=Tk()
      window.title('Main Window')
      window.geometry('200x200')   #가로x세로 widthxheight
      window.resizable(width=FALSE,height=FALSE)#윈도우 크기 조절 불가
      window.mainloop()

def windowEx2():
      window=Tk()
      def eventExitButton():
            label3.config(text='click exit button')
            quit()
      window.title('Widget Test')
      window.geometry('200x400')   #가로x세로 widthxheight
      #window.resizable(width=FALSE,height=FALSE)#윈도우 크기 조절 불가
      label1=Label(window,text='Python GUI')
      label2=Label(window,text='Python ',font=('Bradley Hand ITC',30),fg='blue')  #bradley Hand ITC는 글씨체 fg는 글꼴색 foreground
      label3=Label(window,text='GUI',bg='magenta',width=10,height=5,anchor=CENTER,font=('Bradley Hand ITC',20),fg='yellow') #anchor는 정렬방
      exitbutton=Button(window,text='Exit',fg='blue',width=10,height=3,font=('italic',15),command=eventExitButton)
      label1.pack()
      label2.pack()
      label3.pack()
      exitbutton.pack()

      
      window.mainloop()
class Application(Frame):  #widow라고 보면 됨. 윈도우 하나
      def __init__(self, master=None): #master는 프레임 윈도우? application윈도우에 내부적으로 전달 받는 frame에 대한? Tk객체의 레퍼런스
            super().__init__(master)
            self.pack()
            self.create_widgets(master) #버튼 생성
      def create_widgets(self,master):  #생성자에서 버튼 두개를 직접 생성해줘도 됨
            self.hi_there=Button(self)
            self.hi_there["text"]="Hello World\n(Click me)"
            self.hi_there["command"]=self.say_hi
            self.hi_there.pack(side="top")

            self.quit=Button(self,text="QUIT",fg="red",command=master.destroy)
            self.quit.pack(side="bottom")
      def say_hi(self):
            print("hi there, everyone!")
def windowEx3():
      root=Tk()
      root.title('Widget Test')
      root.geometry('400x200')
     # root.resizable(width=FALSE, height=FALSE)

      app=Application(master=root)
      app.mainloop()

def windowEx4():
      root=Tk()
      root.title('Widget Test')
      root.geometry('400x200')
      #root.resizable(width=FALSE, height=FALSE)
      
      button1=Button(root,text='Button1',width=10,height=3)
      button2=Button(root,text='Button2',width=10,height=3)
      button3=Button(root,text='Button3',width=10,height=3)
      button1.pack(side=LEFT)
      button2.pack(side=LEFT)
      button3.pack(side=LEFT)
      #버튼을 세개 연속해서 나란히 배치
      btnList=[None]*3
      for i in range(4, 7):
            btnList[i-4]=Button(root,text='Buttttttton'+str(i))  #List확인해서 리스트에 담아서 pack() 해도 
      for btn in btnList:
            btn.pack(side=BOTTOM,fill=X,padx=10, pady=10,ipadx=10,ipady=10)
            #TOP하면 위에서 아래로 BOTTOM하면 아래에서 위로 생김 BOTTOM - 4가 제일 밑 그리고 6이 제일 위  fill=X는 채우기 하는거 윈도우에서 남은공간 채우기
            #pad x, pad y는 버튼(위젯)과 버튼 사이 간격 생김.
            #ipad x, ipad y는 위젯 내부()  width랑 height는 고정크기 ipad는 상대적으로 간격값 주는거.
            #GUI위젯 방식에 에디터가 없기 떄문에 이런식으로 다 맞춰줘야함 
      root.mainloop() 


def windowEx5():
      root=Tk()
      root.title('Widget Test')
      root.geometry('400x200')

      def event(ev):
            label.config(text=entry.get())
      label=Label(root, text='Input Text')
      label.pack(side=LEFT)

      entry=Entry(root)
      entry.pack(side=LEFT)
      entry.bind('<Return>',event)   #bind - 엔터키가 눌렀을 때 callback
      #입력하고 엔터 치면 label 값이 바뀜
      #<Button-1> 마우스 왼쪽 버튼 클릭
      #<Button-2> 마우스 중간 버튼 클릭
      #<Button-3> 마우스 오른쪽 버튼 클릭
      #<Double-Button-1> 왼쪽 버튼 더블클릭
      #<Return> Enter 키 눌려짐
      #<Key> 키가 눌려짐

      def func1():
            label2.config(text='Radio1')
            rb1.config(text='r1')
            print(rb1.get())
      def func2():
            label2.config(text='Radio2')
   #   def func3():
   #         if sel==1:
   #               print('Radio1')
   #         else sel==2:
   #               print('Radio2')             #지금은 안됨 sel변수를 꺼내는 과정이 필요한데 알아봐야함
      sel=IntVar()
      sel.set(1)
      label2=Label(root,text='Select Button')
      label2.pack(side=TOP)
      rb1=Radiobutton(root,text='Radio1',variable=sel,value=1,command=func1)
      rb2=Radiobutton(root,text='Radio2',variable=sel,value=2,command=func2)
      rb1.pack(side=TOP)
      rb2.pack(side=TOP)
      
      
      root.mainloop()
      
if __name__=='__main__':
      windowEx5()
