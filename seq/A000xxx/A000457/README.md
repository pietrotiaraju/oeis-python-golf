# A000457

> Exponential generating function: (1+3*x)/(1-2*x)^(7/2).
> — [OEIS A000457](https://oeis.org/A000457)

Offset 0: 1, 10, 105, 1260, 17325, 270270, 4729725, 91891800, 1964187225, 45831035250, …

### Python 3 — 37 bytes

```python
n=a=1
while[print(n*a)]:n+=1;a*=2*n+1
```

**How it works**

- Let G(x)=(1−2x)^(−5/2). Its n-th exponential coefficient is
  g(n)=(2n+3)!!/3, where the double factorial multiplies the odd
  integers through 2n+3.
- G(x)+xG′(x)=(1+3x)/(1−2x)^(7/2), the required e.g.f.
  Multiplication by x and differentiation multiply its n-th
  coefficient by n, so a(n)=(n+1)·g(n).
- The program uses a shifted counter: at a print, the variable
  n=m+1 and the variable a=(2n+1)!!/3=g(m). Thus `n*a`
  is the sequence term a(m), starting at m=0 with n=a=1.
- After incrementing n, `a*=2*n+1` adjoins the next odd factor.
  For example n=2, a=5 prints 10; n=3, a=35 prints 105.

**Notes**

- Exact integers. The division by 3 is absorbed in the initial
  state a=1=3!!/3; all subsequent updates are multiplications.
- The e.g.f. uses a fractional power, but the program needs neither
  fractional arithmetic nor a series expansion at runtime.
- One product and one shifted counter suffice. Python 3.11+
  eventually stops at its default 4300-digit integer-to-string
  limit as the double factorial grows; this is an interpreter limit.
- The b-file has 201 terms (indices 0 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000457), CC BY-SA 4.0.
