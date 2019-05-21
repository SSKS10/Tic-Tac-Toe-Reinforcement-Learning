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
def move_left(a):
   for i in range(1,10):
      if a[i]==" ":
         return 1
   return 0    
def f_move(c,i):
   c[i]="X"
   return player_move(c)       
#computer move]
def comp_move(c):
   if if_win(c)==1:
      return 10
   if if_win(c)==2:
      return -10 
   if move_left(c)==0:
      return 0    
   score=-1000000000000    
   for i in range(1,10):
      if c[i]==" ":
         c[i]="X"
         score1=player_move(c)
         if score<score1:
            score=score1
         c[i]=" " 
   return score

def player_move(c):
   if if_win(c)==1:
      return 10
   if if_win(c)==2:
      return -10 
   if move_left(c)==0:
      return 0     
   score=1000000000   
   for i in range(1,10):
      if c[i]==" ":
         c[i]="O"
         score1=comp_move(c)
         if score>score1:
            score=score1
         c[i]=" " 
   return score 
        
def decision(a,check):
   print("\n")
   global count_player,count_bot
   if if_win(a):
      if check%2==1:
         print("Player is win")
         count_player+=1
      else:
         print("Computer is win")
         count_bot+=1
   else:
      print("Match is draw")   
def start_info():
   b=('Anything','1','2','3','4','5','6','7','8','9')
   print("\nYou starts with X")
   print_board(b)
   print("Press 1 to start game")
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

#main function begins 
if __name__ == "__main__":
   #print(a)
   count_player=0
   count_bot=0
   ans=[]
   start_info()
   eps=0.9
   start=int(input())
   if start==1:
      games=0
      fileobject=open("./values_minmax",'rb')
      min_max=pickle.load(fileobject)
      fileobject.close() 
      try:
         fileobject=open("./values",'rb')
         values=pickle.load(fileobject)
         fileobject.close() 
      except:
         fileobject=open("./values",'wb')
         actions=[" ","X","O"]
         a=[0]*10**6
         for i in range(10**6):
           a[i]=[0]*10
         pickle.dump(a,fileobject)
         fileobject.close()  
      while games<=10**5:
         a=[" "]*10
         number=0
         check=1
         start0=0
         temporary=0
         while check!=10:
            ##comp/agent move
            if move_left(a)==0:
               break   
            if if_win(a):
               break     
            moves=[i for i in range(1,10) if a[i]==" "]
            #############
            #comp move)
            if check%2==1:
               move_indexes=[]               
               if random.random()<0:
                   move_index=random.choice(moves) 
               else:    
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
               print(number,values[number])             
               maxi=-150  
               for i in range(1,10):
                  x=values[number+2*3**(9-move_index)][i]
                  if x>maxi:
                     maxi=x 
               a[move_index]="O"                  
               values[number][move_index]+=0.5*(reward(a)+0.9*maxi-values[number][move_index])
               temporary=move_index
               #print(number,move_index,values[number][move_index]) 
               number=number+2*3**(9-move_index)
            ############
            #player move     
            elif check%2==0:
               if random.random()<0:
                   move_index=random.choice(moves) 
               else:    
                  score=-150
                  move_indexes=[]
                  print(number,min_max[number])
                  if len(min_max[number])!=0:    
                      move_index=random.choice(min_max[number]) 
                  else:     
                     for i in range(1,10):
                        c=a[:]
                        if a[i]==" ": 
                           score1=f_move(c,i)
                           c[i]=" "       
                           if score1>=score:
                              if score1==score:
                                 move_indexes.append(i) 
                              else:
                                 move_indexes.clear()
                                 move_indexes.append(i)        
                              score=score1   
                     #print(move_indexes,score)  
                     min_max[number]=move_indexes      
                     move_index=random.choice(move_indexes)  
               a[move_index]="X"
               c=a[:]
               mini=150   
               for i in range(1,10):
                  x=values[number+3**(9-move_index)][i]
                  if x<mini:
                     mini=x                 
               values[number-2*3**(9-temporary)][temporary]+=0.5*(reward(a)+0.9*mini-values[number-2*3**(9-temporary)][temporary])
               print(number,values[number])
               number=number+3**(9-move_index)
            ###################              
            print_board(a)      
            check+=1 
         games+=1 
         print(games)
         if(games%10000==0):
            eps-=0.1
            ans.append([count_player,count_bot])    
         decision(a,check) 
      print(ans)
      fileobject=open("./values_minmax",'wb')
      pickle.dump(min_max,fileobject)
      fileobject.close()   
      fileobject=open("./values",'wb')
      pickle.dump(values,fileobject)
      fileobject.close()       
