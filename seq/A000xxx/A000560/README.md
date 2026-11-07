# A000560

> Number of symmetric ways of folding a strip of n labeled stamps.
> — [OEIS A000560](https://oeis.org/A000560)

Offset 2: 1, 2, 5, 12, 33, 87, 252, 703, 2105, 6099, …

### Python 3 — 158 bytes

```python
L=[[n:=1]],
while[n<3or print(len(L)//n//2)]:L=[(x+[-n],p,*r)for p,*r in L for x in([],p,*r)if all((x<c)^(x<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))];n+=1
```

**How it works**

- **The formula.** a(n) = A000136(n + 1)/(2n + 2) for n ≥ 2, where A000136(m)
  counts the foldings of a strip of m labelled stamps. This is the OEIS
  formula line by Alcover (2019); it combines the OEIS formula
  a(n) = A000682(n + 1)/2 with A000136(m) = m·A000682(m), A000682 being the
  semi-meanders. The program builds every folding of m stamps and prints the
  count divided by 2m, for m = 3, 4, …
- **Foldings as heights.** A state lists the stamps' heights in the pile,
  newest stamp first. A height is a list compared lexicographically: the new
  stamp gets `x+[-n]`, which sorts just above x and below everything that
  was above x (those heights extend x by an older, so larger, marker −m, or
  differ from x earlier). With x = `[]` the new stamp goes to the bottom, and
  with x an old height it goes just above that stamp: all m + 1 gaps.
- **No crossing creases.** The new crease joins the new stamp to the
  previous newest one, p. Creases alternate between the two edges of the
  strip, so the old creases on the same edge are the pairs (r_0, r_1),
  (r_2, r_3), … of the older stamps r, which is `zip(*[iter(r)]*2)`. Two
  creases on one edge must nest or be disjoint: exactly when the new stamp
  and p are both between c and d or both outside, `(x<c)^(x<d)==(p<c)^(p<d)`.
  Comparing x instead of `x+[-n]` gives the same answer, also when c is x
  itself (then neither is below c).
- **The loop.** `L=[[n:=1]],` is the one folding of 1 stamp, of height
  `[1]`. Each pass makes the foldings of n + 1 stamps, then n becomes n + 1;
  printing starts once n = 3, where `len(L)//n//2` = 6/6 = 1 = a(2). Every
  folding comes from exactly one folding with its last stamp removed, so
  `len(L)` is A000136(n), and ⌊⌊x/n⌋/2⌋ = ⌊x/(2n)⌋.

**Notes**

- Other versions: the newest stamp as `q[0]` and the pairs as
  `zip(q[1::2],q[2::2])` is 160 bytes; the first entry, with a separate
  `if n>2:print(…)` and markers `-len(q)`, was 172.
- Correctness beyond the b-file rests on the OEIS formula a(n) =
  A000682(n + 1)/2 (with A000136(m) = m·A000682(m)); the folding count itself
  is exhaustive.
- About 12 terms in 60 s here: a(12) comes after about 15 s and a(13) at
  about 60 s. The whole list of foldings is held in memory, about 0.6 GB for
  the 14 stamps behind a(13), and each new stamp multiplies it by about 3.
- The b-file has 43 terms (up to a(44)); the bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 172 | first entry |
| 2026-11-07 | Python 3 | 158 | unpack `p,*r`, pairs from `zip(*[iter(r)]*2)`, print in the while header |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000560), CC BY-SA 4.0.
