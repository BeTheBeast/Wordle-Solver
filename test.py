def single_true(iterable):
    i = iter(iterable)
    return any(i) and not any(i)  # check for first true : then make sure no other true values


print(single_true([True, True]))