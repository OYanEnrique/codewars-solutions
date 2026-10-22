'''
SevenAte9:

Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"
'''
def seven_ate9(str):
    final_str=""
    for i, n in enumerate(str):
        if i+1 < len(str):
            if str[i] == '9'and str[i-1] == '7' and str[i+1] == '7':
                final_str+=''
            else:
                final_str+=str[i]
        else:
            final_str+=str[i]
    return final_str