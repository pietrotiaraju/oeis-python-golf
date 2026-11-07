# A000457

> Exponential generating function: (1+3*x)/(1-2*x)^(7/2).
> — [OEIS A000457](https://oeis.org/A000457)

Offset 0: 1, 10, 105, 1260, 17325, 270270, 4729725, 91891800, 1964187225, 45831035250, …

a(n) = (n+1)·5·7·…·(2n+3) = (n+1)·(2n+3)!!/3.

### Python 3 — 37 bytes

```python
n=a=1
while[print(n*a)]:n+=1;a*=2*n+1
```

**How it works**

- **The formula.** Let G(x) = (1−2x)^(−5/2). Its n-th e.g.f. coefficient
  is 2ⁿ·(5/2)(7/2)…(5/2 + n − 1) = 5·7·…·(2n+3) = g(n). Then
  G + x·G′ = (1−2x)^(−7/2)·((1−2x) + 5x) = (1+3x)/(1−2x)^(7/2), and x·G′
  has coefficients n·g(n), so a(n) = (n+1)·g(n).
- **The loop.** At a print, the variable n is m + 1 and a = g(m), so
  `n*a` is a(m), starting with n = a = 1 at m = 0. Then n goes up and
  `a*=2*n+1` multiplies in the next odd factor 2(m+1) + 3.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `a*=n-~n` ties; with the odd
  factor as the counter, `m=3;a=1` / `while[print(m//2*a)]:m+=2;a*=m`: 38
  bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 201 terms print in 0.07 s here. The b-file has 201 terms
  (up to a(200)); the bar is the whole b-file in 60 s.
- a(n) grows like a double factorial; the first term with more than 4300
  digits is a(1421), where printing stops.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000457), CC BY-SA 4.0.
