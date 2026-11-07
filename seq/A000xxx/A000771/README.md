# A000771

> Stirling numbers of second kind, S(n,7).
> — [OEIS A000771](https://oeis.org/A000771)

Offset 7: 1, 28, 462, 5880, 63987, 627396, 5715424, 49329280, 408741333, 3281882604, …

### Python 3 — 63 bytes

```python
L=[s:=1]*6
while[print(s)]:s=j=1;L=[s:=(j:=j+1)*x+s for x in L]
```

**How it works**

- Σ_m S(m+7,7)·xᵐ = 1/((1−x)(1−2x)···(1−7x)). Write h_k(m) for the
  coefficient of xᵐ in the product of the first k factors; then
  H_k = H_{k−1}/(1 − kx) gives h_k(m) = k·h_k(m−1) + h_{k−1}(m), with
  h_1(m) = 1 and h_k(0) = 1. So a(m+7) = h_7(m).
- `L` holds h_2(m), …, h_7(m). The new row is a running sum: with `s` =
  h_1 = 1 and `j` counting 2, 3, …, 7, `s:=(j:=j+1)*x+s` turns h_k(m−1)
  into h_k(m) and keeps it in `s` for the next level. After the
  comprehension `s` is h_7(m), the term to print.
- `L=[s:=1]*6` starts every level at h_k(0) = 1 and sets `s` for the first
  print, S(7,7) = 1.
- This is the program of [A000770](../A000770/) with a list one longer:
  the length of `L` picks the column.

**Notes**

- The unrolled chain (`a=b=c=d=e=f=1` / `while[print(a)]:f-=~f;e=3*e+f;…;a=7*a+b`,
  as in [A000481](../A000481/)) is 75 bytes; the inclusion–exclusion
  formula (7ⁿ − 7·6ⁿ + 21·5ⁿ − 35·4ⁿ + 35·3ⁿ − 21·2ⁿ + 7)/5040 in a
  `while[print(…)]:n+=1` loop is 76.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 194 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 5093, so printing stops
  there with a ValueError (about one second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000771), CC BY-SA 4.0.
