# A001814

> Coefficient of H_2 when expressing x^{2n} in terms of Hermite polynomials H_m.
> — [OEIS A001814](https://oeis.org/A001814)

Offset 1: 1, 12, 180, 3360, 75600, 1995840, 60540480, 2075673600, 79394515200, 3352212864000, 154872234316800, 7771770303897600, …

### Python 3 — 37 bytes

```python
b=n=1
while[print(n*b)]:n+=1;b*=4*n-2
```

**How it works**

- **The expansion.** As in Abramowitz and Stegun's table 22.12, the powers are
  scaled by 2^m: (2x)^m = m!·Σₖ H_(m−2k)(x)/(k!·(m − 2k)!), with H the
  physicists' Hermite polynomials. For m = 2n the H₂ term is k = n − 1, so
  a(n) = (2n)!/(2·(n − 1)!), the OEIS formula. (Unscaled, x^(2n) has H₂
  coefficient a(n)/4ⁿ; the listed integers are those of (2x)^(2n).)
- **Splitting off a double factorial.** (2n)! = 2ⁿ·n!·(2n − 1)!!, so
  a(n) = n·b with b = 2^(n−1)·(2n − 1)!!, and b grows by 2(2n − 1) = 4n − 2.
- **The program.** `b=n=1` is b at n = 1; each step raises n and multiplies b
  by `4*n-2`; it prints n·b.

**Notes**

- Checked against the exact expansion of (2x)^(2n) in Hermite polynomials
  (solving the triangular system) for n < 50, and against the b-file.
- `n*b` with the double-factorial update is 8 bytes shorter than the single
  ratio a(n) = a(n − 1)·n(4n − 2)/(n − 1).
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1309.
- The b-file has 200 terms (n = 1 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001814), CC BY-SA 4.0.
