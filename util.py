def pad(i):
    ret = i
    if i % 100 != 0:
        i = i + 100 - (i%100)
    return i