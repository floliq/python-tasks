def check_ip(ip):
    nums = ip.split('.')
    if ip.count('.') != 3 or len(nums) != 4:
        print('Адрес - это четыре числа, разделенные точками')
        return False
    for num in nums:
        if not num.isdigit():
            print('{}- не целое число'.format(num)) 
            return False
        if int(num) < 0:
            print('Наименьшее значение - 0')
            return False
        if int(num) > 255:
            print('{} превышает 255'.format(num))
            return False
    return True

    
while True:
    ip = input('Введите IP: ')
    if check_ip(ip):
        print('IP-адрес корректен') 
        break
