a = 0
b = 1
c = 0
print('\n\033[33m{:=^40}'.format("\033[m FIBONACCI \033[33m"))
print(f'    \033[31m{a} {b} ',end='')
for i in range(0,8):
    c = a + b
    a = b
    b = c
    print(f'{c} ',end='')
print('\n\033[33m{:^30}'.format("=============="))
