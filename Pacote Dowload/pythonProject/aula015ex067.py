while True:
    num=int(input('Quer ver a tabuada de qual valor?: '))
    if num <=0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(num, c, num * c))
