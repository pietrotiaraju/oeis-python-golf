# A000050

> Number of positive integers <= 2^n of form x^2 + y^2.
> — [OEIS A000050](https://oeis.org/A000050)

Offset 0: 1, 2, 3, 5, 9, 16, 29, 54, 97, 180, 337, 633, 1197, 2280, 4357, …

### Python 3 — 91 bytes

```python
n=0
while r:=range(1<<-~n//2|3):print(len({min(x*x+y*y,2**n)for x in r for y in r})-1);n+=1
```

**How it works**

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2)
  ≤ 2^c, where c = ⌈n/2⌉ is `-~n//2`. `range(1<<-~n//2|3)` holds
  0 … 2^c: its length is 2^c + 3 for c ≥ 2, and 3 for c ≤ 1, where `|3`
  makes up for 2^c being 1 or 2. One range serves both variables.
- A range is truthy when it is not empty, so `while r:=range(…):` names the
  range and keeps the loop going, with the print and `n+=1` after the
  colon. That is 1 byte shorter than a `while 1:` body that assigns
  `r=range(…);`, and 5 bytes shorter than `while[print(…)]:n+=1`, which
  needs `[r:=range(…)]and` to name the range inside the expression,
  because a walrus may not appear in a comprehension's iterable.
- `min(x*x+y*y,2**n)` turns every sum above 2ⁿ into 2ⁿ. That adds nothing
  new to the set, because 2ⁿ is itself a sum of two squares with both roots
  in the range: (2^k)² + 0² when n = 2k, and (2^k)² + (2^k)² when
  n = 2k+1. So the set holds exactly the sums in [0, 2ⁿ], without an `if`
  filter.
- 0 = 0² + 0² is in the set and is not positive, so `-1` removes it.

**Speed**

- Term n costs |r|² pairs: about 2ⁿ for even n and 2ⁿ⁺¹ for odd n. The
  87-byte version used `range(2<<n//2)`, which is 2ⁿ⁺² pairs for even n.
- The bar is 25 terms in 60 s, and it must come within half the timeout,
  in reference seconds. The 87-byte version needed about 42 s on the
  GitHub runners; on the same local machine this one is 2.2 times faster,
  about 19 s. The b-file goes to n = 60, far beyond any enumeration.

**Notes**

- Running y only up to x (`r[:x+1]`, 6 more bytes) halves the work again.
- The filter version, `{v for x in r for y in r if(v:=x*x+y*y)>>n<1}` with
  no `-1`, is 3 bytes longer. It counts [0, 2ⁿ) and relies on the same
  fact: 0 is counted and 2ⁿ is left out, and the two cancel.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 88 | first entry |
| 2026-11-05 | Python 3 | 87 | range named in the while condition |
| 2026-11-08 | Python 3 | 91 | fix: range up to 2^⌈n/2⌉ only, so the bar comes within half the timeout |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000050), CC BY-SA 4.0.
