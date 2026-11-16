# A001899

> Number of divisors of n of the form 5k+4; a(0) = 0.
> — [OEIS A001899](https://oeis.org/A001899)

Offset 0: 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 2, 0, …

### Python 3 — 58 bytes

```python
r=[0]
for n in r:print(sum(n%d<1for d in r[4::5]));r+=n+1,
```

**How it works**

- a(n) counts the divisors d of n with d ≡ 4 (mod 5).
- `r` starts as `[0]`, and each pass counts first and appends n + 1 afterwards, so while n is
  read `r` holds 0, 1, …, n and `r[i]` = i. `r[4::5]` is then 4, 9, 14, … up to n, and `n%d<1`
  tests d | n. At n = 0 the slice is empty, which gives the a(0) = 0 that the entry sets (every
  d would divide 0).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms; the bar is the whole b-file in 60 s, which takes a few seconds
  here. The same template, with another slice, gives [A001817](../A001817/),
  [A001822](../A001822/), [A001826](../A001826/), [A001842](../A001842/),
  [A001876](../A001876/), [A001877](../A001877/), [A001878](../A001878/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001899), CC BY-SA 4.0.
