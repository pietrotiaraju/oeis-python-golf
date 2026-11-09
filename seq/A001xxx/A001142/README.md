# A001142

> a(n) = Product_{k=1..n} k^(2k - 1 - n).
> — [OEIS A001142](https://oeis.org/A001142)

Offset 0: 1, 1, 2, 9, 96, 2500, 162000, 26471025, 11014635520, …

### Python 3 — 45 bytes

```python
a=f=n=1
while[print(a)]:f*=n;a=a*n**n//f;n+=1
```

**How it works**

- a(n) is the product of row n of Pascal's triangle:
  ∏ⱼ C(n, j) = n!^(n+1) / (∏ⱼ j!)², and the factor k sits once in n! and
  once in j! for each of the n−k+1 values j ≥ k, which leaves
  k^((n+1)−2(n−k+1)) = k^(2k−1−n).
- For k < n, C(n, k) = C(n−1, k)·n/(n−k), and C(n, n) = 1, so
  a(n) = a(n−1)·nⁿ/n!. The loop keeps f = n! (`f*=n`) and updates
  `a=a*n**n//f`; the floor division is exact because a(n−1)·nⁿ = a(n)·n!.
- Starting n at 1 lets one assignment `a=f=n=1` seed everything: the first
  pass gives a(1) = 1·1/1.
- `while[print(a)]:` prints in the loop test (`[None]` is a true list).

**Alternatives measured**

- `a=a*n**n//(f:=f*n)` instead of `f*=n;a=…//f` is 2 bytes longer.
- Hyperfactorial over superfactorial, a(n) = ∏ mᵐ / ∏ m!, with three
  running products and `print(h//s)`: 51 bytes.
- `math.prod(comb(n,k)for k in range(n+1))` after `from math import*`:
  75 bytes.

**Notes**

- Exact integer arithmetic, correct for every n. a(n) has about
  0.217·n² digits, so the program prints a(0)…a(143) and stops with a
  `ValueError` at a(144), past the 4300-digit int-to-str limit of
  Python 3.11+: an interpreter limit, not a wrong term. The bar is the
  whole b-file (51 terms) in 60 s; they print at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001142), CC BY-SA 4.0.
