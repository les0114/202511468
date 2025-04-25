
def print_dan_group(start, end):
    for i in range(1, 10):
        for dan in range(start, end + 1):
            print(f"{dan} * {i} = {dan*i:2}", end='\t')
        print()



print_dan_group(2, 5)


print()


print_dan_group(6, 9)
