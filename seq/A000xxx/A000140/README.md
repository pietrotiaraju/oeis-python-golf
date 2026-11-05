# A000140

> Kendall-Mann numbers: the most common number of inversions in a permutation on n letters is floor(n*(n-1)/4); a(n) is the number of permutations with this many inversions.
> — [OEIS A000140](https://oeis.org/A000140)

Offset 1: 1, 1, 2, 6, 22, 101, 573, 3836, 29228, 250749, 2409581, 25598186, …

### Python 3 — 78 bytes

```python
p=[1];z=[s:=0]
while[print(max(p))]:z+=0,;p=[s:=s+a-b for a,b in zip(p+z,z+p)]
```

**How it works**

- Counting permutations of n letters by inversions gives the Mahonian
  polynomial [1]·[2]⋯[n], with [m] = 1 + x + ⋯ + x^(m−1). Its coefficients
  peak at x^⌊n(n−1)/4⌋, so a(n) is simply its largest coefficient: `max(p)`.
- Each round multiplies the list `p` by the next factor
  [m] = (1 − x^m)/(1 − x). The list `z` holds m zeros (it gains one per
  round), so `zip(p+z,z+p)` pairs every coefficient of p with the one m
  places earlier, and `a-b` runs over the coefficients of p·(1 − x^m).
- Dividing by 1 − x is a running sum, kept in `s` by the walrus. `s` is set
  to 0 once (inside `z=[s:=0]`) and never reset: the coefficients of
  p·(1 − x^m) add up to p(1)·0 = 0, so each round's sum ends back at 0.
- That final 0 is also the last entry of the new list, so p picks up one
  trailing zero per round. Zeros do not change the maximum.
- `z` starts as `[0]`, so the first factor is [2] = 1 + x: the loop prints
  a(1) from `p=[1]`, then a(2), a(3), …

**Notes**

- Round n costs about n²/2 big-integer additions, so the whole b-file
  (400 terms) prints in about 5 s. The bar is the whole b-file in 60 s.
- Summing a sliding window, `p=[sum(p[:i+1][~n:])for i in range(len(p)+n)]`,
  needs zero padding on one side to be right and came out at 85–86 bytes.
- Growing `z` inside the `zip` call with a walrus would save the `z+=0,;`,
  but an assignment expression is not allowed in a comprehension's iterable.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000140), CC BY-SA 4.0.
