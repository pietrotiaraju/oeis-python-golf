# A000825

> Expansion of cos x (1 + sin x ) /cos 2x.
> — [OEIS A000825](https://oeis.org/A000825)

Offset 0: 1, 1, 3, 8, 57, 256, 2763, 17408, 250737, 2031616, 36581523, 362283008, 7828053417, …

### Python 3 — 83 bytes

```python
r=[]
while[print(abs(s:=3**len(r)+(r>[])-sum(r+r))+1>>1)]:r=[s:=s+x*4for x in[0]+r]
```

**How it works**

- Replacing x by ix in the even part of the e.g.f. and by ix (then
  dividing by i) in its odd part multiplies the n-th coefficient by
  (−1)^⌊n/2⌋ and turns cos into cosh, sin into sinh (see
  [A000810](../A000810/)).
- cos x·(1 + sin x)/cos 2x = sec 2x·(cos x + sin 2x/2) becomes
  F(x) = sech 2x·(cosh x + sinh 2x/2). Since cosh x·sech 2x =
  (e^(3x) + eˣ)/(1 + e^(4x)) and tanh 2x/2 = 1/2 − 1/(1 + e^(4x)),
  2F − 1 = 2(e^(3x) + eˣ − 1)/(1 + e^(4x)).
- So z(n), the coefficients of Z = 2F − 1, satisfy
  (1 + e^(4x))·Z = 2(e^(3x) + eˣ − 1). As on the A000810 page, a Seidel
  triangle (row n starts at z(n), T(n,k) = T(n,k−1) + 4·T(n−1,k−1)) ends
  at z(n) + 4·(sum of row n−1), which gives
  z(n) = 3ⁿ + [n ≥ 1] − 2·(sum of row n−1).
- `r` is row n−1, so `len(r)` is n and `(r>[])` is [n ≥ 1]. For n ≥ 1,
  z(n) = 2·(−1)^⌊n/2⌋·a(n), and z(0) = 1 = a(0), so `abs(z)+1>>1` is a(n)
  for every n. `[s:=s+x*4for x in[0]+r]` then builds row n.
- The absolute value restores the sign because every a(n) ≥ 0: the even
  terms are the Springer numbers [A001586](https://oeis.org/A001586)
  (the cos x/cos 2x part) and the odd ones are tan 2x/2, that is
  [A000828](../A000828/)(n).

**Notes**

- Row n has n+1 entries, so a(n) costs about n big-integer additions.
  The whole b-file (201 terms) prints in a few hundredths of a second;
  the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1508) (about 4 s here).
- Other normalizations need a second power: 2F + 1 has numerator
  2(e^(4x) + e^(3x) + eˣ), 2 bytes longer.
- Two boustrophedon triangles (Springer numbers for even n, A000828 for
  odd n) take over 110 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000825), CC BY-SA 4.0.
