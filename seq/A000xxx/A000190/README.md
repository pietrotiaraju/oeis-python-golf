# A000190

> Number of solutions to x^4 == 0 (mod n).
> — [OEIS A000190](https://oeis.org/A000190)

Offset 1: 1, 1, 1, 2, 1, 1, 1, 4, 3, 1, 1, 2, 1, 1, 1, 8, 1, 3, 1, 2, 1, 1, 1, 4, 5, …

### Python 3 — 53 bytes

```python
n=1
while[print(sum(x**4%n<1for x in range(n)))]:n+=1
```

**How it works**

- The definition, taken literally: count the residues x = 0, …, n−1 with
  n | x⁴. No factoring.
- Why it matches the formula a(p^e) = p^⌊3e/4⌋: for each prime p with
  p^e ∥ n, n | x⁴ exactly when p^⌈e/4⌉ | x, so the solutions are the
  multiples of m = ∏ p^⌈e/4⌉ below n, and there are n/m of them, which is
  ∏ p^(e−⌈e/4⌉) = ∏ p^⌊3e/4⌋.
- Same template as [A000188](../A000188/) (x² ≡ 0), one byte longer for
  `x**4` instead of `x*x`. `while[print(…)]:` is a byte under `while 1:…;`,
  and `<1for` saves the space before `for`.

**Notes**

- Exact integer arithmetic, correct for every n. Each term costs n steps,
  so the whole b-file (10000 terms) takes about 28 s here. The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000190), CC BY-SA 4.0.
