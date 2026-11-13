# A001658

> Fibonomial coefficients.
> — [OEIS A001658](https://oeis.org/A001658)

Offset 0: 1, 13, 273, 4641, 85085, 1514513, 27261234, 488605194, 8771626578, …

### Python 3 — 53 bytes

```python
a=2;b=3
while[print((a**5-a)*(a+b+b)//240)]:a,b=b,a+b
```

**How it works**

- a(n) = C(n+6, 6)_F = F(n+1)···F(n+6)/(1·1·2·3·5·8): the Fibonomial
  coefficient, F(n+1)···F(n+6)/240 in the formula section.
- As in [A001657](../A001657/), Catalan's identity makes the five factors
  F(n+1)···F(n+5) equal F(m)⁵ − F(m) with m = n + 3. The sixth is
  F(n+6) = F(n+4) + F(n+5) = F(m) + 2F(m+1).
- `a`, `b` hold F(n+3), F(n+4) (starting at 2, 3), so each pass prints
  `(a**5-a)*(a+b+b)//240`, exact since a(n) is an integer.

**Notes**

- Folding the step into the print, `(a**5-a)*(b+(b:=a+b))//240` then
  `a=b-a`, is 54 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001658), CC BY-SA 4.0.
