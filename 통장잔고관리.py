from msvcrt import getch
from os import system

class Usage:
    """Class that contains name, quantity of money, and docstring.
used as one line of account book."""
    def __init__(self, black_red ='+', name = '', money = 0, docstring = '-'):
        self.__black_red = black_red
        self.__name = name
        self.__money = money
        self.__docstring = docstring


    def set_black_red(self, black_red = '+'):
        self.__black_red = black_red       
    def set_name(self, name = ''):
        self.__name = name
    def set_money(self, money = 0):
        self.__money = money
    def set_docstring(self, docstring = '-'):
        self.__docstring = docstring
        

    def get_black_red(self):
        return self.__black_red
    def get_name(self):
        return self.__name
    def get_money(self):
        return self.__money
    def get_docstring(self):
        return self.__docstring


# data open
f = open("list.txt", 'r')
ment = f.readline()
ment = ment[:len(ment) - 1]
lines = f.readlines()
f.close()
usages = list()
sum_up = 0
for line in lines:
    split = line.split()
    if len(split) == 3:
        split.append('')
    usage = Usage(split[0], split[1], int(split[2]), split[3])
    usages.append(usage)
for usage in usages:
    if usage.get_black_red() == '+':
        sum_up += usage.get_money()
    else:
        sum_up -= usage.get_money()

# execute once
pos = 0
page = len(usages) // 10 + 1
max_page = len(usages) // 10 + 1
index_counter = 10 * page
maximum_index = min(index_counter, len(usages))
print("=" * 40)
print(ment)
print('-' * 40)
if len(usages) != 0:
    for index in range(index_counter - 10, maximum_index):
        if len(usages[index].get_name())< 3:
            if usages[index].get_money() >= 100000:
                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
            else:
                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
        else:
            if usages[index].get_money() >= 100000:
                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
            else:
                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
else:
    print("내역이 비어있습니다.")
print("-" * 40)
print("  계 :\t\t", sum_up)
print("-" * 40)
print('  새로운 내역 추가', end = '')
print('\t  <-')
print("=" * 40)
print('Page', max_page - page + 1, '/', max_page)

