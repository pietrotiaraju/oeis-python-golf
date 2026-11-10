# A001499

> Number of n X n matrices with exactly 2 1's in each row and column, other entries 0.
> — [OEIS A001499](https://oeis.org/A001499)

Offset 0: 1, 0, 1, 6, 90, 2040, 67950, 3110940, 187530840, 14398171200, …

### Python 3 — 55 bytes

```python
a=n=1;b=0
while[print(a)]:a,b=b,n*-~n*(2*b+n*a)//2;n+=1
```

**Why the recurrence**

- Stanley (*Enumerative Combinatorics* 2, Cor. 5.5.11 (b); also Comtet,
  *Advanced Combinatorics*, Sect. 6.3) proves

  Σ a(n) xⁿ/n!² = e^(−x/2) / √(1 − x).

- Call this B(x) = Σ bₙxⁿ. Its logarithmic derivative is
  −1/2 + 1/(2(1 − x)) = x/(2(1 − x)), so 2(1 − x)B′ = xB, which reads
  2(n+1)b₍ₙ₊₁₎ = 2n·bₙ + b₍ₙ₋₁₎. With bₙ = a(n)/n!² this is Bricard's
  recurrence (1901)

  **a(n+1) = n(n+1)/2 · (2a(n) + n·a(n−1)).**

**How it works**

- `a`, `b` hold a(n − 1), a(n) and `n` is n; the pass prints a(n − 1) and
  shifts in a(n + 1). It starts at n = 1 with a(0) = 1, a(1) = 0.
- n(n + 1) is even, so `//2` is exact; `n*-~n` is n(n + 1).

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(860)
  has more than 4300 digits, so Python's int-to-str limit stops it there,
  after a fraction of a second.
- The b-file has 254 terms (n = 0 to 253); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001499), CC BY-SA 4.0.
