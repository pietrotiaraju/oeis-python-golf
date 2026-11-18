# A001970

> Functional determinants; partitions of partitions; Euler transform applied twice to all 1's sequence.
> — [OEIS A001970](https://oeis.org/A001970)

Offset 0: 1, 1, 3, 6, 14, 27, 58, 111, 223, 424, 817, 1527, 2870, 5279, 9710, …

### Python 3 — 107 bytes

```python
*L,n=1,1,0
while[print(L[-1])]:
 n-=2
 for h in 0,1:L+=sum(d*L[-d*h]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- **Two Euler transforms.** The partition numbers p(k) are the Euler
  transform of 1, 1, 1, …, and a(n) is the Euler transform of p:
  Σ a(n)·x^n = Π_{k≥1} (1 − x^k)^(−p(k)) (Cayley). For an Euler transform
  b = ET(c), the logarithmic derivative gives

  m·b(m) = Σ_{k≥1} k·c(k)·(b(m−k) + b(m−2k) + …),

  so p uses weight k·1 and a uses weight k·p(k).
- **One interleaved list.** `L` holds p(0), a(0), p(1), a(1), …, and
  n = −2m when the m-th pair is built (the template of
  [A000235](../../A000xxx/A000235/)). With d = −2k running over even
  values, the slice `L[d::d]` taken when L has 2m entries is p(m−k),
  p(m−2k), …; one entry later, with p(m) appended, the same slice is
  a(m−k), a(m−2k), …. Dividing by n = −2m turns d = −2k into k/m.
- **The weights.** The pass `h=0` reads `L[0]` = p(0) = 1, so it is the
  partition recurrence and appends p(m). The pass `h=1` reads `L[-d]` =
  L[2k] = p(k), including the p(m) just appended, and appends a(m).
- `*L,n=1,1,0` starts with p(0) = a(0) = 1 and n = 0; the loop prints the
  last entry, a(m), before building the next pair.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The two passes cost about 2·m·ln m additions for the m-th pair; the bar
  is 4000 of the 8998 b-file terms in 60 s (about 24 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001970), CC BY-SA 4.0.
