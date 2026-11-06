# A000592

> Number of nonnegative solutions of x^2 + y^2 = z in first n shells.
> — [OEIS A000592](https://oeis.org/A000592)

Offset 0: 1, 3, 4, 6, 8, 9, 11, 13, 15, 17, …

### Python 3 — 100 bytes

```python
from math import*
a=n=0
while[a==(a:=sum(1+isqrt(n-x*x)for x in range(isqrt(n)+1)))or print(a)]:n+=1
```

**How it works**

- For a squared radius n, let F(n) count ordered nonnegative pairs
  with x²+y²≤n. For each x=0,…,floor(√n), the y coordinates
  are 0,…,floor(√(n−x²)), hence

  **F(n)=Σₓ₌₀^⌊√n⌋(1+floor(√(n−x²)))**.

- The difference F(n)−F(n−1) is the number of points on the
  shell x²+y²=n. Consequently a nonempty shell occurs precisely
  when the cumulative total changes; print that new total.
- In `a==(a:=...)`, Python reads the old a before assigning F(n)
  to the new a. If they are equal, `or` skips the print. Otherwise
  print the updated a. The enclosing one-element list stays truthy
  in both cases, and the loop advances n.
- With a initially zero, F(0)=1 prints the origin as the first
  shell. Swapped coordinates are distinct when unequal, and points
  on either axis are included.

**Notes**

- All nonnegative solutions are covered, including coordinates equal
  to zero. No floating point geometry is used.
- The reference file contains 2750 terms from the OEIS b-file; the verification
  bar is 2750 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |
| 2026-11-06 | Python 3 | 100 | count the quarter disk and print when its total changes |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000592), CC BY-SA 4.0.
