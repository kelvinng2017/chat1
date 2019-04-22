while True:
    print("請輸入最終成就:")
    print("請輸入分數:", end='')
    input_score = input()
    if input_score != '離開':

        if int(input_score) >= 90:
            print("A")
        elif int(input_score) >= 80:
            print("B")
        elif int(input_score) >= 70:
            print("C")
        elif int(input_score) >= 60:
            print("D")
        elif int(input_score) < 60:
            print("F")
    if input_score == '離開':
        print('謝謝')

        break