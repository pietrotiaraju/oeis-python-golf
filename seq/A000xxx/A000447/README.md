# A000447

> a(n) = 1^2 + 3^2 + 5^2 + 7^2 + ... + (2*n-1)^2 = n*(4*n^2 - 1)/3.
> — [OEIS A000447](https://oeis.org/A000447)

Offset 0: 0, 1, 10, 35, 84, 165, 286, 455, 680, 969, …

### Python 3 — 34 bytes

```python
m=0
while[print((m**3-m)//6)]:m+=2
```

**How it works**

- Σ_{j=1}^{n} (2j−1)² = 4Σj² − 4Σj + n = n(4n² − 1)/3, the closed form in
  the name. With m = 2n this is (m−1)m(m+1)/6 = (m³ − m)/6 = C(m+1, 3).
- m³ − m is a product of three consecutive integers, so it is divisible
  by 6 and `//6` is exact.
- `m` runs over the even numbers 0, 2, 4, …, so there is no other
  variable; `while[print(…)]:m+=2` prints first in every pass.

**Notes**

- The running sum `s=0;n=1` / `while[print(s)]:s+=n*n;n+=2` is 35 bytes;
  n(4n² − 1)/3 directly, `n=0` / `while[print(n*(4*n*n-1)//3)]:n+=1`, is
  37.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints at once. The b-file has 1001 terms (up to
  a(1000)); the bar is the whole b-file in 60 s.
- a(n) ≈ 4n³/3 has only about 3·log₁₀ n digits, so the 4300-digit
  int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |
| 2026-11-07 | Python 3 | 34 | C(2n+1, 3) = (m³ − m)/6 with m = 2n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000447), CC BY-SA 4.0.
