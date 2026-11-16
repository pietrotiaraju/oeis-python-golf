# A001864

> Total height of rooted trees with n labeled nodes.
> — [OEIS A001864](https://oeis.org/A001864)

Offset 1: 0, 2, 24, 312, 4720, 82800, 1662024, 37665152, 952401888, …

### Python 3 — 68 bytes

```python
s=0;n=1
while[print(s*n*~-n)]:
 n+=1
 for i in range(n-1):s=s*i+n**i
```

**How it works**

- The total height of a rooted tree is the sum of the distances of its
  nodes from the root. Riordan and Sloane (*J. Austral. Math. Soc.* 10
  (1969)) showed that over all rooted trees on n labeled nodes it is
  a(n) = n!·Σ_{k=0}^{n−2} nᵏ/k! = n·[A000435](../../A000xxx/A000435/)(n),
  the formula on the OEIS page.
- With S(m) = Σ_{k=0}^{m} nᵏ·m!/k!, S(m) = m·S(m−1) + nᵐ and S(−1) = 0, so
  the loop `s=s*i+n**i` over i = 0…n−2 ends with s = S(n−2), and
  a(n) = n(n−1)·S(n−2) is printed as `s*n*~-n`.
- The first pass multiplies by i = 0, which wipes the previous n's value,
  so s needs no reset. At n = 1 the loop is empty and 0 = a(1) is printed.
  The same loop without the factor n(n−1) is
  [A001863](../A001863/).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 100 terms (n = 1 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001864), CC BY-SA 4.0.
