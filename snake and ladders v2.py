import random
import json
print("<>"*25)
print("SNAKE AND LADDERS V2")
print()
print("Do you want to see the rules?(y for yes or press enter to skip) ")
rules=input()
if rules=="y":
    print()
    print("The Rules Are :- ")
    print("1)The board will not be revealed\n")
    print("2)For each turn you get to roll the dice twice. You can choose which outcome you want to be considered\n")
    print("3)There are two mode: multiplayer and against computer(the computer is not stupid ;)\n")
    print("4)Throughout the game you will discover new snakes and ladders. You can display them when it is your turn to play \n")
    print('"snake_head": "snake_tail",')
    print('"29": 11')
    print("5)In the above example, there is a snkae from 29 to 11\n")
    print("6)You dont need a 1 to start, any number can start the match\n")
    print("7)You do not have to land exactly at 100 to win. If you cross 100, you win\n")
print()
print()

s1,s2,l1,l2=[],[],[],[]
no_s_l=random.randint(6,10)
i=0
while len(s1)<=no_s_l:
    r=random.randint(11,99)
    if s1.count(r)==0:
        s1=s1+[r]
i=0
while len(s2)<=no_s_l:
    t=(s1[i]//10)*10
    r=random.randint(1,t-1)
    if s1.count(r)==0 and s2.count(r)==0:
        s2=s2+[r]
        i=i+1
i=0
while len(l1)<=no_s_l:
    r=random.randint(11,99)
    if s1.count(r)==0 and s2.count(r)==0 and l1.count(r)==0:
        l1=l1+[r]
        i=i+1
i=0
while len(l2)<=no_s_l:
    t=(l1[i]//10)*10
    r=random.randint(1,t-1)
    if s1.count(r)==0 and s2.count(r)==0 and l1.count(r)==0 and l2.count(r)==0:
        l2=l2+[r]
        i=i+1
print()

print("Enter 1 for single player and 2 for multi player")
mode=int(input())
if mode==1:
    p1,p2=0,0
    z,c,i,cc=0,0,0,0
    s={'snake_head':'snake_tail'}
    l={'ladder_start':'ladder_end'}
    while p1<100 and p2<100:
        if z%2==0:
            print()
            print("It is your turn to play")
            print("You are at position ",p1)
            r1=random.randint(1,6)
            print("Your first number is ",r1)
            r2=random.randint(1,6)
            print("Your second number is ",r2)
            see=input("do you want to see the snakes and ladders you have discovered?(y/n) ")
            if see=="y":
                print(json.dumps((s),indent=4))
                print(json.dumps((l),indent=4))
            i,c=0,0
            while c!=r1 and c!=r2:
                if i>0:
                    print("Please enter either the first or second number")
                c=int(input("Enter the number you want to choose "))
                i=1
            p1=p1+c
            if p1 in s1:
                print("You discovered a snake :(")
                print("The snake is from ",p1," to ",s2[s1.index(p1)])
                s[p1]=s2[s1.index(p1)]
                p1=s2[s1.index(p1)]
            if p1 in l2:
                print("You discovered a ladder :)")
                print("The ladder is from ",p1," to ",l1[l2.index(p1)])
                l[p1]=l1[l2.index(p1)]
                p1=l1[l2.index(p1)]
        if z%2!=0:
            print()
            print("It is Computer's turn to play")
            print("Computer is at position ",p2)
            c1=random.randint(1,6)
            c2=random.randint(1,6)
            if (p2+c1) in s and (p2+c2) not in s:
                cc=c2
            elif (p2+c2) in s and (p2+c1) not in s:
                cc=c1
            elif (p2+c2) in s and (p2+c1) in s:
                diff1=(p2+c1)-s[p2+c1]
                diff2=(p2+c2)-s[p2+c2]
                if diff1>=diff2:
                    cc=c2
                else:
                    cc=c1
            elif (p2+c1) in l and (p2+c2) not in l:
                cc=c1
            elif (p2+c2) in l and (p2+c1) not in l:
                cc=c2
            elif (p2+c2) in l and (p2+c1) in l:
                diff1=(p2+c1)-l[p2+c1]
                diff2=(p2+c2)-l[p2+c2]
                if diff1>=diff2:
                    cc=c1
                else:
                    cc=c2
            else:
                if c1>=c2:
                    cc=c1
                else:
                    cc=c2
                    
            print("Number chosen by computer : ",cc)
            p2=p2+cc
            if (p2) in s1:
                print("Computer discovered a snake")
                print("The snake is from ",p2," to ",s2[s1.index(p2)])
                s[p2]=s2[s1.index(p2)]
                p2=s2[s1.index(p2)]
            if p2 in l2:
                print("Computer discovered a ladder")
                print("The ladder is from ",p2," to ",l1[l2.index(p2)])
                l[p2]=l1[l2.index(p2)]
                p2=l1[l2.index(p2)]
        z+=1

    print()
    print()
    if p1>=100:
        print("YOU WON")
    else:
        print("COMPUTER WON")
if mode==2:
    print("LOL it is under development. Restart the code and select single player")
                
                
            


        
    
        
    
    
