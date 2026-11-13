# A001601

> a(n) = 2*a(n-1)^2 - 1, if n>1. a(0)=1, a(1)=3.
> — [OEIS A001601](https://oeis.org/A001601)

Offset 0: 1, 3, 17, 577, 665857, 886731088897, 1572584048032918633353217, …

### Python 3 — 33 bytes

```python
a=1
while[print(a)]:a=a*a*2+1-2%a
```

**How it works**

- The definition: a(0) = 1, a(1) = 3 and a(n) = 2a(n−1)² − 1 for n > 1.
  Only the first step breaks the rule 2a² − 1, and it is the only step
  taken from a = 1; every later term is at least 3.
- `2%a` is 0 when a = 1 and 2 when a ≥ 3, so `a*a*2+1-2%a` is 3 for the
  first step and 2a² − 1 for all the others.

**Notes**

- a(n) = ((1 + √2)^(2ⁿ) + (1 − √2)^(2ⁿ))/2 is the companion Pell number
  H(2ⁿ) of [A001333](../A001333/). From H(m)² − 2P(m)² = (−1)ᵐ,
  H(2m) = 2H(m)² − (−1)ᵐ, so the + 1 appears exactly when m = 2ⁿ⁻¹ is odd,
  at n = 1.
- `print(1);a=3` with `a=2*a*a-1` is 38 bytes, and the correction
  `2*a*a-1+2//a` is 34.
- Exact integer arithmetic, so the program is right for every n. a(13) has
  3136 digits; a(14) has 6272, past Python's 4300-digit int-to-str limit,
  so the program stops there with a ValueError after 14 terms.
- The b-file has 12 terms (a(0) to a(11)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001601), CC BY-SA 4.0.
