#At least 8 char long
#contain any sort letters, numbers and $W%^$

import re

password = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
string = '@Gwge23214$$@'
check = password.search(string)

print(check)