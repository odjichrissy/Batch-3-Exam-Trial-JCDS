'''
========================================================================================
FPB AND KPK
========================================================================================
'''

first_num = input('Enter the first number: ')
second_num = input('Enter the second number: ')
first_num_conv = int(first_num)
second_num_conv = int(second_num)


def FPB(first_value, second_value):
    if first_num_conv > second_num_conv:
        x = second_num_conv
    else:
        x = first_num_conv
    while x > 1:
        if first_num_conv % x == 0 and second_num_conv % x == 0:
            break
        x -= 1
    print(f'FPB dari {first_value} dan {second_value} adalah {x}')


def KPK(first_value, second_value):
    if first_num_conv > second_num_conv:
        y = second_num_conv
    else:
        y = first_num_conv
    while (True):
        if y % first_num_conv == 0 and y % second_num_conv == 0:
            terkecil = y
            break
        y += 1
    print(f'KPK dari {first_value} dan {second_value} adalah {terkecil}')

FPB(first_num, second_num)
KPK(first_num, second_num)
