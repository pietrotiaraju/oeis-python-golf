# A000124

> Central polygonal numbers (the Lazy Caterer's sequence): n(n+1)/2 + 1; or,
> maximal number of pieces formed when slicing a pancake with n cuts.
> — [OEIS A000124](https://oeis.org/A000124)

Offset 0: 1, 2, 4, 7, 11, 16, 22, 29, 37, 46, 56, 67, 79, 92, 106, 121, …

### Python 3 — 31 bytes

```python
a=k=1
while[print(a)]:a+=k;k+=1
```

**How it works**

- a(n) = n(n+1)/2 + 1, so a(n) − a(n−1) = n: the n-th cut crosses the
  n − 1 earlier ones and so splits n pieces in two.
- `a` is the current term and `k` the next difference. Both start at 1
  (a(0) = 1, a(1) − a(0) = 1), and each pass adds `k` to `a` and then
  steps `k` on, so the loop prints 1, 2, 4, 7, … forever.
- `while[print(a)]` is always true because `[None]` is a non-empty list,
  as in [A000027](../A000027/).

**Notes**

- Exact integer arithmetic, so it is right for every n.
- The closed form also gives 31 bytes: put m = 2n + 1, so m² = 8·T(n) + 1
  with T(n) = n(n+1)/2, and print `m*m//8+1` (or `m*m+7>>3`) from `m=1`
  with `m+=2`, the same trick as [A000096](../A000096/).
- In that shape the `+1` (or `+7`) can't be dropped. If m = kn + c and the
  quotient is m²/d, matching n²/2 + n/2 forces d = 2k² and c = k/2, which
  leaves m²/d = T(n) + 1/8, and `m*m//d` would print T(n), one less than
  a(n), every time.
- A brute-force search over every integer expression in `m` of up to 8
  bytes (operators `** * // % + - >> << & ^ |`, unary `-` and `~`,
  constants 0–99), with any start value and any step from −19 to 19,
  found only `1+m*m//8` and `7+m*m>>3` with m = 1, 3, 5, …. So the
  `m=…` / `while[print(…)]:m+=…` shape can't get below 31 bytes. The search
  doesn't cover two-variable loops like the one above.
- Other forms are longer: `n=0` + `while[print(1-n*~n//2)]:n+=1` is
  32 bytes, and `a=1;k=0` + `while[print(a:=a+k)]:k+=1` is 33.
- The b-file has the 1001 terms a(0)..a(1000), all printed in a fraction of
  a second; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000124), CC BY-SA 4.0.
