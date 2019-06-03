import os
import pickle,random
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
def reward(a):
   if if_win(a):
      if if_win(a)==1:
         return -1
      elif if_win(a)==2:
         return 1      
   if move_left(a)==0:
      return 0.5 
   else:
      return 0      
def move_left(a):
   for i in range(1,10):
      if a[i]==" ":
         return 1
   return 0            
def decision(a,check):
   print("\n")
   if if_win(a):
      if check%2==1:
         print("Player is win")
      else:
         print("Computer is win")
   else:
      print("Match is draw")   
def start_info():
   b=('Anything','1','2','3','4','5','6','7','8','9')
   print("\nYou starts with X")
   print_board(b)
   print("Press 1 to start game")
#main function begins 
if __name__ == "__main__":
   #print(a)
   start_info()
   start=int(input())
   if start==1:
      eps=0.0
      a=[" "]*10
      check=1
      try:
         fileobject=open("./pickle/values",'rb')
         values=pickle.load(fileobject)
         fileobject.close()
      except:
         print("Error in loading file\nTrain your code again!")
         os.exit(0)   
      number=0
      start0=0
      check=random.choice([0,1])
      if check==0:
         last=9
      else:
         last=10
      while check!=last:
         if move_left(a)==0:
            for i in range(1,10):
               values[number][i]=0
            break   
         if if_win(a)==1:
            break 
         if if_win(a)==2:
            break    
         ##comp/agent move
         moves=[i for i in range(1,10) if a[i]==" "]
         if check%2==0:
            if random.random()<0:
                move_index=random.choice(moves) 
            else:    
               move_indexes=[]
               temp=-150   
               for i in moves:
                  x=values[number][i]
                  if x>temp:
                     temp=x
                     move_indexes.clear()
                     move_indexes.append(i) 
                  elif x==temp:
                     move_indexes.append(i) 
               move_index=random.choice(move_indexes)              
            a[move_index]="O"  
            print(number,values[number])
            number+=2*3**(9-move_index)    
         #player move      
         elif check%2==1:
            print("\nWhich No. from 1-9 You want to choose?")
            x=int(input(''))
            if a[x]!=" ":
               print("\nIllegal Move")
               print_board(a)
               continue  
            a[x]="X" 
            print(number,values[number])
            #print(values[number][x])
            number=number+3**(9-x) 
         print_board(a)          
         check+=1   
      decision(a,check)
      fileobject=open("./pickle/values",'wb')
      pickle.dump(values,fileobject)
      fileobject.close()

            

