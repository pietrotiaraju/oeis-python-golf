# A000431

> Expansion of 2*x^3/((1-2*x)^2*(1-4*x)).
> — [OEIS A000431](https://oeis.org/A000431)

Offset 0: 0, 0, 0, 2, 16, 88, 416, 1824, 7680, 31616, …

a(n) = 2^(n−3)·(2ⁿ − 2n) for n ≥ 1, the coefficients of the rational
generating function in the name.

### Python 3 — 37 bytes

```python
n=0
while[print(2**n-2*n<<n>>3)]:n+=1
```

**How it works**

- Partial fractions: 1/((1−2x)²(1−4x)) = 4/(1−4x) − 2/(1−2x) − 1/(1−2x)²,
  whose coefficient of x^m is 4^(m+1) − (m+3)·2^m. Multiplying by 2x³,
  a(n) = 2·4^(n−2) − 2n·2^(n−3) = 2ⁿ(2ⁿ − 2n)/8 for n ≥ 3, and the same
  expression is 0 at n = 1, 2.
- `2**n-2*n<<n>>3` is ⌊(2ⁿ − 2n)·2ⁿ/8⌋: `-` binds tighter than the shifts,
  which group from the left. 2ⁿ ≥ 2n for every n ≥ 0, so the shifted value is
  never negative and `>>3` is the floor of the division by 8. It is exact for
  n ≥ 1, and at n = 0 it turns the formula's 1/8 into the correct a(0) = 0.

**Notes**

- `2**n*(2**n-2*n)//8` with the same loop: 41 bytes (42 with
  `while 1:print(…);n+=1`); `4**n//8-n*2**n//4`: 40.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s.
- a(7144) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 42 | first entry |
| 2026-11-07 | Python 3 | 37 | shifts: `2**n-2*n<<n>>3` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000431), CC BY-SA 4.0.
