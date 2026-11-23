# A002186

> Sprague-Grundy values for the game of Kayles (octal games .77 and .771).
> — [OEIS A002186](https://oeis.org/A002186)

Offset 0: 0, 1, 2, 3, 1, 4, 3, 2, 1, 4, 2, 6, 4, 1, 2, 7, 1, 4, 3, 2, …

### Python 3 — 84 bytes

```python
g=[]
while 1:print(x:=min({*range(9)}-{*map(int.__xor__,g+[99]+g,g[::-1]*2)}));g+=x,
```

**How it works**

- **The game.** A row of n pins; a move knocks down one pin or two
  adjacent pins, which may split the row in two. By the Sprague–Grundy
  theorem a set of rows has the XOR of their values, and a row has the
  mex (least missing value) of its options, so
  G(n) = mex{G(i) ⊕ G(j) : i + j = n − 1 or i + j = n − 2}.
- **All options in one pass.** `g` holds G(0), …, G(n − 1).
  `g[::-1]*2` is G(n − 1), …, G(0) twice, and it is XORed term by term
  with `g+[99]+g`: the first n pairs are (G(i), G(n − 1 − i)), then
  G(0) meets the filler 99, and the remaining n − 1 pairs are
  (G(i), G(n − 2 − i)), shifted by one place. So every split of n − 1
  and of n − 2 appears, in both orders (XOR is symmetric), plus the
  value 99 ⊕ G(0) = 99, far outside the candidate range. The
  filler is 1 byte shorter than keeping the list newest first
  (`r+r[1:]`, `r[::-1]*2`, `r=[x]+r`), and `map(int.__xor__,…)`, which
  stops at the shorter list, is 2 bytes shorter than
  `{a^b for a,b in zip(…)}`.
- **The mex.** `min({*range(9)}-S)` is the mex of S whenever the mex is
  at most 8. That holds for every n: by the periodicity theorem of Guy
  and Smith (Winning Ways, ch. 4), if an octal game whose moves take at
  most t tokens has G(n + p) = G(n) for all n with
  n0 ≤ n < 2n0 + p + t, then G(n + p) = G(n) for all n ≥ n0. Kayles has
  t = 2, and the values computed with an unbounded mex satisfy
  G(n + 12) = G(n) for 71 ≤ n < 156 (checked to n = 400; they agree
  with the whole b-file), so G is periodic with period 12 from n = 71
  on, as the entry says, and every value is one of G(0), …, G(82), at
  most 8. By induction on n the program's values are the true ones.

**Notes**

- The b-file has 105 terms (n = 0 to 104); the bar is all of them in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002186), CC BY-SA 4.0.
