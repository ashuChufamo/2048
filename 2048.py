import random
class entry:
    def __init__(self,matrix=[]):
        self.matrix=matrix
    def start (self):
        '''starts the first matrix with the 2 elements non 0'''
        size=eval(input('give size: '))
        for temp1 in range(size):
            temp1=[]
            for temp2 in range (size):
                temp2=0
                temp1.append(temp2)
            self.matrix.append(temp1)
        #to create the playing matrix with all 0s
        c=[]
        for i in range(len(self.matrix)):
            c+=[i]
        temp1=random.choice(c)
        temp2=random.choice(c)
        self.matrix[temp1][temp2]=2
        c=[]
        for i in range(len(self.matrix)):
            c+=[i]
        temp1=random.choice(c)
        temp2=random.choice(c)
        counter=0
        #to add 2 at random position where it is 0
        for i in self.matrix:
            for j in i:
                if j==0:
                    counter+=1
        while self.matrix[temp1][temp2] != 0 and counter!=0:
            we,rt=random.choice(c),random.choice(c)
        if counter!=0 and self.matrix[temp1][temp2]==0:
            self.matrix[temp1][temp2]=2
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(format(self.matrix[i][j],"6"),end="")
            print()
        #return the starting matrix
        
class play(entry):
    #inherits the matrix made by the entry class
    #move and add based on given command 
    def __init__(self,score=0):
        entry.__init__(self)
        self.score=score
        
    def left(self):
        '''adds and moves the numbers in the matrix to left'''
        t=[]
        for i in self.matrix:
            t+=[[]]
        #to initialize t equal to the length of the orginal matrix
        print()
        for yo in range(len(self.matrix)):
            i=self.matrix[yo]#to find each list in the matrix
            b=len(i)
            y=sum(i)
            j=[]
            p=0
            while p+1 < len(i):
                a=i[p]
                ctr=p+1
                while ctr<len(i) and i[ctr]==0:
                    ctr+=1#pass if 0
                if ctr < len(i):#if not 0 compare
                    if a==i[ctr]:
                        j.append(2*a)
                        self.score+=(2*a)#add 2*a to score
                        i.pop(ctr)   
                    elif a!=0:
                        j.append(a)
                elif ctr>=len(i):
                    if i[ctr-1]==0:
                        j.append(a)
                    elif comparisional==i[ctr-1]:
                        j.append(a*2)
                p=ctr
            if sum(j)!=y:#to add the last non-0 element,if not included
                k=-1
                while i[k]== 0:
                    k-=1
                j.append(i[k])
            for l in range(b-len(j)):#fill the rest with 0s
                j.append(0)
            t[yo]+=j
        c=[]
        for i in range(len(t)):#to add 2 at random position
            c+=[i]
        temp1=random.choice(c)
        temp2=random.choice(c)
        counter=0
        for i in t:
            for j in i:
                if j!=0:
                    counter+=1
        while t[temp1][temp2] != 0 and counter!=0:
            temp1,temp2=random.choice(c),random.choice(c)
        if counter!=0 and t[temp1][temp2]==0:
            t[temp1][temp2]=2
        self.matrix=t
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(format(self.matrix[i][j],"6"),end="")
            print()#print what we have now
        print("score =",self.score)

    def right(self):
        '''changes to left 
                  adds and moves the numbers in the matrix to left
                            changes back to right'''
        #to initialize t equal to the length of the orginal matrix
        t=[]
        for i in self.matrix:
            t+=[[]]
        self.n=self.matrix[::-1]#invert the matrix to left
        print()
        for yo in range(len(self.n)):
            i=self.matrix[yo]#to find each list
            b=len(i)
            y=sum(i)
            j=[]
            p=0
            i=i[::-1]#invert the matrix
            while p+1 < len(i):
                a=i[p]
                ctr=p+1
                while ctr<len(i) and i[ctr ]==0:
                    ctr+=1#pass if 0
                if ctr < len(i):#if not 0 compare
                    if a==i[ctr]:
                        j.append(2*a)
                        self.score+=(2*a)#add 2*a to score
                        i.pop(ctr)   
                    elif a!=0:
                        j.append(a)
                elif ctr>=len(i):
                    if i[ctr-1]==0:
                        j.append(a)
                    elif a==i[ctr-1]:
                        j.append(a*2)
                p=ctr
            if sum(j)!=y:#to add the last non-0 element,if not included
                k=-1
                while i[k]== 0:
                    k-=1
                j.append(i[k])
            for l in range(b-len(j)):
                j.append(0)#fill the rest with 0s
            j=j[::-1]#invert back
            t[yo]+=j
        t=t[::-1]#invert back the matrix
        self.matrix=t
        c=[]
        for i in range(len(t)):#add 2 at random position 
            c+=[i]
        we=random.choice(c)
        rt=random.choice(c)
        counter=0
        for i in t:
            for j in i:
                if j==0:
                    counter+=1
        while t[we][rt] != 0 and counter!=0:
            we,rt=random.choice(c),random.choice(c)
        if counter!=0 and t[we][rt]==0:
            t[we][rt]=2
        self.matrix=t
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(format(self.matrix[i][j],"6"),end="")
            print()#print what we have
        print("score =",self.score)
        
    def upward(self):
        '''changes to row
                 adds and moves the numbers in the matrix to left
                           inverts back to column'''
        t=[]
        for i in self.matrix:
            t+=[[]]
        print()
        for y in range(len(self.matrix)):
            i=[]
            for o in self.matrix:
                i+=[o[y]]#change the column to row
                
            d=sum(i)
            b=len(i)
            j=[]
            p=0
            while p+1 < len(i):
                a=i[p]#to find each list
                ctr=p+1
                while ctr<len(i) and i[ctr]==0:
                    ctr+=1#pass the 0s
                if ctr < len(i):#compare
                    if a==i[ctr]:
                        j.append(2*a)
                        self.score+=(2*a)#add 2*a to score
                        i.pop(ctr)   
                    elif a!=0:
                        j.append(a)
                elif ctr>=len(i):
                    if i[ctr-1]==0:
                        j.append(a)
                    elif a==i[ctr-1]:
                        j.append(a*2)
                p=ctr
            if sum(j)!=d:#to add the last non 0 element, in not included
                k=-1
                while i[k]== 0:
                    k-=1
                j.append(i[k])
            for l in range(b-len(j)):
                j.append(0)#fill the rest with 0s
            for ty in range(len(t)):
                t[ty].append(j[ty])#transpose the row back to column
        c=[]
        for i in range(len(t)):
            c+=[i]
        we=random.choice(c)
        rt=random.choice(c)
        counter=0#add 2 at random position
        self.matrix=t
        for i in t:
            for j in i:
                if j==0:
                    counter+=1
        while t[we][rt] != 0 and counter!=0:
            we,rt=random.choice(c),random.choice(c)
        if counter!=0 and t[we][rt]==0:
            t[we][rt]=2
        self.matrix=t
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(format(self.matrix[i][j],"6"),end="")
            print()
        print("score =",self.score)#print what we have

    def downward(self):
        '''invert to upward
                changes to row
                       adds and moves the numbers in the matrix to left
                           inverts back to column
                                    changes back to downward'''
        t=[]
        for i in self.matrix:
            t+=[[]]
        y=0
        i=[]
        self.matrix= self.matrix[::-1]#invert to upward
        print()
        for y in range(len(self.matrix)):
            i=[]
            for o in self.matrix:
                i+=[o[y]]#take all the first ellement to i
            d=sum(i)
            b=len(i)
            j=[]
            p=0
            while p+1 < len(i):
                a=i[p]
                ctr=p+1
                while ctr<len(i) and i[ctr]==0:
                    ctr+=1#pass all the 0s
                if ctr < len(i):#compare if not 0
                    if a==i[ctr]:
                        j.append(2*a)
                        self.score+=(2*a)#add 2*a to score
                        i.pop(ctr)   
                    elif a!=0:
                        j.append(a)
                elif ctr>=len(i):
                    if i[ctr-1]==0:
                        j.append(a)
                    elif a==i[ctr-1]:
                        j.append(a*2)
                p=ctr
            if sum(j)!=d:#to add the last non-0 element, if not included
                k=-1
                while i[k]== 0:
                    k-=1
                j.append(i[k])
            for l in range(b-len(j)):
                j.append(0)#fill the rest by 0
            for ty in range(len(t)):#reverse to column
                t[ty].append(j[ty])
        t=t[::-1]#change back to downward
        c=[]
        for i in range(len(t)):
            c+=[i]
        we=random.choice(c)
        rt=random.choice(c)
        counter=0#add 2 at random position
        self.n=t
        for i in t:
            for j in i:
                if j==0:
                    counter+=1
        while t[we][rt] != 0 and counter!=0:
            we,rt=random.choice(c),random.choice(c)
        if counter!=0 and t[we][rt]==0:
            t[we][rt]=2
        self.matrix=t
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(format(self.matrix[i][j],"6"),end="")
            print()
        print("score =",self.score)
    def game_over(self):
        '''cheks whether the game has end or not '''
        #find for 0 values in the matrix
        ctr=0 
        for i in self.matrix:
            for j in i:
                if j==0:
                    ctr+=1
        #find for similar values in the row
        k=0
        d=0    
        while k<(len(self.matrix)):
            l=1
            while l<len((self.matrix)):
                    if self.matrix[k][l]==self.matrix[k][l-1]:
                        d+=1
                    l+=1
            k+=1
        #find for similaar values in the coulumn
        p=[]
        for i in self.matrix:
                p.append([])
        for i in range(len(self.matrix)):#transposing the coulumn in to rows!
                for j in self.matrix:
                    p[i].append(j[i])
        c=0
        k=0
        while k<(len(p)):
                l=1
                while l<len((p)):
                    if p[k][l]==p[k][l-1]:
                        c+=1
                    l+=1
                k+=1
        #check for if the sumation of the zeros and the sumation of similar terms in the amtrix        
        f=d+c
        if ctr==0:           
            if f==0:
                return(True)
#interface which makes it easier to access        
print('                          2048 game                        ')
print('                just follow the instructions given')
starter=entry()
starter.start()
playing_mat=play()
playing_mat.game_over()
while playing_mat.game_over() != True:
        #print(playing_mat.game_over())
        command=input('give   4<=>left, 6<=>right,  8<=>upward  2<=>downward  or give "exit"')
        if command=='4':
            playing_mat.left() 
        elif command=='6':
            playing_mat.right()
        elif command=='2':
            playing_mat.downward()
        elif command=='8':
            playing_mat.upward()
        elif command=='exit':
            break
print("game over")
    #retry=input('do you want to play again(yes/no)?  ')
    #if retry=='no':
        #break
