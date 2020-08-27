""" 3. Napisz funkcję reverse_list, która przyjmuje listę processed_list.
Jej zadaniem jest obrócenie kolejności elementów w tej liście i zwrócenie odwróconej listy
(przykładowo, dla listy [1, 2, 3, 4], funkcja powinna zwrócić listę [4, 3, 2, 1]).
Uwaga: nie używaj wbudowanej funkcji reversed ani metody .reversed.
-- inna wersja tego zadania
Kolejna misja, to odwracanie stringów (jakkolwiek miałoby to nie brzmieć ;)).
Zakładamy, że mamy wejściowy string "hello world" i chcemy na wyjściu otrzymać "dlrow olleh".

3.1 Wykorzystując funkcję reverse_list, przygotuj funkcję is_palindrome, która przyjmować będzie tekst text.
Funkcja ta ma sprawdzić, czy tekst jest palindromem, tzn. czy ma taką samą postać czytany od przodu i od tyłu
(przykładem palindromu jest słowo "kajak").
Upewnij się, że Twoja funkcja reverse_list działa również dla łańcuchów znaków (stringów)."""


def reserve_list(processed_list):
    list_copy = []
    x = len(processed_list) - 1
    for _ in processed_list:
        list_copy.append(processed_list[x])
        x -= 1
    return list_copy


def reserve_text(string):
    list_string = []
    x = 0
    for _ in string:
        list_string.append(string[x])
        x += 1
    return reserve_list(list_string)


def is_palindrome(text):
    text_list = []
    change_text = reserve_text(text)
    x = 0
    result = 0
    for _ in text:
        text_list.append(text[x])
        x += 1
    merger_list = zip(text_list, change_text)
    for pair in merger_list:
        if pair[0] == pair[1]:
            result += 1
    if result == len(text_list):
        return 'Słowo ' + text + ' jest palindromem.'
    return 'Słowo ' + text + ' nie jest palindromem.'


def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    print(result)


if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    print(reserve_list(list_1))
    list_2 = reserve_text("Hello World")
    print(concatenate_list_data(list_2))
    print(is_palindrome("kajak"))