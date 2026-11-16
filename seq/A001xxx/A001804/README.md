# A001804

> a(n) = n! * C(n,2).
> — [OEIS A001804](https://oeis.org/A001804)

Offset 2: 2, 18, 144, 1200, 10800, 105840, 1128960, 13063680, 163296000, 2195424000, …

### Python 3 — 39 bytes

```python
f=1;n=2
while[print(f*n*~-n)]:n+=1;f*=n
```

**How it works**

- a(n) = n!·C(n, 2) = n!/2 · n(n − 1). `f` holds n!/2: it starts at
  2!/2 = 1 for n = 2, and each pass moves `n` on and multiplies `f` by the
  new n. Then `f*n*~-n` is n!/2 · n(n − 1) = a(n) (`~-n` is n − 1).
- Halving the factorial in the start value instead of halving the product
  saves the `>>1`: `f=n=2` with `f*n*~-n>>1` is one byte longer.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Same length: `f=m=1` / `while[print(f*m*-~m)]:m+=1;f*=-~m`
  (m = n − 1). The ratio recurrence a(n) = a(n − 1)·n²/(n − 2) from
  `a=n=2` is 41 bytes.
- E.g.f. x²/(1 − x)³; a(n) = 2·[A001809](../A001809/)(n). Family n!·C(n, k):
  A001804 (k = 2), [A001805](../A001805/) (k = 3), [A001806](../A001806/)
  (k = 4), [A001807](../A001807/) (k = 5).
- a(1557) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 99 terms (n = 2 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001804), CC BY-SA 4.0.
