

def Fibonacci_sequence(n):
    if n <= 0:
        print("Please Enter a positive number .")
        return
    elif n==1:
        print(0)
        return
    
    a , b = 0 ,1 
    print(a , b ,end=" ")

    for _ in range(2,n):
        a , b = b ,a+b
        print(b,end=" ")

    return 


def main():
    n = int(input("Enter a positive number : "))
    Fibonacci_sequence(n)


main()
    