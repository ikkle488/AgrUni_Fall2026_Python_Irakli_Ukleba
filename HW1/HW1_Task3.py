while True:
    number_1 = input('გთხოვთ შეიყვანოთ რიცხვი - ')
    number_f = number_1 or 0
    print('')
    try:
        float_f = float(number_f)
        print(float_f**2)
        break
    except ValueError:
        print("გთხოვთ შეიყვანოთ რიცხვი მხოლოდ ათწილადის სახით, მთელი გამოყავით წერტილით ან დატოვეთ ცარიელი ")