# A000023

> a(n) is the number of permutations on {1,2,...,n} with an even number of
> fixed points minus the number of permutations with an odd number of fixed
> points.
> — [OEIS A000023](https://oeis.org/A000023)

Offset 0: 1, −1, 2, −2, 8, 8, 112, 656, 5504, 49024, 491264, …

### Python 3 — 40 bytes

```python
a=n=1
while[print(a)]:a=a*n+(-2)**n;n+=1
```

**How it works**

- Each fixed point counts −1, so a(n) is the sum over permutations of
  (−1)^(number of fixed points). Choosing the k points that are not fixed and
  a derangement of them gives the e.g.f. e^(−2x)/(1 − x) (e^(−x) for the
  derangements, times e^(−x) for the signed fixed points).
- Multiplying by 1/(1 − x) turns the e.g.f. into the recurrence
  **a(n) = n·a(n−1) + (−2)ⁿ**, a(0) = 1, which is what the loop runs.
- `while[print(...)]:` prints in the loop condition: `[None]` is a non-empty
  list, so it is true, and it saves a byte over `while 1:print(...);`.

**Notes**

- Each term is one multiplication, so the whole b-file (251 terms) prints at
  once; the bar is the whole b-file in 60 s.
- The second-order recurrence a(n+1) = (n−1)·a(n) + 2n·a(n−1), from
  (1 − x)·f′ = (2x − 1)·f, needs two variables and is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000023), CC BY-SA 4.0.
