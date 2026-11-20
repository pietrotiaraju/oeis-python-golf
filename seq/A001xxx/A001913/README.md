# A001913

> Full reptend primes: primes with primitive root 10.
> — [OEIS A001913](https://oeis.org/A001913)

Offset 1: 7, 17, 19, 23, 29, 47, 59, 61, 97, 109, 113, 131, 149, 167, 179, 181, …

### Python 3 — 62 bytes

```python
p=3
while[len({10**k%p for k in range(p)})>p-2==print(p)]:p+=2
```

**How it works**

- 10 is a primitive root modulo a prime p exactly when the powers 10⁰,
  10¹, …, 10^(p−1) take p − 1 different values mod p. The program tests
  every odd p ≥ 3 this way and prints p when there are more than p − 2
  values (`len(…)>p-2`, one byte shorter than `==p-1`).
- That test alone rules out composites, so there is no primality test.
  For an odd composite p prime to 10 the powers are units and repeat with
  a period dividing φ(p) < p − 1. If 5 divides p, every 10^k with k ≥ 1 is
  a multiple of 5 mod p, so there are at most p/5 + 1 values. Even p are
  never tried, and p = 3 (10 ≡ 1) and p = 5 (values 1, 0) fail too.
- In `…>p-2==print(p)` the chained comparison calls `print` only when the
  first comparison holds; the list `[False]` keeps the loop going.

**Notes**

- Same test as the primes with primitive root 2,
  [A001122](../A001122/); writing the loop as `while[…]:p+=2` from p = 3
  saves a byte over `while 1:p+=2;…`.
- `10**k%p` builds the whole power each time; `pow(10,k,p)` is 3 bytes
  longer and reaches about 2.5 times as many terms in the same time.
- Every odd p costs p powers, so the run slows down quickly: about 180
  terms (p = 3167) in 24 s here. The b-file has 10000 terms; the bar is
  170 terms (a(170) = 2897) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001913), CC BY-SA 4.0.
