# A000309

> Number of rooted planar bridgeless cubic maps with 2n nodes.
> — [OEIS A000309](https://oeis.org/A000309)

Offset 0: 1, 1, 4, 24, 176, 1456, 13056, 124032, 1230592, 12629760, 133186560, 1436098560, 15774990336, …

### Python 3 — 55 bytes

```python
a=j=1
while[print(a)]:a=a*27*j*-~j//(j+5)//(2*j+7);j+=3
```

**How it works**

- a(n) = 2ⁿ·(3n)!/((n+1)!·(2n+1)!), so a(n)/a(n−1) =
  3(3n−1)(3n−2)/((n+1)(2n+1)).
- With j = 3n − 2 the ratio is 27·j·(j+1)/((j+5)(2j+7)): 3n − 1 = j + 1,
  and 3(n+1) = j + 5, 3(2n+1) = 2j + 7. j steps by 3.
- j = 1 at the first step (n = 1), the same start value as a(0) = 1, so
  `a=j=1` sets both.

**Notes**

- The numerator a(n−1)·27j(j+1) equals a(n)·(j+5)(2j+7), so the two floor
  divisions in a row are one exact division.
- This is [A000139](../A000139/) times 2^(n−1), and its step
  `a*27*m*~-m//-~(m:=m+3)//(4*m-2)` (with m = 3n − 1) works here too as
  `//(2*m-1)`: that step is as long as the one above, but m starts at 2,
  and `a=1;m=2` makes the program 57 bytes. Starting j at 1 with the
  walrus, `//(2+(j:=j+3))//(2*j+1)`, is also 2 bytes longer.
- Exact integer arithmetic, so the program is right for every n. a(3813)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted
  as a failure.
- The b-file has 101 terms (n = 0 to 100); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000309), CC BY-SA 4.0.
