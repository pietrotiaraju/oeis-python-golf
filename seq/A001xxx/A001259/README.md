# A001259

> A sequence of sorted odd primes 3 = p_1 < p_2 < ... < p_m such that p_i-2 divides the product p_1*p_2*...*p_(i-1) of the earlier primes and each prime factor of p_i-1 is a prime factor of twice the product.
> — [OEIS A001259](https://oeis.org/A001259)

Offset 1: 3, 5, 7, 17, 19, 37, 97, 113, 257, 401, 487, 631, 971, 1297, 1801, 19457, 22051, 28817, 65537, 157303, 160001

### Python 3 — 93 bytes

```python
P=1;p=3
while[P%(p-2)+pow(2*P,p,p-1)or any(p%d<1for d in range(2,p))or[print(p),P:=P*p]]:p+=2
```

**How it works**

- The conditions only get weaker as the product of the earlier primes
  grows. So the sequence is the greedy one: scan the odd numbers p in
  increasing order and take p when it is prime, p − 2 divides P (the
  product of the primes taken so far), and every prime factor of p − 1
  divides 2P. Any sorted list with the property is contained in this
  one, by induction: each of its primes passes the test against a
  superset of its predecessors. The OEIS list is this maximal one, and Holt showed (see the OEIS entry) that it is complete:
  it ends at 160001.
- p − 1 < 2ᵖ, so every prime factor of p − 1 divides 2P exactly when
  (2P)ᵖ ≡ 0 (mod p − 1): `pow(2*P,p,p-1)`. `P%(p-2)` is the divisibility
  test. Trial division checks primality last, so it runs only for the
  few p that pass both cheap tests. p = 3 starts the list, with P = 1.
- When p is taken, `[print(p),P:=P*p]` prints it and multiplies it into
  P.

**Notes**

- All 21 terms come in a quarter of a second. After that the program
  keeps scanning forever without printing (Holt's theorem says nothing
  more comes). It does not stop by itself, so the program never assumes
  the theorem.
- The 21 terms fit in a table shorter than the program, so it needs a
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001259), CC BY-SA 4.0.
