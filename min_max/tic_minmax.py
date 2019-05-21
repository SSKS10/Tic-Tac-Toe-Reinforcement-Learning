import os,random
import pickle
def print_board(a):
   print("\n")
   print("-------------")
   for i in range(1,4):
        print("| "+a[3*i-2]+" | "+a[3*i-1]+" | "+a[3*i]+" |")
        print("-------------")
        
def if_win(a):
   if a[1]=="X" and ((a[2]=="X" and a[3]=="X") or (a[4]=="X" and a[7]=="X") or (a[5]=="X" and a[9]=="X")):
      return 1
   elif a[1]=="O" and ((a[2]=="O" and a[3]=="O") or (a[4]=="O" and a[7]=="O") or (a[5]=="O" and a[9]=="O")):
      return 2
   elif a[3]=="X" and ((a[6]=="X" and a[9]=="X") or (a[5]=="X" and a[7]=="X")):
      return 1
   elif a[3]=="O" and ((a[6]=="O" and a[9]=="O") or (a[5]=="O" and a[7]=="O")):
      return 2
   elif a[2]=="X" and a[5]=="X" and a[8]=="X":
      return 1
   elif a[2]=="O" and a[5]=="O" and a[8]=="O":
      return 2
   elif a[4]=="X" and a[5]=="X" and a[6]=="X":
      return 1
   elif a[4]=="O" and a[5]=="O" and a[6]=="O":
      return 2
   elif a[7]=="X" and a[8]=="X" and a[9]=="X":
      return 1
   elif a[7]=="O" and a[8]=="O" and a[9]=="O":
      return 2
   else:
      return 0
def move_left(a):
   for i in range(1,10):
      if a[i]==" ":
         return 1
   return 0            
#first move by computer   
count=0   
def f_move(c,i):
   c[i]="O"
   return player_move(c)       
#computer move]
def comp_move(c):
   if if_win(c)==1:
      return -10
   if if_win(c)==2:
      return 10 
   if move_left(c)==0:
      return 0    
   score=-1000000000000    
   for i in range(1,10):
      if c[i]==" ":
         c[i]="O"
         score1=player_move(c)
         if score<score1:
            score=score1
         c[i]=" " 
   return score

def player_move(c):
   if if_win(c)==1:
      return -10
   if if_win(c)==2:
      return 10 
   if move_left(c)==0:
      return 0     
   score=1000000000   
   for i in range(1,10):
      if c[i]==" ":
         c[i]="X"
         score1=comp_move(c)
         if score>score1:
            score=score1
         c[i]=" " 
   return score 

#main function begins 
if __name__ == "__main__":
   b=('Anything','1','2','3','4','5','6','7','8','9')
   print("\nYou starts with X")
   print_board(b)
   print("Press 1 to start game")  
   start=int(input())
   if start==1:
      games=0
      fileobject=open("./values_minmax",'rb')
      values=pickle.load(fileobject)
      fileobject.close()
      while games<10000:
         #a=[' ', ' ', ' ', 'X', ' ', 'O', ' ', ' ', ' ', 'X']
         number=0
         a=[" "]*10
         c=a[:]
         check=
         while check!=10:
            score=-100
            x=[]
            if check%2==0:
               if len(values[number])!=0:
                  print(number,values[number])
                  y=random.choice(values[number])
               else:  
                  moves=[i for i in range(1,10) if a[i]==" "]
                  for i in moves:
                     c=a[:] 
                     score1=f_move(c,i)
                     c[i]=" "       
                     if score1>=score:
                        if score==score1:
                           x.append(i)
                        else:
                           x.clear()
                           x.append(i)
                        score=score1     
                  y=random.choice(x)         
                  values[number]=x                   
               a[y]="O"
               number=number+3**(9-y)
               c=a[:]
            elif check%2==1:
               print("\nWhich No. from 1-9 You want to choose?")
               moves=[i for i in range(1,10) if a[i]==" "]
               x=random.choice(moves)
               #print(x)
               if a[x]!=" ":
                  print("\nIllegal Move")
                  print_board(a)
                  continue 
               a[x]="X"
               number=number+2*3**(9-x)
               c=a[:]  
            print_board(a)
            if if_win(a):
               break;
            #print(check)
            check+=1   
         games+=1   
         print(games)
   print("\n\n\n")
   if if_win(a):
      if check%2==0:
         print("Player is win")
      else:
         print("Computer is win")

   else:
      print("Match is draw")
   x=int(input("Press 1 to exit\n"))
   fileobject=open("./values_minmax",'wb')
   pickle.dump(values,fileobject)
   fileobject.close()
   if x==1:
      exit()
      