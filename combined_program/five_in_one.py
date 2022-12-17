import sys

def count_base():
    чилсо = int(input("Число10 = "))
    п = int(input("п = "))

    к = 1
    числоп = 0

    while (чилсо != 0):
        числоп = числоп + (чилсо % п) * к

        к *= 10
        чилсо = чилсо // п

    print(числоп)

def hem_code():
    b='0000000 0001111 0010110 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    hem=b.split()
    code = "0101010"
    def Distance(first_code, second_code):
        dinstance = 7
        for i in range(len(first_code)):
            if first_code[i] == second_code[i]: dinstance -= 1
        return dinstance
    print(code)
    min_ = Distance(code, hem[0])
    i_min = 0
    for i in range(1, 10):
        d = Distance(code, hem[i])
        if min_ > d: 
            min_ = d
            i_min = i
    if min_ == 0: print("Код верный")
    elif min_ == 1: print(f"Код исправлен: {hem[i]} = {i_min}")
    else: print("CODE IS WrONG")

def morse():
    morse_dic = {
        'а' : '.-',
        'б' : '-...',    
        'в' : '.--', 
        'г' : '--.', 
        'д' : '-..', 
        'е' : '.', 
        'ж' : '...-', 
        'з' : '--..', 
        'и' : '..', 
        'й' : '.---', 
        'к' : '-.-', 
        'л' : '.-..', 
        'м' : '--', 
        'н' : '-', 
        'о' : '---', 
        'п' : '.--.', 
        'р' : '.-.', 
        'с' : '...', 
        'т' : '-', 
        'у' : '..-', 
        'ф' : '..-.', 
        'х' : '....', 
        'ц' : '-.-.', 
        'ч' : '---.', 
        'ш' : '----', 
        'щ' : '--.-', 
        'ъ' : '.--.-', 
        'ы' : '-.--', 
        'ь' : '-..-', 
        'э' : '..-..', 
        'ю' : '..--', 
        'я' : '.-.-', 
    }

    word = input("Введите слово: ")

    morse_word = '' 
    for letter in word:
        letter = letter.lower()
        
        print(f"{letter}: {morse_dic[letter]}")

def exit():
    sys.exit()

func = [count_base, hem_code, morse, exit]

while True:
    a = input("Выберите режим: 1 - система счисления, 2 - Код Хеммингтона, 3 - Код Морзе, 4 - Выход\n")
    if a.isdigit:
        if int(a) in [1, 2, 3, 4]:
            print("\n"*10)
            func[int(a) - 1]()
            print("")
    else:
        print("Ошибка ввода")
