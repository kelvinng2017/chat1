while True:

    print("請輸入年齡:", end='')
    year_old = input()
    if year_old != '離開':
        if int(year_old) >= 18:
            print("你已經成年,可看各級電影！")
        elif int(year_old) >= 12:
            print("可看限制級以外所有影片！")
        elif int(year_old) >= 6:
            print("可看普遍級及保護及!")
        elif int(year_old) < 6:
            print("可看普遍及!")

    if year_old == '離開':
        print('謝謝')

        break