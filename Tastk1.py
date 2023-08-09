poem = str(input("Введите стихотворение: "))
phrase_list = list()
count_list = list()
phrase_list = poem.split()
for i in range(len(phrase_list)):
    phrase = phrase_list[i]
    coutn_syllables = phrase.count('а')
    count_list.append(coutn_syllables)
j = 1
count_rhyme = 0
for j in range(len(count_list)):
    if count_list[j] == count_list[j - 1]:
        count_rhyme +=1
if count_rhyme == len(phrase_list):
    print('Парам пам-пам')
else:
    print('Пам парам')
        