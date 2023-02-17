def all_multiples(devisor, numbers):
    '''List all multiples of a given devisor from a given range'''
    print(f'Devisor is {devisor}')
    print(f'List of natural numbers is {numbers}')
    multiples = []
    for number in numbers:
        print(f'Taking number {number}')
        if number % devisor == 0:
            print(f'{number} is devided by {devisor} withot a remainder')
            multiples.append(number)
        else:
            print(f'{number} is devided by {devisor} with a remainder')
    print(f'All multiples of {devisor} are {multiples}')
    return multiples

devisors = {3, 5}
numbers = [number for number in range(11)]
print(sum(all_multiples(devisor, numbers) for devisor in devisors))
