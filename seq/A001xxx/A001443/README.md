# A001443

> Number of strong starters in cyclic group of order 2n+1.
> — [OEIS A001443](https://oeis.org/A001443)

Offset 1: 0, 0, 2, 0, 4, 8, 32, 224, 800, 6660, 27554, 158680, 1201626, …

A starter in the cyclic group Z_v, v = 2n + 1, splits the v − 1 nonzero
elements into n pairs {x, y} so that every nonzero element is a difference
±(y − x) of exactly one pair; it is strong when the n sums x + y are
distinct and nonzero (Kocay et al. 1985, in the OEIS
references).

### Python 3 — 153 bytes

```python
g=lambda E,x=0,*U:x<1 or sum(g(E|{y-x,v+x-y,(x+y)%-v},*[u for u in U if u-y])for y in U if not{y-x,(x+y)%-v}&E)
v=3
while[print(g({0},*range(1,v)))]:v+=2
```

**How it works**

- **Pairing.** `g(E,x,*U)` gets the unpaired elements in increasing order:
  x is the smallest, and it is paired with each larger unpaired y in turn;
  the rest, `[u for u in U if u-y]`, stays sorted. Every starter is a set
  of pairs and comes out exactly once, through the partner of the smallest
  element at each step. When nothing is left, x takes its default 0 and
  `x<1` scores the completed starter.
- **One set for both rules.** As y > x, the two differences of the pair are
  the residues y − x and v − (y − x), both from 1 to v − 1. The sum is
  stored as `(x+y)%-v`, its residue shifted into −(v − 1)…0, so sums and
  differences never collide in E, and a sum ≡ 0 has code 0. E starts as
  `{0}`, which forbids that sum, and a pair is allowed when neither its
  difference nor its sum code is in E (`not{…}&E`; the difference v − (y −
  x) is in E exactly when y − x is, since both go in together).
- **Why that is enough.** The n pairs then have 2n = v − 1 distinct nonzero
  differences, so every nonzero element is a difference of exactly one
  pair: that is the starter condition. Distinct sum codes, none 0, is the
  strong condition.

**Notes**

- Exact integer search, no stored terms, nothing beyond the definition.
- The search counts every strong starter one by one, and the counts grow
  about eight times per term: a(11) = 27554 comes after about 52 s here,
  a(12) would need several minutes. The bar is 11 terms in 120 s (the
  b-file has 18). The recursion is n deep.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 153 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001443), CC BY-SA 4.0.
