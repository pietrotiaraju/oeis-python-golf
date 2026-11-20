# A001972

> Expansion of 1/((1-x)^2*(1-x^4)) = 1/( (1+x)*(1+x^2)*(1-x)^3 ).
> — [OEIS A001972](https://oeis.org/A001972)

Offset 0: 1, 2, 3, 4, 6, 8, 10, 12, 15, 18, 21, 24, 28, 32, 36, 40, 45, 50, 55, 60, 66, …

### Python 3 — 29 bytes

```python
n=3
while[print(n*n>>3)]:n+=1
```

**How it works**

- **Closed form.** a(n) = ⌊(n + 3)²/8⌋ (Michael Somos's formula in the
  entry). Multiplying the series by 1 − x⁴ leaves 1/(1 − x)², so
  a(n) − a(n − 4) = n + 1 for n ≥ 0, with a(n) = 0 for n < 0. The floor
  does the same: (n + 3)² − (n − 1)² = 8(n + 1) is a multiple of 8, so
  ⌊(n + 3)²/8⌋ − ⌊(n − 1)²/8⌋ = n + 1, and at n = −4, …, −1 the floor is
  ⌊1/8⌋, ⌊0/8⌋, ⌊1/8⌋, ⌊4/8⌋ = 0. By induction the two agree for every n.
- **Program.** `n` runs over n + 3 from 3, and `n*n>>3` floors n²/8.

**Notes**

- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001972), CC BY-SA 4.0.
