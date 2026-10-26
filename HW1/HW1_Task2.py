while True:
    number_1 = input('შეიყვანეთ პირველი რიცხვი - ')
    number_2 = input('შეიყვანეთ მეორე რიცხვი - ')
    print('')
    try:
        float_1 = float(number_1)
        float_2 = float(number_2)
        if float_1 > float_2:
            print('პირველი მეტია')
            break
        elif float_1 < float_2:
                print('მეორე მეტია')
                break
        else:
                print('რიცხვები ტოლია (15 დეციმალის სიზუსტით)')
                break
    except ValueError:
        print('გთხოვთ შეიყვანოთ რიცხვები მხოლოდ ათწილადის სახით, მთელი გამოყავით წერტილით')