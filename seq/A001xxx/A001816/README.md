# A001816

> Coefficients of x^n in Hermite polynomial H_{n+4}.
> — [OEIS A001816](https://oeis.org/A001816)

Offset 0: 12, 120, 720, 3360, 13440, 48384, 161280, 506880, 1520640, 4392960, 12300288, 33546240, …

### Python 3 — 41 bytes

```python
a=12;n=0
while[print(a)]:n+=1;a+=a+8*a//n
```

**How it works**

- **The coefficient.** H_m(x) = Σₖ (−1)ᵏ m!/(k!·(m − 2k)!)·(2x)^(m−2k), so
  the coefficient of xⁿ in H_(n+4) (k = 2) is (n + 4)!·2ⁿ/(2·n!)
  = 12·C(n + 4, 4)·2ⁿ, the g.f. 12/(1 − 2x)⁵.
- **A ratio.** a(n)/a(n − 1) = 2(n + 4)/n = 2 + 8/n. Since a(n) and 2a(n − 1)
  are integers, so is 8a(n − 1)/n, and a(n) = 2a(n − 1) + ⌊8a(n − 1)/n⌋
  exactly.
- **The program.** `a+=a+8*a//n` is that step, after `n+=1`.

**Notes**

- Checked against the Hermite polynomials (H_(m+1) = 2xH_m − 2mH_(m−1)) for
  n < 120, and against the b-file.
- `a+=a+8*a//n` is 3 bytes shorter than `a=a*(2*n+8)//n`.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 14231.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001816), CC BY-SA 4.0.
