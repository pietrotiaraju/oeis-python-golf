# A000822

> Expansion of (sin^2 x + sin x) /cos 2x.
> — [OEIS A000822](https://oeis.org/A000822)

Offset 0: 0, 1, 2, 11, 40, 361, 1952, 24611, 177280, 2873041, 25866752, 512343611, 5535262720, …

### Python 3 — 85 bytes

```python
r=[]
while[print(abs(s:=3**len(r)+2**len(r)+~sum(r+r))>>1)]:r=[s:=s+x*4for x in[0]+r]
```

**How it works**

- Replacing x by ix in the even part of the e.g.f. and by ix (then
  dividing by i) in its odd part multiplies the n-th coefficient by
  (−1)^⌊n/2⌋ and turns cos into cosh, sin into sinh (see
  [A000810](../A000810/)).
- (sin²x + sin x)/cos 2x = sec 2x·(sin x + sin²x) becomes
  F(x) = sech 2x·(sinh x − sinh²x). With cosh 2x = 1 + 2 sinh²x,
  2F + 1 = (2 sinh x + 1)·sech 2x = 2(e^(3x) + e^(2x) − eˣ)/(1 + e^(4x)).
- So z(n), the coefficients of Z = 2F + 1, satisfy
  (1 + e^(4x))·Z = 2(e^(3x) + e^(2x) − eˣ). As on the A000810 page, a
  Seidel triangle (row n starts at z(n), T(n,k) = T(n,k−1) + 4·T(n−1,k−1))
  ends at z(n) + 4·(sum of row n−1), which gives
  z(n) = 3ⁿ + 2ⁿ − 1 − 2·(sum of row n−1).
- `r` is row n−1 (`len(r)` = n); `~sum(r+r)` is −2·sum − 1. For n ≥ 1,
  z(n) = 2·(−1)^⌊n/2⌋·a(n), and z(0) = 1 while a(0) = 0, so `abs(z)>>1`
  is a(n) for every n. `[s:=s+x*4for x in[0]+r]` then builds row n.
- The absolute value restores the sign because every a(n) ≥ 0: the odd
  terms are the Springer numbers [A001586](https://oeis.org/A001586)
  (the sin x/cos 2x part) and the even ones are (sec 2x − 1)/2,
  [A000816](../A000816/).

**Notes**

- Row n has n+1 entries, so a(n) costs about n big-integer additions.
  The whole b-file (178 terms) prints in a few hundredths of a second;
  the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1508) (about 4 s here).
- `3**len(r)` is 1 byte under a separate power `p=1` … `p*=3`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000822), CC BY-SA 4.0.
