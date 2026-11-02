while True:
    try:
        Number_1 = int(input('შეიყვანეთ ნატურალური რიხცვი არაუდიდეს 1000: '))
        if 0<Number_1<=1000:
            count = 0
            for i in range(1,1000):
                if Number_1 % i < 1:
                    print(i, end='; ')
                    count = count + 1
            if count == 2:
                print('გილოცავთ!!! თქვენ იპოვეთ მარტივი რიცხვი')
            break
    except ValueError:
        print('გთხოვთ ნატურალური რიცხვი შეიყვანეთ თავიდან')
