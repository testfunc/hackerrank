def print_rangoli(size):
    alphabet = list(map(chr, range(97, 123)))[:size]
    rangoli = alphabet[::-1]+alphabet[1:]
    for i in range(len(rangoli)):
        if i < size:
            print('-'.join(rangoli[:i+1] + rangoli[:i][::-1]).center(len(rangoli)*2-1,'-'))
        if i >= size:
            print('-'.join(rangoli[:i-1:-1] + rangoli[i+1:]).center(len(rangoli)*2-1,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)