while True:
    try:
        year = int(input('გთხოვთ შეიყვანეთ წელიწადი: '))
        if year > 0:
            if year % 400 < 1  or year % 4 < 1 and year % 100 >= 1:
                print('ნაკიანი წელია')
            else:
                print('არ არის ნაკიანი წელი')
            break
        else:
            print('გთხოვთ შეიყვანეთ ნატურალური რიცხვი')
    except ValueError:
        print('შეიყვანეთ ნატურალური რიცხვი, ჩაწერეთ მხოლოდ მთელი რიცხვის სახით')