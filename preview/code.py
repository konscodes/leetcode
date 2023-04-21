'''
1. Find multiples of 3 and 5
if number from a range (below 10 so 0-10 in test case) is devided by 3 or 5 without a remainder
    add this number to list 
2. Take a sum
'''


def find_multiples(before):
    multiples = []
    for number in range(1, before):
        if number % 3 == 0 or number % 5 == 0:
            multiples.append(number)
    #print(multiples)
    return multiples


if __name__ == '__main__':
    print(sum(find_multiples(before=1000)))