# main
while True:
    maximum_index = min(index_counter, len(usages))
    # switch input
    switch = getch()
    if switch == b'\xe0':
        switch = getch()

    # upper arrow
    if switch == b'H' and pos < maximum_index - index_counter + 10:
        pos += 1
        system('CLS')
        print("=" * 40)
        print(ment)
        print('-' * 40)
        for index in range(index_counter - 10, maximum_index):
            if len(usages[index].get_name())< 3:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring(), end = '')
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring(), end = '')
            else:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring(), end = '')
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring(), end = '')
            if index == maximum_index - pos:
                print(' <-', end = '')
            print()
        print("-" * 40)
        print("  계 :\t\t", sum_up)
        print("-" * 40)
        print('  새로운 내역 추가', end = '')
        if pos == 0:
            print('\t  <-', end = '')
        print()
        print("=" * 40)
        print('Page', max_page - page + 1, '/', max_page)

    # down arrow
    elif switch == b'P' and pos >0:
        pos -= 1
        system('CLS')
        print("=" * 40)
        print(ment)
        print('-' * 40)
        for index in range(index_counter - 10, maximum_index):
            if len(usages[index].get_name())< 3:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring(), end = '')
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring(), end = '')
            else:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring(), end = '')
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring(), end = '')
            if index == maximum_index - pos:
                print(' <-', end = '')
            print()
        print("-" * 40)
        print("  계 :\t\t", sum_up)
        print("-" * 40)
        print('  새로운 내역 추가', end = '')
        if pos == 0:
            print('\t  <-', end = '')
        print()
        print("=" * 40)
        print('Page', max_page - page + 1, '/', max_page)

    # left arrow
    elif switch == b'M' and page > 1:
        pos = 0
        page -= 1
        index_counter -= 10
        system('CLS')
        print("=" * 40)
        print(ment)
        print('-' * 40)
        maximum_index = min(index_counter, len(usages))
        for index in range(index_counter - 10, maximum_index):
            if len(usages[index].get_name())< 3:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
            else:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
        print("-" * 40)
        print("  계 :\t\t", sum_up)
        print("=" * 40)
        print('  새로운 내역 추가')
        print("=" * 40)
        print('Page', max_page - page + 1, '/', max_page)

    # right arrow
    elif switch == b'K' and page < max_page:
        pos = 0
        page += 1
        index_counter += 10
        system('CLS')
        print("=" * 40)
        print(ment)
        print('-' * 40)
        maximum_index = min(index_counter, len(usages))
        for index in range(index_counter - 10, maximum_index):
            if len(usages[index].get_name())< 3:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
            else:
                if usages[index].get_money() >= 100000:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                else:
                    print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
        print("-" * 40)
        print("  계 :\t\t", sum_up)
        print("-" * 40)
        print('  새로운 내역 추가')
        print("=" * 40)
        print('Page', max_page - page + 1, '/', max_page)
        
    # enter
    elif switch == b'\r':
        if pos == 0:
            pos = 1
            system('CLS')
            print("=" * 40)
            print('입력할 위치를 선택하시오')
            print("-" * 40)
            for index in range(index_counter - 10, maximum_index):
                if len(usages[index].get_name())< 3:
                    if usages[index].get_money() >= 100000:
                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                    else:
                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                else:
                    if usages[index].get_money() >= 100000:
                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                    else:
                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
            print('<-')
            print("=" * 40)
            print('Page', max_page - page + 1, '/', max_page)
            while True:
                # switch input
                switch = getch()
                if switch == b'\xe0':
                    switch = getch()
                    
                # esc
                if switch == b'\x1b':
                    system('CLS')
                    print("=" * 40)
                    print(ment)
                    print('-' * 40)
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print("-" * 40)
                    print("  계 :\t\t", sum_up)
                    print("-" * 40)
                    print('  새로운 내역 추가', end = '')
                    print('\t  <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    pos = 0
                    break
                    
                # upper arrow
                elif switch == b'H' and pos < maximum_index - index_counter + 11:
                    pos += 1
                    system('CLS')
                    print("=" * 40)
                    print('입력할 위치를 선택하시오')
                    print("-" * 40)
                    if pos == maximum_index - index_counter + 11:
                        print(' <-')
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        if index == maximum_index - pos:
                            print(' <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    
                # down arrow
                elif switch == b'P' and pos >1:
                    pos -= 1
                    system('CLS')
                    print("=" * 40)
                    print('입력할 위치를 선택하시오')
                    print("-" * 40)
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        if index == maximum_index - pos:
                            print(' <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)

                # left arrow
                elif switch == b'M' and page > 1:
                    pos = 0
                    page -= 1
                    index_counter -= 10
                    system('CLS')
                    print("=" * 40)
                    print('입력할 위치를 선택하시오')
                    print("-" * 40)
                    maximum_index = min(index_counter, len(usages))
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print('<-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)

                # right arrow
                elif switch == b'K' and page < max_page:
                    pos = 0
                    page += 1
                    index_counter += 10
                    system('CLS')
                    print("=" * 40)
                    print('입력할 위치를 선택하시오')
                    print("-" * 40)
                    maximum_index = min(index_counter, len(usages))
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print('<-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    
                # enter
                elif switch == b'\r':
                    system('CLS')
                    name = input("내역명 : ")
                    system('CLS')
                    while True:
                        money = input("금액(적자일경우 음수로 표시) : ")
                        try:
                            if money[0] == '-':
                                black_red = '-'
                                money = money[1:]
                            else:
                                black_red = '+'
                            money = int(money)
                        except ValueError:
                            system('CLS')
                            print("잘못된 입력입니다.")
                        except IndexError:
                            system('CLS')
                            print("잘못된 입력입니다.")
                        else:
                            break
                    system('CLS')
                    docstring = input("주석 입력 : ")
                    system('CLS')
                    print("=" * 40)
                    print('새로운 내역을 작성하시겠습니까?')
                    print("-" * 40)
                    print('적용')
                    print('취소 <-')
                    print("=" * 40)
                    cursor = 0
                    while True:
                            
                        # switch input
                        switch = getch()
                        if switch == b'\xe0':
                            switch = getch()
                            
                        # upper arrow
                        if switch == b'H' and cursor != 1:
                            system('CLS')
                            print("=" * 40)
                            print('새로운 내역을 작성하시겠습니까?')
                            print("-" * 40)
                            print('적용 <-')
                            print('취소')
                            print("=" * 40)
                            cursor = 1
                            
                        # down arrow
                        elif switch == b'P' and cursor != 0:
                            system('CLS')
                            print("=" * 40)
                            print('새로운 내역을 작성하시겠습니까?')
                            print("-" * 40)
                            print('적용')
                            print('취소 <-')
                            print("=" * 40)
                            cursor = 0

                        # esc
                        elif switch == b'\x1b':
                            system('CLS')
                            print("=" * 40)
                            print(ment)
                            print('-' * 40)
                            for index in range(index_counter - 10, maximum_index):
                                if len(usages[index].get_name())< 3:
                                    if usages[index].get_money() >= 100000:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                    else:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                else:
                                    if usages[index].get_money() >= 100000:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                    else:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                            print("-" * 40)
                            print("  계 :\t\t", sum_up)
                            print("-" * 40)
                            print('  새로운 내역 추가', end = '')
                            print('\t  <-')
                            print("=" * 40)
                            print('Page', max_page - page + 1, '/', max_page)
                            pos = 0
                            break
                        
                        # enter
                        elif switch == b'\r':
                            if cursor == 1:
                                usage = Usage(black_red, name, money, docstring)
                                if black_red == '+':
                                    sum_up += money
                                else:
                                    sum_up -= money
                                usages.insert(maximum_index - pos + 1, usage)
                                maximum_index = min(index_counter, len(usages))
                            break
                    system('CLS')
                    print("=" * 40)
                    print(ment)
                    print('-' * 40)
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print("-" * 40)
                    print("  계 :\t\t", sum_up)
                    print("-" * 40)
                    print('  새로운 내역 추가', end = '')
                    print('\t  <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    pos = 0
                    break
                    
        else:
            system('CLS')
            print("=" * 40)
            print('내역 관리')
            print("-" * 40)
            print('수정')
            print('삭제 <-')
            print("=" * 40)
            cursor = 0
            while True:
                
                # switch input
                switch = getch()
                if switch == b'\xe0':
                    switch = getch()
                        
                # upper arrow
                if switch == b'H' and cursor != 1:
                    system('CLS')
                    print("=" * 40)
                    print('내역 관리')
                    print("-" * 40)
                    print('수정 <-')
                    print('삭제')
                    print("=" * 40)
                    cursor = 1
                                
                #down arrow
                elif switch == b'P' and cursor != 0:
                    system('CLS')
                    print("=" * 40)
                    print('내역 관리')
                    print("-" * 40)
                    print('수정')
                    print('삭제 <-')
                    print("=" * 40)
                    cursor = 0
                    
                # esc
                elif switch == b'\x1b':
                    system('CLS')
                    print("=" * 40)
                    print(ment)
                    print('-' * 40)
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print("-" * 40)
                    print("  계 :\t\t", sum_up)
                    print("-" * 40)
                    print('  새로운 내역 추가', end = '')
                    print('\t  <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    pos = 0
                    break
                
                #enter
                elif switch == b'\r':
                    if cursor == 0:
                        system('CLS')
                        print("=" * 40)
                        print('삭제하시겠습니까?')
                        print("-" * 40)
                        print('확인')
                        print('취소 <-')
                        print("=" * 40)
                        cursor = 0
                        while True:
                            
                            # switch input
                            switch = getch()
                            if switch == b'\xe0':
                                switch = getch()
                            
                            # upper arrow
                            if switch == b'H' and cursor != 1:
                                system('CLS')
                                print("=" * 40)
                                print('삭제하시겠습니까?')
                                print("-" * 40)
                                print('확인 <-')
                                print('취소')
                                print("=" * 40)
                                cursor = 1
                            
                            #down arrow
                            elif switch == b'P' and cursor != 0:
                                system('CLS')
                                print("=" * 40)
                                print('삭제하시겠습니까?')
                                print("-" * 40)
                                print('확인')
                                print('취소 <-')
                                print("=" * 40)
                                cursor = 0

                            # esc
                            elif switch == b'\x1b':
                                system('CLS')
                                print("=" * 40)
                                print(ment)
                                print('-' * 40)
                                for index in range(index_counter - 10, maximum_index):
                                    if len(usages[index].get_name())< 3:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                    else:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                print("-" * 40)
                                print("  계 :\t\t", sum_up)
                                print("-" * 40)
                                print('  새로운 내역 추가', end = '')
                                print('\t  <-')
                                print("=" * 40)
                                print('Page', max_page - page + 1, '/', max_page)
                                pos = 0
                                break
                                
                            #enter
                            elif switch == b'\r':
                                if cursor == 1:
                                    if usages[maximum_index - pos].get_black_red() == '+':
                                        sum_up -= usages[maximum_index - pos].get_money()
                                    else:
                                        sum_up += usages[maximum_index - pos].get_money()
                                    usages.pop(maximum_index - pos)
                                maximum_index = min(index_counter, len(usages))
                                system('CLS')
                                print("=" * 40)
                                print(ment)
                                print('-' * 40)
                                for index in range(index_counter - 10, maximum_index):
                                    if len(usages[index].get_name())< 3:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                    else:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                           print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                print("-" * 40)
                                print("  계 :\t\t", sum_up)
                                print("-" * 40)
                                print('  새로운 내역 추가', end = '')
                                print('\t  <-')
                                print("=" * 40)
                                print('Page', max_page - page + 1, '/', max_page)
                                pos = 0
                                break
                        break
                    else:
                        system('CLS')
                        name = input(usages[maximum_index - pos].get_name() + "에서 내역명 변경 : ")
                        system('CLS')
                        while True:
                            if usages[maximum_index - pos].get_black_red() == '+':
                                money = input(str(usages[maximum_index - pos].get_money()) + "원에서 금액 변경(적자는 음수로 표시) : ")
                            else:
                                money = input('-' + str(usages[maximum_index - pos].get_money()) + "원에서 금액 변경(적자는 음수로 표시) : ")
                            try:
                                if money[0] == '-':
                                    black_red = '-'
                                    money = money[1:]
                                else:
                                    black_red = '+'
                                money = int(money)
                            except ValueError:
                                system('CLS')
                                print("잘못된 입력입니다.")
                            except IndexError:
                                system('CLS')
                                print("잘못된 입력입니다.")
                            else:
                                break
                        system('CLS')
                        docstring = input(usages[maximum_index - pos].get_docstring() + "에서 주석 내용 변경 : ")
                        system('CLS')
                        print("=" * 40)
                        print('변경을 적용하시겠습니까?')
                        print("-" * 40)
                        print('적용')
                        print('취소 <-')
                        print("=" * 40)
                        cursor = 0
                        while True:
                
                            # switch input
                            switch = getch()
                            if switch == b'\xe0':
                                switch = getch()
                                
                            # upper arrow
                            if switch == b'H' and cursor != 1:
                                system('CLS')
                                print("=" * 40)
                                print('변경을 적용하시겠습니까?')
                                print("-" * 40)
                                print('적용 <-')
                                print('취소')
                                print("=" * 40)
                                cursor = 1
                                
                            #down arrow
                            elif switch == b'P' and cursor != 0:
                                system('CLS')
                                print("=" * 40)
                                print('변경을 적용하시겠습니까?')
                                print("-" * 40)
                                print('적용')
                                print('취소 <-')
                                print("=" * 40)
                                cursor = 0

                            # esc
                            elif switch == b'\x1b':
                                system('CLS')
                                print("=" * 40)
                                print(ment)
                                print('-' * 40)
                                for index in range(index_counter - 10, maximum_index):
                                    if len(usages[index].get_name())< 3:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                    else:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                print("-" * 40)
                                print("  계 :\t\t", sum_up)
                                print("-" * 40)
                                print('  새로운 내역 추가', end = '')
                                print('\t  <-')
                                print("=" * 40)
                                print('Page', max_page - page + 1, '/', max_page)
                                pos = 0
                                break
                        
                            #enter
                            elif switch == b'\r':
                                if cursor == 1:
                                    if black_red == '+':
                                        if usages[maximum_index - pos].get_black_red() == '+':
                                            sum_up += money - usages[maximum_index - pos].get_money()
                                        else:
                                            sum_up += money + usages[maximum_index - pos].get_money()
                                    else:
                                        if usages[maximum_index - pos].get_black_red() == '+':
                                                    sum_up -= money + usages[maximum_index - pos].get_money()
                                        else:
                                            sum_up -= money - usages[maximum_index - pos].get_money()
                                    usages[maximum_index - pos].set_black_red(black_red)
                                    usages[maximum_index - pos].set_name(name)
                                    usages[maximum_index - pos].set_money(money)
                                    usages[maximum_index - pos].set_docstring(docstring)
                                system('CLS')
                                print("=" * 40)
                                print(ment)
                                print('-' * 40)
                                for index in range(index_counter - 10, maximum_index):
                                    if len(usages[index].get_name())< 3:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                    else:
                                        if usages[index].get_money() >= 100000:
                                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                        else:
                                           print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                print("-" * 40)
                                print("  계 :\t\t", sum_up)
                                print("-" * 40)
                                print('  새로운 내역 추가', end = '')
                                print('\t  <-')
                                print("=" * 40)
                                print('Page', max_page - page + 1, '/', max_page)
                                pos = 0
                                break
                        break
    # esc
    elif switch == b'\x1b':
        system('CLS')
        print("=" * 40)
        print('종료하시겠습니까?')
        print("-" * 40)
        print('종료')
        print('취소 <-')
        print("=" * 40)
        cursor = 0
        while True:
                
            # switch input
            switch = getch()
            if switch == b'\xe0':
                switch = getch()
                                
            # upper arrow
            if switch == b'H' and cursor != 1:
                system('CLS')
                print("=" * 40)
                print('종료하시겠습니까?')
                print("-" * 40)
                print('종료 <-')
                print('취소')
                print("=" * 40)
                cursor = 1
                                
            # down arrow
            elif switch == b'P' and cursor != 0:
                system('CLS')
                print("=" * 40)
                print('종료하시겠습니까?')
                print("-" * 40)
                print('종료')
                print('취소 <-')
                print("=" * 40)
                cursor = 0

            # esc
            elif switch == b'\x1b':
                system('CLS')
                print("=" * 40)
                print(ment)
                print('-' * 40)
                for index in range(index_counter - 10, maximum_index):
                    if len(usages[index].get_name())< 3:
                        if usages[index].get_money() >= 100000:
                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                        else:
                            print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    else:
                        if usages[index].get_money() >= 100000:
                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                        else:
                            print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                print("-" * 40)
                print("  계 :\t\t", sum_up)
                print("-" * 40)
                print('  새로운 내역 추가', end = '')
                print('\t  <-')
                print("=" * 40)
                print('Page', max_page - page + 1, '/', max_page)
                pos = 0
                break
                        
            # enter
            elif switch == b'\r':
                if cursor == 1:
                    system('CLS')
                    print("=" * 40)
                    print('저장하시겠습니까?')
                    print("-" * 40)
                    print('저장')
                    print('저장안함 <-')
                    print("=" * 40)
                    cursor = 0
                    while True:
                
                        # switch input
                        switch = getch()
                        if switch == b'\xe0':
                            switch = getch()
                                
                        # upper arrow
                        if switch == b'H' and cursor != 1:
                            system('CLS')
                            print("=" * 40)
                            print('저장하시겠습니까?')
                            print("-" * 40)
                            print('저장 <-')
                            print('저장안함')
                            print("=" * 40)
                            cursor = 1
                                
                        # down arrow
                        elif switch == b'P' and cursor != 0:
                            system('CLS')
                            print("=" * 40)
                            print('저장하시겠습니까?')
                            print("-" * 40)
                            print('저장')
                            print('저장안함 <-')
                            print("=" * 40)
                            cursor = 0

                        # esc
                        elif switch == b'\x1b':
                            system('CLS')
                            print("=" * 40)
                            print(ment)
                            print('-' * 40)
                            for index in range(index_counter - 10, maximum_index):
                                if len(usages[index].get_name())< 3:
                                    if usages[index].get_money() >= 100000:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                                    else:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                                else:
                                    if usages[index].get_money() >= 100000:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                                    else:
                                        print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                            print("-" * 40)
                            print("  계 :\t\t", sum_up)
                            print("-" * 40)
                            print('  새로운 내역 추가', end = '')
                            print('\t  <-')
                            print("=" * 40)
                            print('Page', max_page - page + 1, '/', max_page)
                            pos = 0
                            break
                        
                        # enter
                        elif switch == b'\r':
                            if cursor == 1:
                                f = open('list.txt', 'w')
                                f.write((ment + '\n'))
                                for usage in usages:
                                    write = usage.get_black_red() + ' ' + usage.get_name() + ' ' + str(usage.get_money()) + ' ' +  usage.get_docstring() + '\n'
                                    f.write(write)
                                f.close
                                exit()
                            else:
                                exit()
                else:
                    system('CLS')
                    print("=" * 40)
                    print(ment)
                    print('-' * 40)
                    for index in range(index_counter - 10, maximum_index):
                        if len(usages[index].get_name())< 3:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                        else:
                            if usages[index].get_money() >= 100000:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '', usages[index].get_docstring())
                            else:
                                print(usages[index].get_black_red(), usages[index].get_name(), '\t', usages[index].get_money(), '\t', usages[index].get_docstring())
                    print("-" * 40)
                    print("  계 :\t\t", sum_up)
                    print("-" * 40)
                    print('  새로운 내역 추가', end = '')
                    print('\t  <-')
                    print("=" * 40)
                    print('Page', max_page - page + 1, '/', max_page)
                    pos = 0
                    break
                break
