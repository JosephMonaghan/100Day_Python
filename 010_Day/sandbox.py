def format_name(first,last):
    tmp=first.title()
    tmp2=last.title()
    result=f"{tmp} {tmp2}"
    return result

test=format_name("jOsePh", "moNaghan")

print(test)
