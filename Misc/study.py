month = 12
try:
    month = month + 1
    assert 1 <= month <= 12
except:
    print('h')
    print(month)

print(month)