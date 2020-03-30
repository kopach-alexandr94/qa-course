def test_one(function_fixture):
    print("Просто вывод текста на экран")

    """"Тест выводящий текст на экран"""


def test_two(class_fixture):
    list0 = [1, 2, 3, 4, 5]
    for i in list0:
        print(i)

    """"Тест выводящий список на экран"""


def test_three(module_fixture):
    t = (1, 2, 3)
    print(t[2])
    print("-----------------")

    """"Тест выводящий тупл на экран"""


def test_four(session_fixture):
    s = set()

    s.add('1')
    s.add('2')
    s.add('3')
    s.add('1')
    s.add('1')

    print(s)
    print('pop el ->', s.pop())
    print('len -> ', len(s))

    """"Тест выводящий сет на экран"""


def test_five(class_fixture):
    d = {'key': 'new_value'}
    del d['key']
    del d

    d = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '0': 'zero'}

    for i in d:
        print(i)

    """"Тест выводящий словарь на экран"""


def test_six(class_fixture):
    list1 = [1, 2, 3, "string", "autotest", 6, 7, 8, 9, 10]
    print(len(list1))

    """"Тест выводящий длину списка на экран"""


class TestClass:

    def test_seven(self, module_fixture):
        a = 2
        b = 5
        if a + b == 4:
            print(f"\n good")
        else:
            print(f"\n not so well")

        """"Тест выводящий строку в зависимости от переменных на экран"""

    def test_eight(self, function_fixture):
        x = 10
        y = 1
        z = x / y
        print(z)

        """"Тест выводящий результат деления на экран"""

    def test_nine(self, function_fixture):
        a = 3
        b = 5
        c = a * b
        print(c)

        """"Тест выводящий результат умножения на экран"""

    def test_ten(self, function_fixture):
        x = 10
        y = 5
        z = x / y
        print(z)
        if x / y == 2:
            print(f"\n z посчитано правильно")
        else:
            print(f"\n z посчитано не правильно")

        """"Тест выводящий результат деления на экран"""

