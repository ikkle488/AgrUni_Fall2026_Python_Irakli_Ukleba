while True:
    word = input('დაწერეთ ნებისმიერი ქართული სიტყვა - ')
    import re
    if re.fullmatch(r'^[\u10d0-\u10ff]+$', word):
        break
    else:
        print('გთხოვთ შეიყვანოთ მხოლოდ ქართული ასოები')
while True:
    number = input('აირჩიეთ ნებისმიერი ნატურალური რიცხვი - ')
    try:
        numint = int(number)
        if numint > 0:
            print('\n' + 'გამოტოვების ჩათვლით - ' + (word + ' ')* numint)
            print('გამოტოვების გარეშე - ' + (word * numint))
            print('\n' + 'სამწუხაროდ ქართული ლექსიკონი არ არის ჩაშენებული პროგრამაში და მითითებული სიტყვის არსებობა არ შემოწმებულა')
            break
        else:
            print('გთხოვთ შეიყვანოთ ნატურალური რიცხვი')
    except ValueError:
        print('გთხოვთ შეიყვანოთ ნატურალური რიცხვი')