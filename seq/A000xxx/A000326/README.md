# A000326

> Pentagonal numbers: a(n) = n*(3*n-1)/2.
> — [OEIS A000326](https://oeis.org/A000326)

Offset 0: 0, 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176, 210, 247, 287, …

### Python 3 — 30 bytes

```python
m=1
while[print(m*m//24)]:m-=6
```

**How it works**

- Complete the square: 24·n(3n − 1)/2 = 36n² − 12n = (6n − 1)² − 1, so
  a(n) = ((6n − 1)² − 1)/24.
- 6n − 1 is prime to 6, and the square of any number prime to 6 is 1 mod 24,
  so `m*m//24` is exactly (m² − 1)/24 for m = ±(6n − 1).
- Only m² matters, so m can run through 1 − 6n = 1, −5, −11, … instead of
  6n − 1 = −1, 5, 11, …: the start `m=1` is a byte under `m=-1`.
- `while[print(…)]:` is a non-empty list, so it is always true, as in the
  triangular numbers of [A000217](../A000217/), which use `m*m>>3` the same
  way.

**Notes**

- Exact integer arithmetic, so it is right for every n.
- The direct formula, `n=0` + `while[print(n*3*n-n>>1)]:n+=1`, is 33 bytes,
  and so is the running sum `a=0;k=1` + `while[print(a)]:a+=k;k+=3`.
- No shorter square works: with m = kn + c, `m*m//d` matching 3n²/2 forces
  d = 2k²/3, and the linear term −n/2 forces c = −k/6. So k is a multiple
  of 6 and d is at least 24 (k = 12 gives `m*m//96` with a two-digit step).
  A power of two (`m*m>>s`) would need 2k² = 3·2^s, which has no solution.
- A brute-force search over every integer expression in `m` of up to
  6 bytes (operators `** * // % + - >> << & ^ |`, unary `-` and `~`,
  constants 0–99), with any start value from −99 to 99 and any step from −19
  to 19, found nothing. So this frame needs at least the 7 bytes of
  `m*m//24`.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000326), CC BY-SA 4.0.
