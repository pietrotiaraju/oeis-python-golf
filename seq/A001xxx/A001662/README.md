# A001662

> Coefficients of Airey's converging factor.
> — [OEIS A001662](https://oeis.org/A001662)

Offset 0: 0, 1, 1, −1, −1, 13, −47, −73, 2447, −16811, −15551, 1726511, …

### Python 3 — 104 bytes

```python
import math
a=[0,1];m=0
while[print(a[m])]:m+=1;a+=a[m]-sum(math.comb(m,k)*a[k]*a[-k]for k in range(m)),
```

**How it works**

- The entry gives the e.g.f. A(x) = Σ a(n)xⁿ/n! = (W(e^(4x+1)) − 1)/2,
  with W the Lambert function (Kruchinin), equivalent to Bernstein and
  Sloane's functional equation. Put w = 1 + 2A: w·e^w = e^(1+4x), so
  2A + ln(1 + 2A) = 4x. Differentiating and clearing the denominator gives
  A′·(1 + A) = 1 + 2A, that is A′ = 1 + 2A − A·A′, with a(0) = 0 (W(e) = 1)
  and a(1) = 1.
- Comparing the coefficients of xᵐ/m! for m ≥ 1:
  a(m+1) = 2a(m) − Σ_{k=0..m} C(m,k)·a(k)·a(m+1−k). The k = 0 term is 0
  (a(0) = 0) and the k = m term is a(m)·a(1) = a(m), so
  a(m+1) = a(m) − Σ_{k=0..m−1} C(m,k)·a(k)·a(m+1−k), the recurrence the
  entry quotes from Gutkovskiy in another form.
- The list holds a(0) … a(m), so `a[-k]` is a(m+1−k) for k ≥ 1, and for
  k = 0 `a[-0]` is a(0) = 0, which keeps that term 0 as it should.
  `while[print(a[m])]` prints a(m) and the body appends a(m+1), so the list
  stays one term ahead of the output.

**Notes**

- Exact integer arithmetic (the binomial convolution has integer
  coefficients), so every term is right. The whole b-file (201 terms)
  prints in a fraction of a second; the bar is the whole b-file.
- Keeping the k = m term, `2*a[m]-sum(…range(m+1))`, is 4 bytes longer.
  Summing the second-order Eulerian numbers of each row with alternating
  signs (the Maple program) is also longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 104 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001662), CC BY-SA 4.0.
