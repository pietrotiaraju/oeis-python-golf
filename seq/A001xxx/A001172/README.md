# A001172

> Smallest even number that is an unordered sum of two odd primes in exactly n ways.
> — [OEIS A001172](https://oeis.org/A001172)

Offset 0: 0, 6, 10, 22, 34, 48, 60, 78, 84, 90, 114, 144, 120, 168, 180, 234, 246, 288, 240, 210, …

### Python 3 — 121 bytes

```python
n=m=0
while[print(m)]:
 n+=1;m=0
 while sum(all(k%d for k in(q,m-q)for d in range(2,k))for q in range(3,m//2+1,2))-n:m+=2
```

**How it works**

- For each n the program scans the even numbers m = 0, 2, 4, … and stops at
  the first one with exactly n representations m = q + (m − q), q ≤ m − q,
  both odd primes. So it prints the least such m, whatever order the values
  come in (a(11) = 144 comes after a(12) = 120, for instance).
- q runs over the odd numbers 3, 5, …, m/2, so m − q is odd and at least q,
  and every unordered pair is counted once (q = m/2 included).
- `all(k%d for k in(q,m-q)for d in range(2,k))` is trial division of both
  numbers at once; both are at least 3, so it is exactly "both prime". Written
  inline it is 10 bytes under a `P=lambda` called twice.
- a(0) = 0: 0 has no representation, and `while[print(m)]:` prints it before
  the first pass.

**Notes**

- Exact for every n. It assumes nothing about Goldbach-type statements: it
  only searches, and prints a(n) when it finds it.
- Trial division over every q and every m below a(n), redone for every n, makes
  this slow: about 53 terms in 20 s on the PC it was written on. The b-file has
  10001 terms (a(10000) = 855000); the bar is 55 terms in 60 s (fewer would
  fit in a table shorter than the program).
- Faster but longer (142 bytes): one pass over the odd x that keeps the odd
  primes in a set S (Wilson's theorem on a running factorial F = (x − 1)!),
  counts the ordered pairs of m = x + 1 as `len(S&{x+1-p for p in S})`, and
  keeps the unordered counts in a list R, printing `2*R.index(n)` once n is
  in it. It prints about 770 terms in 23 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001172), CC BY-SA 4.0.
