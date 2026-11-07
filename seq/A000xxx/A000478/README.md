# A000478

> Number of ways of placing n labeled balls into 3 indistinguishable boxes with at least 2 balls in each box.
> — [OEIS A000478](https://oeis.org/A000478)

Offset 6: 15, 105, 490, 1918, 6825, 22935, 74316, 235092, 731731, 2252341, …

### Python 3 — 47 bytes

```python
m=5
while[print(3**m+3-(m+3)*(2**m-m)>>1)]:m+=1
```

**How it works**

- A box with at least 2 balls has e.g.f. eˣ − 1 − x, so three unlabeled
  boxes have e.g.f. (eˣ − 1 − x)³/3!. Expanding the cube,
  (eˣ − 1 − x)³ = e³ˣ − 3(1+x)e²ˣ + 3(1+x)²eˣ − (1+x)³, and for n ≥ 4
  the coefficient of xⁿ/n! is 3ⁿ − 3(n+2)·2ⁿ⁻¹ + 3(n² + n + 1). So
  a(n) = (3ⁿ⁻¹ − (n+2)·2ⁿ⁻¹ + n² + n + 1)/2.
- With m = n − 1 the numerator is 3ᵐ − (m+3)·2ᵐ + m² + 3m + 3, which is
  `3**m+3-(m+3)*(2**m-m)`: the product (m+3)(2ᵐ − m) supplies the
  quadratic part.
- The numerator is 2a(n), so `>>1` halves it exactly; `>>` binds more
  loosely than `+` and `-`, so it needs no parentheses. m starts at 5
  for a(6) = 15.

**Notes**

- Kruchinin's recurrence a(n) = 3a(n−1) + (2ⁿ⁻³ − n + 1)(n − 1), as
  `a=0;m=5` / `while[print(a:=3*a+m*(2**m//4-m))]:m+=1`, is also 47
  bytes; the closed form over 12 with n itself was 61.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 195 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 9015, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 61 | first entry |
| 2026-11-07 | Python 3 | 47 | closed form in m = n − 1, halved with `>>1` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000478), CC BY-SA 4.0.
