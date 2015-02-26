from fractions import gcd

def slice_bread(l, b):
    max_even_slice = gcd(l, b)
    bread_area = l * b
    max_even_slice_area = max_even_slice ** 2
    return int(bread_area / max_even_slice_area)

if __name__ == '__main__':
    num_cases = int(input())
    cases = (list(map(int, input().strip().split(" "))) for _ in range(num_cases))
    print(*list(map(lambda d: slice_bread(d[0], d[1]), cases)), sep='\n')
