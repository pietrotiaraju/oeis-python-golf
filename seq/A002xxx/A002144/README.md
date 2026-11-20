# A002144

> Pythagorean primes: primes of the form 4*k + 1.
> — [OEIS A002144](https://oeis.org/A002144)

Offset 1: 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149, …

### Python 3 — 56 bytes

```python
r=k=1
while 1:
 if pow(r,k:=k+1,k):r*=k;k%4>1or print(k)
```

**How it works**

- **Prime test.** r is the product of the primes below k. If k is prime,
  it does not divide r, so it does not divide r^k and `pow(r,k,k)` > 0. If
  k ≥ 2 is composite, each of its prime factors p is below k and divides r;
  if p^e is the exact power of p in k, then e < p^e ≤ k, so p^e divides
  p^k, which divides r^k. Hence k | r^k and `pow(r,k,k)` = 0. So the
  test is exact for every k ≥ 2 and rests on no conjecture.
- **Filter.** k runs over all integers from 2 (`k:=k+1` inside `pow`);
  every prime multiplies r, and `k%4>1or print(k)` prints it only when
  k ≡ 1 (mod 4). r must collect the primes of both classes for the test
  to work.

**Notes**

- `pow(r,k,k)` reduces r modulo k before powering, so a test costs one
  pass over r, which has about 98 000 digits at the end of the b-file.
  The whole b-file (10000 terms, up to 225217) comes in about 8
  reference seconds; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002144), CC BY-SA 4.0.
