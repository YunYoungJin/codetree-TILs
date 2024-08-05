n = int(input())

def is_valid(seq):
    length = len(seq)
    for size in range(1, length // 2 + 1):
        for start in range(length - 2 * size + 1):
            if seq[start:start + size] == seq[start + size:start + 2 * size]:
                return False
    return True

def make_seq(seq, n):
    if len(seq) == n:
        return seq

    for digit in '456':
        next_seq = seq + digit
        if is_valid(next_seq):
            result = make_seq(next_seq, n)
            if result:
                return result
    
    return None

print(make_seq('', n))