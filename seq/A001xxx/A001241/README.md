# A001241

> Differences of reciprocals of unity.
> — [OEIS A001241](https://oeis.org/A001241)

Offset 1: 1, 50, 1660, 46760, 1217776, 30480800, 747497920, 18139003520, …

### Python 3 — 50 bytes

```python
n=0
while[print(4*24**n-6*12**n+4*8**n-6**n)]:n+=1
```

**How it works**

- The OEIS entry gives the g.f. x/((1 − 6x)(1 − 8x)(1 − 12x)(1 − 24x)) and
  the closed form a(n) = (24ⁿ − 3·12ⁿ + 3·8ⁿ − 6ⁿ)/6. Dividing the 24ⁿ/6 by
  the 6 term by term is exact once one factor of each base is pulled out:
  with m = n − 1, 24ⁿ/6 = 4·24ᵐ, 3·12ⁿ/6 = 6·12ᵐ, 3·8ⁿ/6 = 4·8ᵐ and
  6ⁿ/6 = 6ᵐ, so a(m + 1) = 4·24ᵐ − 6·12ᵐ + 4·8ᵐ − 6ᵐ, with no division left.
- The loop variable `n` is that m: it starts at 0, which prints a(1) = 1,
  so the offset shift costs nothing. Exact integers throughout.
- The title: 6·a(n)/24ⁿ = 1 − 3·2⁻ⁿ + 3·3⁻ⁿ − 4⁻ⁿ = −Δ³(x⁻ⁿ) at x = 1,
  the third difference of the reciprocal powers taken at unity (David,
  Kendall and Barton tabulate these); 24 = 4! clears the denominators.
- `while[print(…)]:` is one byte under `while 1:print(…);`: `print`
  returns `None`, so `[None]` is a non-empty, true list.

**Notes**

- The coefficients 4, 6, 4, 1 are C(4, k); `4*(24**n+8**n)-6*12**n-6**n`
  is the same length, and the original form with `//6` is 4 bytes longer.
  Pulling out 6ⁿ (`6**n*(4*4**n-6*2**n-1)+4*8**n`) is 2 bytes longer.
- A recurrence needs four state values (signature 50, −840, 5760, −13824),
  so it cannot beat four powers.
- Python's 4300-digit int-to-str limit stops the program at a(3117), the
  first term with 4301 digits, after printing a(1) to a(3116).
- The b-file has 700 terms; all of them print instantly, and the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001241), CC BY-SA 4.0.
