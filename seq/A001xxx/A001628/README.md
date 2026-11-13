# A001628

> Convolved Fibonacci numbers.
> — [OEIS A001628](https://oeis.org/A001628)

Offset 0: 1, 3, 9, 22, 51, 111, 233, 474, 942, 1836, 3522, 6666, 12473, …

### Python 3 — 53 bytes

```python
a=n=0;b=1
while[print(b)]:n+=1;a,b=b,a+b+(4*a+2*b)//n
```

**How it works**

- The generating function is A = 1/(1 − x − x²)³. Differentiating,
  A′ = 3(1 + 2x)·A/(1 − x − x²), so (1 − x − x²)A′ = 3(1 + 2x)A. The
  coefficient of xⁿ⁻¹ on both sides gives, for n ≥ 1 (with a(−1) = 0),
  n·a(n) = (n + 2)·a(n−1) + (n + 4)·a(n−2),
  the recurrence on the OEIS page (Michael D. Weiner), here derived.
- Splitting off n(a(n−1) + a(n−2)) leaves
  a(n) = a(n−1) + a(n−2) + (4a(n−2) + 2a(n−1))/n, and that last quotient
  is an integer because everything else in the identity is: so `//n` is
  exact.
- `a`, `b` hold a(n−2), a(n−1); they start at a(−1) = 0, a(0) = 1, and
  the step for n = 1 gives a(1) = 3.

**Notes**

- Two variables and a counter beat the order-6 linear recurrence
  a(n) = 3a(n−1) − 5a(n−3) + 3a(n−5) + a(n−6) (a list of six terms) and
  the closed form ((5n+16)(n+1)F(n+2) + (5n+17)(n+2)F(n+1))/50 (about 75
  bytes with a Fibonacci pair).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 4501 terms (n = 0 to 4500); the bar is the whole b-file
  in 60 s, which prints in well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001628), CC BY-SA 4.0.
