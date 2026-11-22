# A002187

> Sprague-Grundy values for Dawson's Chess (octal game .137).
> — [OEIS A002187](https://oeis.org/A002187)

Offset 0: 0, 1, 1, 2, 0, 3, 1, 1, 0, 3, 3, 2, 2, 4, 0, 5, 2, 2, 3, 3, …

### Python 3 — 79 bytes

```python
g=[0]
while 1:print(x:=min({*range(10)}-{*map(int.__xor__,g,g[-2::-1])}));g+=x,
```

**How it works**

- **Octal game .137.** From a heap of n tokens a move takes one token
  if it is the whole heap, two tokens from an end (leaving one heap or
  none), or three tokens leaving up to two heaps. So a(1) = mex{0},
  a(n) for n ≥ 2 is the mex of a(n − 2) and, for n ≥ 3, all
  a(x) ⊕ a(y) with x + y = n − 3.
- **Through Dawson's Kayles (.07).** As the entry says, .07 (take two
  adjacent pins, leaving up to two rows) has values D(m) = a(m − 1):
  D(m) = mex{D(i) ⊕ D(m − 2 − i) : 0 ≤ i ≤ m − 2} with D(0) = 0, and for
  m = n + 1 the splits with i = 0 or i = n − 1 give
  D(0) ⊕ D(n − 1) = a(n − 2) (or D(0) ⊕ D(0) = 0 when n = 1), while
  1 ≤ i ≤ n − 2 gives a(i − 1) ⊕ a(n − 2 − i), every split of n − 3:
  the same option sets, so D(n + 1) = a(n) by induction.
- **The program.** `g` holds D(0), …, D(m − 1), starting from D(0) = 0,
  and `map(int.__xor__,g,g[-2::-1])` XORs D(i) with D(m − 2 − i) for
  i = 0, …, m − 2 (`g[-2::-1]` is the list reversed from its
  next-to-last entry, and `map` stops at the shorter list; it is
  2 bytes shorter than `{a^b for a,b in zip(…)}`). The first value
  printed is D(1) = a(0).
- **The mex.** `min({*range(10)}-S)` is the mex of S whenever the mex is
  at most 9. That holds for every n: by the periodicity theorem of Guy
  and Smith (Winning Ways, ch. 4), if an octal game whose moves take at
  most t tokens has a(n + p) = a(n) for all n with
  n0 ≤ n < 2n0 + p + t, then a(n + p) = a(n) for all n ≥ n0. Here
  t = 3, and a(n + 34) = a(n) holds for 52 ≤ n < 141 (and throughout
  the b-file, which a direct computation of .137 with an unbounded mex
  matches), so a is periodic with period 34 from n = 52 on, as the
  entry says, and every value is one of a(0), …, a(85), at most 9. By
  induction the program's values are the true ones.

**Notes**

- The b-file has 1001 terms (n = 0 to 1000); the bar is all of them in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002187), CC BY-SA 4.0.
