# A001917

> a(n) = (p-1)/x, where p = prime(n) and x = ord(2,p), the smallest positive integer such that 2^x == 1 (mod p).
> — [OEIS A001917](https://oeis.org/A001917)

Offset 2: 1, 1, 2, 1, 1, 2, 1, 2, 1, 6, 1, 2, 3, 2, 1, 1, 1, 1, 2, 8, 2, 1, 8, 2, …

### Python 3 — 71 bytes

```python
P=k=2
while[P%k>0==print(sum(2**e%k<2for e in range(1,k)))]:P*=k*k;k+=1
```

**How it works**

- For an odd prime p, 2^e ≡ 1 (mod p) holds exactly when e is a multiple
  of x = ord_p(2), and x divides p − 1. So among e = 1, …, p − 1 there are
  exactly (p − 1)/x such exponents, and counting them gives a(n) with no
  division: `sum(2**e%k<2for e in range(1,k))`. Modulo an odd prime 2^e is
  never 0, so `<2` means `==1`.
- Primes come from Wilson's theorem with a twist: `P=k=2` and `P*=k*k`
  keep P = 2·((k − 1)!)². For a prime k ≥ 3 that is 2 mod k; for a
  composite k it is 0 (also for k = 4: 2·36 = 72); and for k = 2 it is
  P = 2 ≡ 0. So `P%k>0` holds exactly for the odd primes, and p = 2,
  which is not in the sequence (offset 2 starts at p = 3), is skipped for
  free.
- `P%k>0==print(…)` is a chained comparison: the count is printed only
  when `P%k>0`; the list `[False]` keeps the loop going.

**Notes**

- Wilson's theorem and exact integers: right for every n.
- `pow(2,e,k)` instead of `2**e%k` is 4 bytes longer and faster.
- Every prime p costs p − 1 powers: about 976 terms (up to
  p = prime(977) = 7699) in 24 s here. The b-file has 9999 terms; the bar
  is 940 terms (up to p = prime(941) = 7417) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001917), CC BY-SA 4.0.
