# A000180

> Expansion of E.g.f. exp(-x)/(1-3x).
> — [OEIS A000180](https://oeis.org/A000180)

Offset 0: 1, 2, 13, 116, 1393, 20894, 376093, 7897952, 189550849, 5117872922, …

### Python 3 — 33 bytes

```python
a=n=0
while[print(a:=a*n^1)]:n+=3
```

**How it works**

- The terms satisfy a(n) = 3n·a(n−1) + (−1)^n (Werner Schulte's formula on
  the OEIS page), the derangement recurrence with n replaced by 3n.
- 3n·a(n−1) always has the parity of n: for even n it is even, and for odd
  n both factors are odd (a(n−1) is odd when n−1 is even, by induction: an
  even product plus 1 is odd). So for even n we add 1 to an even number and
  for odd n we subtract 1 from an odd one, and both are `^1`:
  a(n) = 3n·a(n−1) xor 1.
- `n` runs over 0, 3, 6, … and already stands for 3n, so there is no `3*`.
- The update happens inside `print` with a walrus, and the loop starts one
  step early: at n = 0 the product is 0 whatever `a` holds, and `0^1` is
  a(0) = 1. That is 3 bytes under `a=n=1` / `while[print(a)]:a=a*n*3^1;n+=1`.
- `*` binds tighter than `^`, and `:=` looser than both, so no parentheses.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (101 terms) prints at once; the program stops after a(1353), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000180), CC BY-SA 4.0.
