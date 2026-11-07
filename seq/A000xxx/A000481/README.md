# A000481

> Stirling numbers of the second kind, S(n,5).
> — [OEIS A000481](https://oeis.org/A000481)

Offset 5: 1, 15, 140, 1050, 6951, 42525, 246730, 1379400, 7508501, 40075035, …

### Python 3 — 55 bytes

```python
a=b=c=d=1
while[print(a)]:d-=~d;c=3*c+d;b=4*b+c;a=5*a+b
```

**How it works**

- Σ_m S(m+5,5)·xᵐ = 1/((1−x)(1−2x)(1−3x)(1−4x)(1−5x)). Write h_j(m) for
  the coefficient of xᵐ in the product of the first j factors; then
  H_j = H_{j−1}/(1 − jx) gives h_j(m) = j·h_j(m−1) + h_{j−1}(m), with
  h_1(m) = 1 and h_j(0) = 1. So S(m+5,5) = h_5(m).
- `d`, `c`, `b`, `a` hold h_2, h_3, h_4, h_5. Each line of the recurrence
  needs the lower level of the same m, so they update upwards, each one
  reading the value just written.
- `d-=~d` is d − (−d − 1) = 2d + 1, the h_2 step with h_1 = 1, 2 bytes
  under `d=2*d+1`.
- All four start at h_j(0) = 1, so the first print is S(5,5) = 1.

**Notes**

- The inclusion–exclusion formula
  (5ⁿ − 5·4ⁿ + 10·3ⁿ − 10·2ⁿ + 5)/120 in a `while[print(…)]:n+=1` loop is
  59 bytes; reading S(n,5) off Bⁿ//((B−1)(B−2)(B−3)(B−4)(B−5)) with
  `math.perm(B-1,5)` and B = 6ⁿ is 67.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 196 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 6155, so printing stops
  there with a ValueError.
- [A000453](../A000453/) is the column S(n,4).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |
| 2026-11-07 | Python 3 | 55 | `d-=~d` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000481), CC BY-SA 4.0.
