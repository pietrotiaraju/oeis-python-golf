# A000118

> Number of ways of writing n as a sum of 4 squares; also theta series of four-dimensional cubic lattice Z^4.
> — [OEIS A000118](https://oeis.org/A000118)

Offset 0: 1, 8, 24, 32, 24, 48, 96, 64, 24, 104, 144, 96, 96, 112, 192, 192, 24, 144, 312, …

The number of integer 4-tuples (w, x, y, z), signs and order counted, with
w² + x² + y² + z² = n.

### Python 3 — 67 bytes

```python
n=0
while[print(8*sum(d*(d%4>0==n%d)for d in range(n+1))or 1)]:n+=1
```

**How it works**

- Jacobi's four-square theorem: for n ≥ 1, a(n) is 8 times the sum of the
  divisors d of n that are not multiples of 4.
- `d%4>0==n%d` is a chained comparison, `d%4>0 and 0==n%d`: d is not a
  multiple of 4 and divides n. Multiplying by `d` keeps exactly those
  divisors.
- The chain stops at `d%4>0` when d = 0, so `n%0` is never evaluated. That
  lets the range start at 0, and `range(n+1)` is 2 bytes shorter than
  `range(1,n+1)`.
- For n = 0 the sum is 0, and `or 1` prints a(0) = 1 (the empty sum of
  squares).
- `while[print(…)]` prints and loops forever, because `[None]` is a
  non-empty list.

**Notes**

- Correct for every n by Jacobi's theorem (a(n) = 8σ(n) − 32σ(n/4) in the
  OEIS formulas); exact integer arithmetic. A sieve check of the formula
  matched all 50001 b-file terms.
- Other shapes tried, all 68 bytes: `range(1,n+1)` with `d%4>n%d*3`
  (n%d·3 ≥ 3 beats d%4 unless d divides n); the filter form
  `sum(d for d in range(n+1)if d%4>0==n%d)`; negative divisors,
  `-8*sum(k*(k%4>n%k*k)for k in range(-n,0))`; and `^1>>n` in place of
  `or 1`. The odd-part formula, 8·(3 if n is even)·σ(odd part of n) with
  `3>>n%2`, is 75.
- Each term costs n + 1 steps: about 32 000 terms a minute. The b-file has
  50001 terms (n = 0 to 50000); the bar for this sequence is 10 000 terms
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000118), CC BY-SA 4.0.
