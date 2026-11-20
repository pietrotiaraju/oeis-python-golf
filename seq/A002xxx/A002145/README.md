# A002145

> Primes of the form 4*k + 3.
> — [OEIS A002145](https://oeis.org/A002145)

Offset 1: 3, 7, 11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127, 131, …

### Python 3 — 56 bytes

```python
r=k=1
while 1:
 if pow(r,k:=k+1,k):r*=k;k%4<3or print(k)
```

**How it works**

- **Prime test.** r is the product of the primes below k. If k is prime,
  it does not divide r, so it does not divide r^k and `pow(r,k,k)` > 0. If
  k ≥ 2 is composite, each of its prime factors p is below k and divides r;
  if p^e is the exact power of p in k, then e < p^e ≤ k, so p^e divides
  p^k, which divides r^k. Hence k | r^k and `pow(r,k,k)` = 0. So the
  test is exact for every k ≥ 2 and rests on no conjecture.
- **Filter.** k runs over all integers from 2 (`k:=k+1` inside `pow`);
  every prime multiplies r, and `k%4<3or print(k)` prints it only when
  k ≡ 3 (mod 4). r must collect the primes of both classes for the test
  to work.

**Notes**

- `pow(r,k,k)` reduces r modulo k before powering, so a test costs one
  pass over r, which has about 98 000 digits at the end of the b-file.
  The whole b-file (10000 terms, up to 224267) comes in about 8
  reference seconds; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002145), CC BY-SA 4.0.
