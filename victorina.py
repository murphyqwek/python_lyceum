import random

questions = []

count = 0

def get_questions():
    with open("q.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        q = []
        for i in range(len(lines)):
            if lines[i] == '\n': 
                questions.append(q)
                q = []
                continue
            q.append(lines[i][:-1])

get_questions()

for i in range(len(questions)):
    j = random.randint(0, len(questions) - 1)
    question = questions[j]
    print(f'{i+1}) ' + question[0])
    variants = question[1].split('/')
    for j, variant in enumerate(variants):
        print(f'{j+1}. ' + variant)
    print()
    ans = input("Ответ: ")
    if question[2] == variants[int(ans)-1]:
        print("\nОтвет правильный! +1 балл")
        count += 1
    else:
        print("\nОтвет неправильный! Правильный ответ: " + question[2] + ". -1 балл")
    questions.remove(question)

print(f"\nВаш результат: {count}")
