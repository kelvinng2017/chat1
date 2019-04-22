
while True:
    print("請輸入密碼:", end='')
    password = input()
    if int(password) == 1234567:
        print("歡迎光臨!敬請指教")
        break
    else:
        print("密碼錯誤!請在重新輸入")