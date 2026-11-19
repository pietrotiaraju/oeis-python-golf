# A002005

> Number of rooted planar cubic maps with 2n vertices.
> — [OEIS A002005](https://oeis.org/A002005)

Offset 0: 1, 4, 32, 336, 4096, 54912, 786432, 11824384, 184549376, 2966845440, …

### Python 3 — 66 bytes

```python
a,b=1,4;k=0
while[print(a)]:k+=3;a,b=b,432*(k*k-1)*a//(k+6)//(k+9)
```

**How it works**

- **Formula.** The entry's closed form a(n) = 2^(2n+1)·(3n)!!/((n+2)!·n!!)
  is the classical count of rooted cubic maps (equivalently, rooted
  triangulations with 2n faces, loops and multiple edges allowed); see the
  entry's references (Mullin, Nemeth and Schellenberg, *The enumeration
  of almost cubic maps*, 1970). The root-edge recursion on the
  [A002006](../A002006/) page, which needs no formula, reproduces it for
  n ≤ 8. It is not
  a single ratio of factorials, because the double factorials alternate
  with the parity of n, but two steps are: dividing a(n) by a(n−2) leaves
  16·3n(3n−2)(3n−4)/n from the powers of 2 and the double factorials and
  1/((n+1)(n+2)) from the factorials, so
  (n+1)(n+2)·a(n) = 48(3n−2)(3n−4)·a(n−2), the entry's D-finite
  recurrence.
- **Golf.** With k = 3n − 3 the factors become 3n−2 = k+1, 3n−4 = k−1,
  n+1 = (k+6)/3 and n+2 = (k+9)/3, so a(n) = 432(k²−1)·a(n−2)/((k+6)(k+9)):
  one `k*k-1` instead of two linear factors. The pair (a, b) holds
  (a(n−2), a(n−1)) and steps by `a,b=b,…`; a(0) = 1 and a(1) = 4 start it.
- **Exact.** 432(k²−1)·a(n−2) equals (k+6)(k+9)·a(n), and nested floor
  divisions by positive integers equal one division by their product, so
  `//(k+6)//(k+9)` is exact.

**Notes**

- The same pair step drives [A002006](../A002006/), and the list version
  of it [A002007](../A002007/)–[A002010](../A002010/) (root vertex of
  valence 4 to 8).
- a(n) grows like (12√3)ⁿ, about 1.32·n digits, so the 4300-digit limit on
  printing an int stops the program near n = 3250. The b-file has 1001
  terms (n = 0 to 1000); the bar is the whole b-file in 60 s, which takes a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002005), CC BY-SA 4.0.
