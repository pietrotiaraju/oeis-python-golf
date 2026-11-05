# A000166

> Subfactorial or rencontres numbers, or derangements: number of permutations of n elements with no fixed points.
> — [OEIS A000166](https://oeis.org/A000166)

Offset 0: 1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496, …

### Python 3 — 34 bytes

```python
a=n=1
while[print(a)]:a=a*n^1;n+=1
```

**How it works**

- The derangement numbers satisfy a(n) = n·a(n−1) + (−1)^n.
- n·a(n−1) always has the parity of n: for even n it is even, and for odd
  n both factors are odd (a(n−1) is odd when n−1 is even, by induction: an
  even n·a(n−1) plus 1 is odd). So for even n we add 1 to an even number
  and for odd n we subtract 1 from an odd one, and both are `^1`, which
  flips the last bit: a(n) = n·a(n−1) xor 1, with no `(-1)**n`.
- `*` binds tighter than `^`, so `a*n^1` needs no parentheses.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (451 terms) prints at once; the program stops after a(1558), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000166), CC BY-SA 4.0.
