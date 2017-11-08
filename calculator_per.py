class Calculator:
      def __init__(self,lis):
            self.tot=0
            self.lis=lis
      def sum(self):
            self.tot=sum(self.lis)
            print(self.tot)
      def avg(self):
            if self.tot!=0:
                  self.av=self.tot/len(self.lis)
            else:
                  self.av=sum(self.lis)/len(self.lis)
            print(self.av)

if __name__=='__main__':
      li=[]
      #li=[1,2,3,4,5]
      while True:
            num=int(input('enter num (0->end):'))
            if num==0:
                  break
            li.append(num)

      cal1=Calculator(li)
      cal1.sum()
      cal1.avg()
