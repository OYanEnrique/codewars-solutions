'''
Kebabize:
Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters
'''
import re
def kebabize(st):
    st=re.sub(r'\d', '', st)
    return '-'.join(re.split(r'(?=[A-Z])', st)).lower().lstrip('-')