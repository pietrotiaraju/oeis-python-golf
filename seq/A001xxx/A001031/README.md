# A001031

> Goldbach conjecture: a(n) = number of decompositions of 2n into sum of two primes (counting 1 as a prime).
> — [OEIS A001031](https://oeis.org/A001031)

Offset 1: 1, 2, 2, 2, 2, 2, 3, 2, 3, 3, 3, 4, 3, 2, 4, 3, 4, 4, 3, 3, …

### Python 3 — 84 bytes

```python
S={1};P=k=1
while 1:k+=1;S|={P%k*k};P*=k*k;k%2or print(-~len(S&{k-p for p in S})//2)
```

**How it works**

- `S` holds 1 and the primes up to k. With P = ((k−1)!)², Wilson's theorem
  gives P mod k = 1 for a prime k and 0 for a composite one (4 included:
  3!² = 36), so `S|={P%k*k}` adds k or 0.
- For even k = 2n, `S&{k-p for p in S}` is the set of p in S whose partner
  k−p is in S too: the ordered decompositions. Each unordered one counts
  twice except n+n, so a(n) = ⌈ordered/2⌉ = `-~x//2`.
- The stray 0 (added at k = 4) would pair only with k itself, and no even
  k ≥ 4 is in S; at k = 2 the 0 is not there yet, and 2 = 1+1 gives
  a(1) = 1.
- This is a plain count for each n: no Goldbach-type conjecture is
  involved.

**Notes**

- Exact integer arithmetic.
- The whole b-file (10 000 terms, 2n up to 20 000) prints in about 4 s;
  the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001031), CC BY-SA 4.0.
