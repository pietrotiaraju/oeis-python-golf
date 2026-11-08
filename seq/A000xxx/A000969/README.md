# A000969

> Expansion of g.f. (1 + x + 2*x^2)/((1 - x)^2*(1 - x^3)).
> — [OEIS A000969](https://oeis.org/A000969)

Offset 0: 1, 3, 7, 12, 18, 26, 35, 45, 57, 70, 84, 100, 117, 135, 155, 176, 198, 222, 247, 273, …

### Python 3 — 30 bytes

```python
y=5
while[print(y*y//24)]:y+=4
```

**The formula**

The OEIS gives a(n) = ⌊(2n+3)(n+1)/3⌋ (Sloane). It matches the g.f.: the
floor is a quadratic polynomial minus a period-3 correction, so it is
annihilated by (1−x)³(1+x+x²) = (1−x)²(1−x³), the denominator of the g.f.;
both sides satisfy the same order-5 recurrence and agree on a(0..4).

With y = 4n+5,

y² = 16n² + 40n + 25 = 8(2n+3)(n+1) + 1, so y²/24 = (2n+3)(n+1)/3 + 1/24.

(2n+3)(n+1)/3 has fractional part 0, 1/3 or 2/3, and adding 1/24 never
reaches the next integer, so a(n) = ⌊y²/24⌋.

**How it works**

- `y` runs over 5, 9, 13, … (`y+=4`) and `y*y//24` is the term: no counter
  and no product of two different factors.
- `while[print(…)]:` prints in the loop test; the one-element list is
  always true.

**Notes**

- Exact integer arithmetic, correct for every n.
- The form ⌊k(k−1)/6⌋ with k = 2n+3 (`k=3` / `print(k*~-k//6)` / `k+=2`)
  is 31 bytes; n-based forms such as `n*(n-~n)//3` from n = 1 are 34.
- The b-file has 10001 terms; they print in about 0.2 s. The bar is the
  whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000969), CC BY-SA 4.0.
