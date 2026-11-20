# A002104

> Logarithmic numbers.
> — [OEIS A002104](https://oeis.org/A002104)

Offset 0: 0, 1, 3, 8, 24, 89, 415, 2372, 16072, 125673, 1112083, 10976184, …

### Python 3 — 43 bytes

```python
a=n=0;b=1
while[print(a)]:a+=b;n+=1;b=b*n+1
```

**How it works**

- **Sum.** From the e.g.f. −log(1−x)·eˣ,
  a(n) = Σ_(k=1..n) C(n, k)·(k−1)!.
- **Difference.** Pascal's rule C(n+1, k) = C(n, k) + C(n, k−1) splits
  a(n+1) into a(n) + Σ_(j=0..n) C(n, j)·j! = a(n) + Σ_j n!/(n−j)!, and
  that last sum is b(n) = [A000522](../A000522/)(n), which satisfies
  b(n) = n·b(n−1) + 1 with b(0) = 1. This is the entry's
  a(n+1) − a(n) = A000522(n).
- **Loop.** `a` starts at a(0) = 0 and `b` at b(0) = 1; each pass adds b(n)
  to a and steps b to b(n+1) = (n+1)·b(n) + 1 (`n+=1;b=b*n+1`).

**Notes**

- a(n) is also the number of arrangements (nonempty lists) of elements of
  {1, …, n} whose first element is the smallest one (comment in the
  entry): choosing k elements and putting the smallest first leaves
  (k−1)! orders.
- a(n) has about n·log₁₀ n digits; the b-file has 101 terms (n = 0 to
  100), and the bar is the whole b-file in 60 s, which takes a fraction of
  a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002104), CC BY-SA 4.0.
