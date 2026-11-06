# A000086

> Number of solutions to x^2 - x + 1 == 0 (mod n).
> — [OEIS A000086](https://oeis.org/A000086)

Offset 1: 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, …

### Python 3 — 56 bytes

```python
n=1
while[print(sum(x*~-x%n>n-2for x in range(n)))]:n+=1
```

**How it works**

- Straight from the name: count the residues x = 0 … n − 1 with
  x² − x + 1 ≡ 0 (mod n).
- `~-x` is x − 1, so `x*~-x%n` is x(x − 1) mod n, a number in 0 … n − 1.
  It equals n − 1 exactly when n divides x(x − 1) + 1 = x² − x + 1, and
  `>n-2` tests that with no `==` and no extra parentheses (2 bytes under
  `(x*x-x+1)%n<1`). For n = 1 it reads 0 > −1, true for the single residue
  x = 0, so a(1) = 1 as it should.
- `sum` counts the `True`s. `while[print(…)]:n+=1` prints and loops
  forever, because `[None]` is a non-empty list.
- It is the [A000089](../A000089/) program (x² + 1) with `x*x` turned into
  `x*~-x`, hence 2 bytes longer.

**Notes**

- Exact integer arithmetic over every residue, so the program is right for
  every n; it relies on no formula.
- Each term costs n steps, so the whole b-file (2000 terms) prints in well
  under a second. The bar is the whole b-file in 60 s.
- The multiplicative formula (a(p^e) = 2 for p ≡ 1 (mod 3), a(3) = 1, 0 for
  9, for 2 and for p ≡ 2 (mod 3)) needs a factorisation and is much longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000086), CC BY-SA 4.0.
