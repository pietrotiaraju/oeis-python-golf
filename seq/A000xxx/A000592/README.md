# A000592

> Number of nonnegative solutions of x^2 + y^2 = z in first n shells.
> — [OEIS A000592](https://oeis.org/A000592)

Offset 0: 1, 3, 4, 6, 8, 9, 11, 13, 15, 17, …

The shells are the values z = 0, 1, 2, 4, 5, 8, 9, 10, … that are sums of two
squares; a(n) counts the pairs (x, y) of nonnegative integers (ordered, so
(1, 2) and (2, 1) are different) with x² + y² on one of the shells number
0, …, n, that is with x² + y² ≤ the n-th such z.

### Python 3 — 75 bytes

```python
a=n=0;S={0}
while[a<(a:=a+len(S&{n-s for s in S}))!=print(a)]:n+=1;S|={n*n}
```

**How it works**

- **Points on one circle.** When the condition runs, `S` is {0², 1², …, n²}.
  `{n-s for s in S}&S` is the set of squares s = x² whose complement n − s is
  also a square y², and each such s gives exactly one pair (x, y) with
  x² + y² = n (every x ≤ √n has x² in S; squares above n give a negative
  n − s). So its size r(n) is the number of nonnegative solutions for this z,
  and `a` is the running total over z = 0, …, n.
- **Printing only at shells.** `a<(a:=a+r)!=print(a)` is a chained
  comparison: the old `a` is read, the walrus stores the new total, and only
  if it grew (r(n) > 0, so n is a shell) is the second comparison evaluated,
  which calls `print`. The list around it is non-empty, so the loop never
  stops (the [A000007](../A000007/) loop).
- `S|={n*n}` adds the next square after `n+=1`. At n = 0 the set {0} gives
  r(0) = 1 and the first line, a(0) = 1.

**Notes**

- Other versions that print the same terms:
  - `a==(a:=…)or print(a)` in place of the chained comparison: 2 bytes more;
  - `sum(n-s in S for s in S)` in place of the set size: 76 bytes;
  - the first version of this page, the lattice-point count
    Σ_{x≤√n} (1 + ⌊√(n − x²)⌋) with `math.isqrt`, printed when it changes:
    100 bytes;
  - column heights of the quarter disc kept in a list,
    `h=[y+(x*x+y*y<=n)for x,y in enumerate(h+[0])]` and `a=sum(h)`: 91 bytes.
- Exact integer arithmetic, so the program is right for every n.
- Each z costs a set of n + 1 squares: about 5200 terms in 60 s here. The
  b-file has 2750 terms (up to a(2749), the shell z = 10000), which take
  about 15 s; the bar is the whole b-file in 60 s.
- a(n) grows roughly like n·√(log n), so the 4300-digit int-to-str limit is
  far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |
| 2026-11-06 | Python 3 | 100 | count the quarter disk and print when its total changes |
| 2026-11-07 | Python 3 | 75 | set of squares intersected with its reflection, chained-comparison print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000592), CC BY-SA 4.0.
