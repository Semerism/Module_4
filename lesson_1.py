 # def strcounter(s): #решение за N**2
#     for sym in s:
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcounter('aabbbbccd')

# def strcounter(s): # решение за N * M
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

# strcounter('aabbbbccd')

# commit

# def strcounter(s): # решение за N
#     syms_counter = {}
#     for sym in s:
#         syms_counter[sym] = syms_counter.get(sym, 0) + 1

#     for sym, count in syms_counter.items():
#         print(sym, count)
# strcounter('aabbbbccd')
def palindrom_check(text):
    if text == text[::-1]:
        print('True')
    else:
        print ('False')
# Я написал функцию проверки на палиндром с помощью среза (::-1), эта "функция" переворачивает сртроки, узнал я о срезах из интернета.

    
    
    