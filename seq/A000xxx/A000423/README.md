# A000423

> a(n) is smallest number > a(n-1) of form a(i)*a(j), i < j < n.
> — [OEIS A000423](https://oeis.org/A000423)

Offset 1: 2, 3, 6, 12, 18, 24, 36, 48, 54, 72, …

### Python 3 — 44 bytes

```python
n=1
while 1:n+=1;6**n%n|n%6*(n>3)or print(n)
```

**How it works**

- The terms are 2, 3 and all 2^a·3^b with a, b ≥ 1 (David W. Wilson's comment
  on the OEIS page). Proof: call that set S. A product of two different
  elements of S has both primes 2 and 3, so it lies in S. Conversely
  6 = 2·3, 2^a·3^b = 2·(2^(a−1)·3^b) for a ≥ 2, and 2·3^b = 3·(2·3^(b−1)) for
  b ≥ 2, each a product of two different smaller elements of S. With the seeds
  2 and 3, by induction the sequence lists S in increasing order.
- So the program scans n = 2, 3, … and prints n when n is 3-smooth and
  (6 | n or n < 4). `6**n%n` is 0 exactly when n is 3-smooth: n | 6^n needs
  only primes 2 and 3 and exponents v₂(n), v₃(n) < n.
- `n%6*(n>3)` is 0 for multiples of 6 and for n = 2, 3, and nonzero for the
  other 3-smooth numbers (4, 8, 9, 16, 27, …). Both parts are nonnegative,
  so `|` is 0 iff both are, 3 bytes under ` or `; then `or print(n)` prints.

**Notes**

- `pow(6,n,n)` instead of `6**n%n`: 48 bytes and much faster (136 terms in
  20 s here). The direct construction, a set of pending products with
  `while[print(n:=min(s))]:s=s-{n}|{n*x for x in a};a+=n,`: 67.
- Exact integer arithmetic, so the program is right for every n.
- 6^n has n·log₁₀ 6 digits, so each test gets slower: the bar's 49 terms
  (up to 11664) take about 3 s here, and 67 terms (up to 49152) print in
  60 s.
- The b-file has 49 terms (up to a(49) = 11664); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |
| 2026-11-07 | Python 3 | 44 | the terms are 2, 3 and 2^a·3^b (a, b ≥ 1): test n \| 6^n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000423), CC BY-SA 4.0.
