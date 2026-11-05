# A000148

> Number of partitions into non-integral powers.
> — [OEIS A000148](https://oeis.org/A000148)

Offset 2: 1, 2, 7, 15, 28, 45, 70, 100, 138, 183, 242, 310, 388, 481, 583, 701, …

### Python 3 — 102 bytes

```python
n=2
while[print(sum((n**3-x*x-y*y)**3>=27*(n*x*y)**2*n for y in range(n*n)for x in range(-y,0)))]:n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the pairs 1 ≤ x ≤ y of integers
  with x^(2/3) + y^(2/3) ≤ n. The program tries every such pair with
  y < n², which is enough: y^(2/3) ≤ n − 1 forces y ≤ (n − 1)^(3/2) < n².
- The test below only sees x², so the smaller number runs over −y, …, −1
  instead of 1, …, y: `range(-y,0)` is a byte shorter than `range(1,y+1)`.
- The test is exact. Write u = x^(2/3), v = y^(2/3) and s = u + v. Cubing,
  s³ = x² + y² + 3uv·s, so s is the root of g(t) = t³ − 3uv·t = x² + y².
  g increases for t ≥ √(uv), and s ≥ 2√(uv) lies in that range. So s ≤ n
  exactly when g(n) ≥ x² + y², that is when m = n³ − x² − y² ≥ 3n·uv.
- Both sides of m ≥ 3n·uv are cubed into integers: m³ ≥ 27n³x²y², written
  `27*(n*x*y)**2*n`. If m < 0 the left side is negative and the test fails,
  as it should (then s³ > x² + y² > n³). If n < √(uv), g(n) < 0 and the test
  fails too, matching s ≥ 2√(uv) > n. Equality s = n, as for x = y = 1 at
  n = 2, passes on both sides.

**Notes**

- Round n tries about n⁴/2 pairs, so the program prints about 52 terms in
  60 s. The bar is 40 terms in 60 s.
- `range(y+1)` with the chain `0<27*(n*x*y)**2*n<=…` to throw out x = 0
  comes to 103 bytes, as does `range(1,y+1)`.
- Naming m³ or n³ in a variable costs more than the two `n` it saves.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000148), CC BY-SA 4.0.
