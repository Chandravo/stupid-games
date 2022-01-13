#HAND CRICKET GAME
import time
import random
c=input("enter your choice- ODD or EVEN - ")
choice=c.lower()
e=0
r=0

if choice=="odd":
    ctoss=random.randint(1,6)
    toss=int(input("enter your no. "))
    print("your opponent's no. ",ctoss)
    if (toss+ctoss)%2!=0:
        print("YOU WON THE TOSS")
        l=input("enter whether you want to BAT or BOWL ")
        inn=l.lower()
        n,m,b,v=1,2,3,4
        if inn=="bat":
            n=0
            while (n%7)!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
            print("-"*50,"YOU ARE OUT","-"*50)
            print("YOU TOTAL SCORE = ",r)
            print('YOU ARE BOWLING')
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
                if e>r:
                    break
        elif inn=="bowl":
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
            print("-"*50,"YOU BOWLED YOUR OPPONENT","-"*50)
            print("SCORE TO BEAT = ",e)
            print('YOU ARE BATTING')
            n=0
            while (n%7)!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
                if r>e:
                    break
    else:
        print("YOUR OPPONENT WON THE TOSS")
        if ctoss%2==0:
            print("Your opponent chose to bat....you will bowl")
            inn="bowl"
        else:
            print("Your opponent chose to bowl...you will bat")
            inn="bat"
        n,m,b,v=1,2,3,4
        if inn=="bat":
            n=0
            while (n%7)!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
            print("-"*50,"YOU ARE OUT","-"*50)
            print("YOUR TOTAL SCORE = ",r)
            print('YOU ARE BOWLING')
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print('your opponents no. ',b)
                if b!=v:
                    e=e+b
                if e>r:
                    break
        elif inn=="bowl":
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
            print("-"*50,"YOU BOWLED YOUR OPPONENT","-"*50)
            print("SCORE TO BEAT = ",e)
            print('YOU ATE BATTING')
            n=0
            while (n%7)!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
                if r>e:
                    break
elif choice=="even":
    ctoss=random.randint(1,6)
    toss=int(input("enter your no. "))
    print("your opponent's no. ",ctoss)
    if (toss+ctoss)%2==0:
        l=input("enter whether you want to BAT or BOWL ")
        inn=l.lower()
        n,m,b,v=1,2,3,4
        if inn=="bat":
            n=0
            while n!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
            print("-"*50,"YOU ARE OUT","-"*50)
            print("YOUR TOTAL SCORE = ",r)
            print('YOU ARE BOWLING')
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
                if e>r:
                    break
        elif inn=="bowl":
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
            print("-"*50,"YOU BOWLED YOUR OPPONENT","-"*50)
            print("SCORE TO BEAT = ",e)
            print('YOU ARE BATTING')
            n=0
            while n!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
                if r>e:
                    break
    else:
        print("YOUR OPPONENT WON THE TOSS")
        if ctoss%2==0:
            print("Your opponent chose to bat....you will bowl")
            inn="bowl"
        else:
            print("Your opponent chose to bowl...you will bat")
            inn="bat"
        n,m,b,v=1,2,3,4
        if inn=="bat":
            n=0
            while n!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n
            print("-"*50,"YOU ARE OUT","-"*50)
            print("YOUR TOTAL SCORE = ",r)
            print('YOU ARE BOWLING')
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
                if e>r:
                    break
        elif inn=="bowl":
            b=0
            while b!=v:
                print("opponent runs = ",e)
                b=random.randint(1,6)
                v=int(input("enter your no. "))
                print("your opponent's no. ",b)
                if b!=v:
                    e=e+b
            print("-"*50,"YOU BOWLED YOUR OPPONENT","-"*50)
            print("SCORE TO BEAT = ",e)
            print('YOU ARE BATTING')
            n=0
            while n!=m:
                print("your runs = ",r)
                m=random.randint(1,6)
                n=int(input("enter your no. "))
                print("your opponent's no. ",m)
                if n!=m:
                    r=r+n%7
                if r>e:
                    break

if r>e:
    print("="*50,"YOU WON","="*50)
    time.sleep(10)
elif r==e:
    print("="*50,"TIE","="*50)
    time.sleep(10)
else:
    print("="*50,"YOU LOST","="*50)
    time.sleep(10)
