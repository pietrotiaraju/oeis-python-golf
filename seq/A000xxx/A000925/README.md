# A000925

> Number of ordered ways of writing n as a sum of 2 squares of nonnegative integers.
> — [OEIS A000925](https://oeis.org/A000925)

Offset 0: 1, 2, 1, 0, 2, 2, 0, 0, 1, 2, 2, 0, 0, 2, 0, 0, 2, 2, 1, 0, …

### Python 3 — 60 bytes

```python
s={n:=0}
while[print(len(s&{n-k for k in s}))]:n+=1;s|={n*n}
```

**How it works**

- `s` is the set of squares 0², 1², …, n². An ordered pair (x, y) with
  x² + y² = n is a square k = x² in `s` with n − k also in `s`, and
  k ↦ n − k is one-to-one, so the count is the size of
  s ∩ {n − k : k ∈ s}.
- `len(s&{…})` is 1 byte under `sum(n-k in s for k in s)`, and a set
  makes each lookup O(1) (the list version of [A000161](../A000161/) is
  O(n) per lookup, too slow for ordered pairs over the whole b-file).
- `s={n:=0}` sets both at once (unparenthesized walrus in a set display,
  allowed since Python 3.10); each pass adds the next square with
  `s|={n*n}`.

**Notes**

- Exact integers, about n set operations per term: the whole b-file
  (10001 terms) prints in about 11 s, and the bar is the whole b-file.
- For n ≥ 1, a(n) = Σ_{d | n} χ₄(d) + [n is a square] (from the entry's
  (1 + θ₃)²/4), but the divisor sum is longer to write.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000925), CC BY-SA 4.0.
