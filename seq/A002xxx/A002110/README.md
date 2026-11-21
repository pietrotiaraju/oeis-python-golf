# A002110

> Primorial numbers (first definition): product of first n primes. Sometimes written prime(n)#.
> — [OEIS A002110](https://oeis.org/A002110)

Offset 0: 1, 2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230, …

### Python 3 — 49 bytes

```python
r=k=1
while 1:r*=1>pow(r,k:=k+1,k)or print(r)or k
```

**How it works**

- **Prime test.** r is the product of the primes below k. If k is prime,
  it does not divide r, so it does not divide r^k and `pow(r,k,k)` > 0. If
  k ≥ 2 is composite, each of its prime factors p is below k and divides r;
  if p^e is the exact power of p in k, then e < p^e ≤ k, so p^e divides
  p^k, which divides r^k. Hence k | r^k and `pow(r,k,k)` = 0. So the
  test is exact for every k ≥ 2 and rests on no conjecture.
- **One statement.** k steps first (`k:=k+1` inside `pow`, so the first k
  is 2). At a composite `1>pow(r,k,k)` is True and r is multiplied by 1. At
  a prime the comparison is False, `print(r)` prints the product of the
  primes found so far and gives None, and `or k` multiplies r by k. The
  primes come in order, so the lines are the primorials of 0, 1, 2, …
  primes.

**Notes**

- `pow(r,k,k)` reduces r modulo k before powering, so a test costs one
  pass over r. Wilson's theorem with P = (k−1)!, as in
  [A000040](../../A000xxx/A000040/), costs two more bytes.
- Exact integer arithmetic. The b-file has 351 terms (n = 0 to 350); the
  bar is the whole b-file in 60 s, a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002110), CC BY-SA 4.0.
