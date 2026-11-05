# A000089

> Number of solutions to x^2 + 1 == 0 (mod n).
> — [OEIS A000089](https://oeis.org/A000089)

Offset 1: 1, 1, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 2, …

### Python 3 — 54 bytes

```python
n=1
while[print(sum(x*x%n>n-2for x in range(n)))]:n+=1
```

**How it works**

- Straight from the name: count the residues x = 0 … n − 1 with
  x² + 1 ≡ 0 (mod n).
- `x*x%n` lies in 0 … n − 1, so `x*x%n>n-2` holds exactly when
  x² mod n = n − 1, that is when n divides x² + 1. It is 2 bytes shorter
  than `(x*x+1)%n<1`. For n = 1 it reads 0 > −1, true for the single
  residue x = 0, so a(1) = 1 as it should.
- `sum` counts the `True`s. `while[print(…)]:n+=1` prints and loops
  forever, because `[None]` is a non-empty list; it is a byte shorter than
  `n=0` + `while 1:n+=1;print(…)`.

**Notes**

- Exact integer arithmetic over every residue, so the program is right for
  every n; it relies on no formula.
- Each term costs n steps, so the whole b-file (10000 terms) prints in
  about 5 s, and about 35000 terms print in 60 s. The bar is the whole
  b-file in 60 s.
- The multiplicative formula (a(n) = 0 if 4 | n, else the product of
  1 + (−1/p) over the odd primes p dividing n) needs a factorisation and is
  much longer.
- With sympy, `len(sqrt_mod(-1,n,1))` in the same loop is 63 bytes, longer
  than the plain program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000089), CC BY-SA 4.0.
