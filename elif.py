
def main():

    num1 = input('Gimme A Damn Number: ')  
    num1 = int(num1)

    num2 = input('Gimme Another Number: ')
    num2 = int(num2)

    maxNum = input('Enter the Max Number: ')
    maxNum = int(maxNum)

    if ( num1 + num2 > maxNum ):
        print(f'{num1} + {num2} > {maxNum}')
    elif (num1 + num2 < maxNum):
        print(f'{num1} + {num2} < {maxNum}')
    else: 
        print('They\'re equal')

        

if __name__ == '__main__':
    main()