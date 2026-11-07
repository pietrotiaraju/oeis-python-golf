# A000777

> a(n) = (n+2)*Catalan(n) - 1.
> — [OEIS A000777](https://oeis.org/A000777)

Offset 0: 1, 2, 7, 24, 83, 293, 1055, 3860, 14299, 53481, 201551, 764217, 2912167, …

### Python 3 — 44 bytes

```python
c=n=1
while 1:n+=1;print(c*n-1);c=4*c-6*c//n
```

**How it works**

- The Catalan numbers C_m = binomial(2m,m)/(m+1) satisfy
  C_{m+1} = C_m·2(2m+1)/(m+2). With n = m + 2 that is
  C_m·(4n−6)/n = 4·C_m − 6·C_m/n, the update of
  [A000108](../A000108/); 6·C_m/n is an integer because C_{m+1} and
  4·C_m are, so `//` is exact.
- `n` runs one ahead of A000108's: after `n+=1` it is m + 2 while `c` is
  still C_m, which is exactly the multiplier of the term, so the print is
  just `c*n-1`, and the same n then drives the step to C_{m+1}.
- Starting at `c=n=1`, the first round has n = 2 and C_0 = 1 and prints
  2·1 − 1 = 1. `while 1:` with `n+=1` first beats `while[print(…)]:` here:
  that form needs `c=1;n=2` (or `-~n` in the print) and is 45 bytes.

**Notes**

- (n+2)·C_n is also binomial(2n,n) + C_n, but carrying the central
  binomial and dividing by n + 1 is longer.
- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 7146, so printing stops
  there with a ValueError (about a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000777), CC BY-SA 4.0.
