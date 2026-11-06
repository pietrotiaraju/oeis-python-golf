# A000565

> Number of discordant permutations.
> — [OEIS A000565](https://oeis.org/A000565)

Offset 7: 31, 696, 5823, 29380, 108933, 327840, 848380, 1958004, 4130895, 8107024, …

### Python 3 — 94 bytes

```python
a=[31,665,4462,13968,23598,22194,10935,2187]
while[print(a[0])]:a=[*map(sum,zip(a,a[1:]+[0]))]
```

**How it works**

- OEIS gives the degree-7 polynomial
  P(n)=(243n⁷−8505n⁶+125685n⁵−1005795n⁴+4606392n³−
  11470340n²+12154480n)/560 for n≥7.
- The initial list contains ΔʲP(7), for j=0,…,7, where
  ΔP(n)=P(n+1)−P(n). These eight constants encode that polynomial;
  they are not a list of consecutive sequence terms. The last is
  2187=7!·243/560, and every eighth difference vanishes.
- Advancing n replaces each difference by itself plus the following
  one. `zip(a,a[1:]+[0])` forms these pairs, including the final pair
  with zero, and `map(sum,...)` performs the eight updates.
- `a[0]` is P(n), so printing before the update starts at P(7)=31 and
  produces the entire polynomial sequence using integer additions.

**Notes**

- Forward differences remove divisions and powers from the output loop.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 24 terms from the published OEIS entry; the verification
  bar is 24 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000565), CC BY-SA 4.0.
