import re
def replace_dots(s):
    return re.sub(r"\.", "-", s)


replace_dots("hello....hello.......")
#regex yapisiyla  "."---> "-"