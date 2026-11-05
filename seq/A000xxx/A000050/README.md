# A000050

> Number of positive integers <= 2^n of form x^2 + y^2.
> — [OEIS A000050](https://oeis.org/A000050)

Offset 0: 1, 2, 3, 5, 9, 16, 29, 54, 97, 180, 337, 633, 1197, 2280, 4357, …

### Python 3 — 87 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(x*x+y*y,2**n)for x in r for y in r})-1);n+=1
```

**How it works**

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2),
  and `range(2<<n//2)` goes past that bound for every n, so one range
  serves both variables. It is the [A000018](../A000018/) enumeration.
- A range is truthy when it is not empty, so `while r:=range(2<<n//2):`
  names the range and keeps the loop going, with the print and `n+=1`
  after the colon. That is 1 byte shorter than a `while 1:` body that
  assigns `r=range(…);`, and 5 bytes shorter than `while[print(…)]:n+=1`,
  which needs `[r:=range(…)]and` to name the range inside the expression,
  because a walrus may not appear in a comprehension's iterable.
- `min(x*x+y*y,2**n)` turns every sum above 2ⁿ into 2ⁿ. That adds nothing
  new to the set, because 2ⁿ is itself a sum of two squares: (2^k)² + 0² when
  n = 2k, and (2^k)² + (2^k)² when n = 2k+1. So the set holds exactly the
  sums in [0, 2ⁿ], without an `if` filter.
- 0 = 0² + 0² is in the set and is not positive, so `-1` removes it.

**Notes**

- The filter version, `{v for x in r for y in r if(v:=x*x+y*y)>>n<1}` with
  no `-1`, is 91 bytes. It counts [0, 2ⁿ) and relies on the same fact: 0 is
  counted and 2ⁿ is left out, and the two cancel.
- Term n costs (2<<n//2)² pairs, between 2ⁿ⁺¹ and 2ⁿ⁺² of them, and the set
  grows to a(n) elements. The program prints a(0)…a(24) in about 25 s and
  a(25) at about 45 s. The bar is 25 terms in 60 s; the b-file goes to
  n = 60, far beyond any enumeration.
- The 88-byte version had a `while 1:` body starting `r=range(2<<n//2);`.
  It runs at the same speed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 88 | first entry |
| 2026-11-05 | Python 3 | 87 | range named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000050), CC BY-SA 4.0.
