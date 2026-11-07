# A000657

> Median Euler numbers (the middle numbers of Arnold's shuttle triangle).
> — [OEIS A000657](https://oeis.org/A000657)

Offset 0: 1, 1, 4, 46, 1024, 36976, 1965664, 144361456, 13997185024, 1731678144256, 266182076161024, …

### Python 3 — 78 bytes

```python
r=[1]
while[print(r[len(r)//2])]:
 for t in 0,0:r=[t:=t+x for x in[0]+r[::-1]]
```

**How it works**

- Arnold's shuttle triangle is the Seidel–Entringer triangle
  [A008280](https://oeis.org/A008280) of [A000111](../A000111/): each row
  is the running sums of 0 followed by the row above read backwards.
  a(n) is the middle entry of row 2n.

  ```
  1                      a(0) = 1
  0  1
  0  1  1                a(1) = 1
  0  1  2  2
  0  2  4  5  5          a(2) = 4
  0  5 10 14 16 16
  0 16 32 46 56 61 61    a(3) = 46
  ```

  A008280 writes the even rows the other way round, which does not move
  the middle of an odd-length row.
- Each pass of the `while` builds two rows. `t` is the `for` target, so it
  is 0 when each comprehension starts; the `[0]` in front gives the row its
  leading 0 and the walrus carries the running sum.
- Row 2n has 2n+1 entries, so its middle is `r[len(r)//2]`.

**Notes**

- The same two-rows-per-pass layout as [A000191](../A000191/).
  Building one row per pass with `exec('…;'*2)` is the same length; printing
  only on odd-length rows is longer.
- The values were checked against Kruchinin's formula
  a(n) = (−1)ⁿ Σ C(n,k)·E(n+k), E the Euler (secant) numbers, for every
  printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(830); the 830 terms
  before it print in about a second.
- The b-file has 201 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000657), CC BY-SA 4.0.
