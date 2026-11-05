# A000188

> (1) Number of solutions to x^2 == 0 (mod n). (2) Also square root of largest square dividing n. (3) Also max_{ d divides n } gcd(d, n/d).
> — [OEIS A000188](https://oeis.org/A000188)

Offset 1: 1, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 2, 1, 1, 1, 4, 1, 3, 1, 2, 1, 1, 1, 2, 5, …

### Python 3 — 52 bytes

```python
n=1
while[print(sum(x*x%n<1for x in range(n)))]:n+=1
```

**How it works**

- Definition (1), taken literally: count the residues x = 0, …, n−1 with
  n | x². No square roots, no factoring.
- Why it matches (2): write n = s²·t with t squarefree. Then n | x² exactly
  when s·t | x (for each prime p with p^e ∥ n, p^⌈e/2⌉ must divide x), so
  the solutions are the n/(s·t) = s multiples of s·t below n, and s is the
  square root of the largest square dividing n.
- `while[print(…)]:` is a byte under `while 1:…;` (a one-element list is
  always true), and `<1for` saves the space before `for`.

**Notes**

- Exact integer arithmetic, correct for every n. Each term costs n steps,
  so the whole b-file (10000 terms) takes about 14 s here. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000188), CC BY-SA 4.0.
