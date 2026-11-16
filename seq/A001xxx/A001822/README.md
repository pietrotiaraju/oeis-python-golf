# A001822

> Expansion of Sum_{n>=0} x^(3n+2)/(1-x^(3n+2)).
> — [OEIS A001822](https://oeis.org/A001822)

Offset 1: 0, 1, 0, 1, 1, 1, 0, 2, 0, 2, 1, 1, 0, 2, 1, 2, 1, 1, 0, 3, 0, 2, 1, 2, 1, 2, …

### Python 3 — 58 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(n%d<1for d in r[1::3]))
```

**How it works**

- a(n) counts the divisors d of n with d ≡ 2 (mod 3). The g.f. says this: x^(3k+2)/(1 −
  x^(3k+2)) = Σ_(j≥1) x^(j(3k+2)), so the coefficient of xⁿ counts the divisors 3k + 2 of n.
- `r` starts as `[1]`, and each pass appends n + 1 before it counts, so while n is read `r`
  holds 1, 2, …, n + 1 (the loop over a growing list is the endless counter). `r[1::3]` is then
  2, 5, 8, … up to n + 1, and `n%d<1` tests d | n; n + 1 never divides n, so the extra entry
  costs nothing.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s, which takes a few seconds
  here. The same template, with another slice, gives [A001817](../A001817/),
  [A001826](../A001826/), [A001842](../A001842/), [A001876](../A001876/),
  [A001877](../A001877/), [A001878](../A001878/), [A001899](../A001899/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001822), CC BY-SA 4.0.
