import math
from util import random_bit, random_matrix, random_noise_vector, random_vector, zero_matrix, zero_vector

# LWE

n = 512
q = 3329
noise_distribution = [-3, 3]


def floor(x):
    return int(math.floor(x))


def get_LWE_sample(s):
    A = random_matrix(q, 1, n)
    e = random_noise_vector(q, noise_distribution, 1)
    b = A * s + e
    return (A, b)


def keygen():
    s = random_vector(q, n)
    return s


def encrypt(s, m):
    assert m == 0 or m == 1
    (A, b) = get_LWE_sample(s)
    c = b + floor(q / 2) * m
    return (A, c)


def decrypt(s, ct):
    (A, c) = ct
    raw = c - A * s
    return round(int(raw) * 2 / q) % 2


s = keygen()
assert (decrypt(s, encrypt(s, 1)) == 1)
assert (decrypt(s, encrypt(s, 0)) == 0)
print("LWE working correctly.")

# PIR

num_items_in_db = 50
desired_idx = 24
db = [random_bit() for i in range(num_items_in_db)]


def generate_query(desired_idx):
    v = []
    for i in range(num_items_in_db):
        bit = 1 if i == desired_idx else 0
        ct = encrypt(s, bit)
        v.append(ct)
    return v


def answer_query(query, db):
    summed_A = zero_matrix(q, 1, n)
    summed_c = zero_vector(q, 1)
    for i in range(num_items_in_db):
        if db[i] == 1:
            (A, c) = query[i]
            summed_A += A
            summed_c += c
    return (summed_A, summed_c)


s = keygen()
query = generate_query(desired_idx)

print("Sending the query to the server...")

answer = answer_query(query, db)

print("Got the answer back from the server...")

result = decrypt(s, answer)

print("The item at index %d of the database is %d" % (desired_idx, result))

assert result == db[desired_idx]
print("PIR was correct!")
