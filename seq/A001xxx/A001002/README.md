# A001002

> Number of dissections of a convex (n+2)-gon into triangles and quadrilaterals by nonintersecting diagonals.
> — [OEIS A001002](https://oeis.org/A001002)

Offset 0: 1, 1, 3, 10, 38, 154, 654, 2871, 12925, 59345, 276835, 1308320, …

### Python 3 — 62 bytes

```python
n=1
while[print(pow(1-(B:=8**n)-B*B,-n,B**n)//B**~-n//n)]:n+=1
```

**Why the formula**

- Cutting at the cell on a fixed edge gives the g.f. equation
  A = 1 + xA² + x²A³ (in the entry). Then A(1 − xA − x²A²) = 1, so
  u = xA satisfies u = x/(1 − u − u²), and Lagrange inversion gives
  Ilya Gutkovskiy's formula from the entry:

  **a(n) = [t^n] (1 − t − t²)^(−(n+1)) / (n+1).**

**How it works**

- In the code `n` is m = n + 1, so the term is c/m with
  c = [t^(m−1)] (1 − t − t²)^(−m).
- The whole series (1 − t − t²)^(−m) mod t^m, evaluated at t = B, is a
  residue mod B^m: `pow(1-B-B*B,-n,B**n)` (Python's modular inverse; the
  base is odd, so it is a unit mod B^m = 8^(m²)).
- Its coefficients c_j (j < m) are nonnegative and smaller than B:
  1/(1 − t − t²) has Fibonacci coefficients ≤ 2^j, so
  c_j ≤ C(m+j−1, j)·2^j < 2^(m+j−1)·2^j ≤ 2^(3m−3) < 8^m = B. The residue
  is therefore exactly Σ c_j B^j, and `//B**~-n` reads its top digit
  c_(m−1); `//n` divides by m.
- `B` is bound by a walrus inside the call, so the loop is the one-line
  `while[print(…)]:n+=1`.

**Notes**

- Exact integer arithmetic, correct for every n; the bound above makes the
  digit extraction rigorous.
- The numbers have about 3m² bits, so the modular inverse and power get
  slow: about 270 terms in 60 s here (200 in 13 s). The b-file has 1373
  terms; the bar is 210 terms in 60 s. Len Smiley's recurrence
  5n(n+1)a(n) = 11n(2n−1)a(n−1) + 3(3n−2)(3n−4)a(n−2) is fast but about
  85 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001002), CC BY-SA 4.0.
