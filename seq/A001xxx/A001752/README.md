# A001752

> Expansion of 1/((1+x)*(1-x)^5).
> — [OEIS A001752](https://oeis.org/A001752)

Offset 0: 1, 4, 11, 24, 46, 80, 130, 200, 295, 420, 581, 784, 1036, 1344, 1716, …

### Python 3 — 37 bytes

```python
m=3
while[print((m*m-2)**2//48)]:m+=1
```

**How it works**

- Partial fractions split 1/((1 + x)(1 − x)⁵) into (1/32)/(1 + x) plus
  multiples of 1/(1 − x)ʲ for j = 1, …, 5, so a(n) = P(n) + (−1)ⁿ/32 with P a
  polynomial of degree 4. Matching five values gives the formula on the OEIS
  page, a(n) = (2n⁴ + 24n³ + 100n² + 168n + 93 + 3(−1)ⁿ)/96.
- Put m = n + 3 and s = m². Since 2s² − 8s + 3 expands to
  2n⁴ + 24n³ + 100n² + 168n + 93, P = (2s² − 8s + 3)/96. Then
  (s − 2)²/48 = (2s² − 8s + 8)/96 = P + 5/96, which is a(n) + 1/48 for even n
  and a(n) + 1/12 for odd n. Both offsets lie in [0, 1), so
  a(n) = ⌊(m² − 2)²/48⌋ for every n ≥ 0.
- `m` runs from 3 (n = 0) and `//48` takes the floor exactly.

**Notes**

- The OEIS formula ⌊((n + 3)² − 1)((n + 3)² − 3)/48⌋ is the same idea:
  (s − 1)(s − 3) = (s − 2)² − 1. Written out it is 5 bytes longer.
- The rest of the family uses a(n) + a(n − 1) = C(n + k − 1, k − 1); here
  that is `a=0;c=n=1\nwhile[print(a:=c-a)]:c+=4*c//n;n+=1`, 45 bytes. For
  k ≥ 6 the polynomial is longer than the recurrence.
- Exact integer arithmetic, so the program is right for every n.
- The family 1/((1 + x)(1 − x)ᵏ): A001752 (k = 5), [A001753](../A001753/) (k = 6), [A001769](../A001769/) (k = 7), [A001779](../A001779/) (k = 8), [A001780](../A001780/) (k = 9), [A001781](../A001781/) (k = 10), [A001786](../A001786/) (k = 11).
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001752), CC BY-SA 4.0.
