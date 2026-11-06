# A000481

> Stirling numbers of the second kind, S(n,5).
> — [OEIS A000481](https://oeis.org/A000481)

Offset 5: 1, 15, 140, 1050, 6951, 42525, 246730, 1379400, 7508501, 40075035, …

### Python 3 — 57 bytes

```python
a=b=c=d=1
while[print(a)]:d=2*d+1;c=3*c+d;b=4*b+c;a=5*a+b
```

**How it works**

- Removing the initial x⁵ from the Stirling column's generating
  function gives Σₘ≥₀ S(m+5,5)xᵐ=∏ⱼ₌₁⁵(1−jx)⁻¹.
  Let h_j(m) be the coefficient after only the first j factors.
- Multiplying the relation H_j(x)=H_(j−1)(x)/(1−jx) through
  gives **h_j(m)=j·h_j(m−1)+h_(j−1)(m)**. All h_j(0)=1,
  while h_1(m)=1 for every m.
- At each print, `d,c,b,a` hold h_2(m), h_3(m), h_4(m), h_5(m).
  Update in that order: the value from the previous level must already
  be from the new row. Thus `d=2*d+1` feeds `c=3*c+d`, which
  feeds b, which feeds a.
- Initially all four states are 1 and the print is S(5,5)=1.
  After one pass their values are 3,6,10,15, so the next print is
  S(6,5)=15. No explicit index counter is needed.

**Notes**

- Exact integer additions and multiplications. This stores four
  coefficients rather than a growing triangle or the five powers
  in a direct inclusion-exclusion formula.
- The update order is the reverse of the old-row dependency in the
  unsigned first-kind loop [A000482](../A000482/): these generating
  function factors require the newly updated lower level.
- [A000453](../A000453/) is the four-block column. Here the offset
  five is absorbed by using m=n−5 in the generating function.
- The coefficients grow exponentially; Python 3.11+ eventually meets
  its default 4300-digit output conversion limit, an interpreter limit.
- The b-file has 196 terms (indices 5 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000481), CC BY-SA 4.0.
