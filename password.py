x = 3  # 剩餘機會
password = 'a123456'
while True:  # 注意：True 首字母需要大寫
    pwd = input('請輸入密碼: ')
    if pwd == password:
        print('登入成功')
        break
    else:
        x = x - 1
        print('密碼錯誤!還有', x, '次機會')
        if x == 0:
            break