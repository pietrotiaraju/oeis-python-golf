# A001242

> Differences of reciprocals of unity.
> — [OEIS A001242](https://oeis.org/A001242)

Offset 1: 1, 274, 48076, 6998824, 929081776, 117550462624, 14500866102976, …

### Python 3 — 61 bytes

```python
n=0
while[print(5*(120**n-30**n-2*60**n+2*40**n)+24**n)]:n+=1
```

**How it works**

- The OEIS entry gives the g.f. x/((1 − 24x)(1 − 30x)(1 − 40x)(1 − 60x)(1 − 120x))
  and the closed form a(n) = (24ⁿ − 4·30ⁿ + 6·40ⁿ − 4·60ⁿ + 120ⁿ)/24.
  Dividing by 24 term by term is exact once one factor of each base is
  pulled out: with m = n − 1, 120ⁿ/24 = 5·120ᵐ, 4·60ⁿ/24 = 10·60ᵐ,
  6·40ⁿ/24 = 10·40ᵐ, 4·30ⁿ/24 = 5·30ᵐ and 24ⁿ/24 = 24ᵐ, so
  a(m + 1) = 5·120ᵐ − 10·60ᵐ + 10·40ᵐ − 5·30ᵐ + 24ᵐ, with no division left.
- The coefficients are C(5, k) with alternating signs, and the four that
  are multiples of 5 share one `5*(…)`.
- The loop variable `n` is that m: it starts at 0, which prints a(1) = 1,
  so the offset shift costs nothing. Exact integers throughout.
- The title: 24·a(n)/120ⁿ = 1 − 4·2⁻ⁿ + 6·3⁻ⁿ − 4·4⁻ⁿ + 5⁻ⁿ = Δ⁴(x⁻ⁿ) at
  x = 1, the fourth difference of the reciprocal powers taken at unity;
  120 = 5! clears the denominators. [A001241](../A001241/) is the third
  difference, with 4! = 24.
- `while[print(…)]:` is one byte under `while 1:print(…);`: `print`
  returns `None`, so `[None]` is a non-empty, true list.

**Notes**

- Other groupings are as long or longer:
  `(120**n-30**n-2*(60**n-40**n))*5+24**n` is the same length,
  `5*(120**n-30**n)+10*(40**n-60**n)+24**n` is 1 byte longer, the plain
  `5*120**n-10*60**n+…` 2 bytes longer, and the OEIS form with `//24`
  at least 2 bytes longer.
- A recurrence needs five state values (signature 274, −27000, 1224000,
  −25920000, 207360000), so it cannot beat five powers.
- Python's 4300-digit int-to-str limit stops the program at a(2069), the
  first term with 4301 digits, after printing a(1) to a(2068).
- The b-file has 481 terms; all of them print instantly, and the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001242), CC BY-SA 4.0.
