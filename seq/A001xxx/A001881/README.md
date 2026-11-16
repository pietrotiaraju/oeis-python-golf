# A001881

> Coefficients of Bessel polynomials y_n (x).
> — [OEIS A001881](https://oeis.org/A001881)

Offset 5: 1, 21, 378, 6930, 135135, 2837835, 64324260, 1571349780, 41247931725, 1159525191825, 34785755754750, 1109981842719750, …

### Python 3 — 44 bytes

```python
b=k=1
while[print(k*-~k*b//2)]:k+=1;b*=2*k+3
```

**How it works**

- **The Bessel coefficient.** y_n(x) = Σₖ (n + k)!/((n − k)!·k!·2ᵏ)·xᵏ; this
  sequence is the coefficient of x^(n−5), a(n) = (2n − 5)!/(5!·(n − 5)!·2^(n−5)).
- **Splitting off a double factorial.** (2n − 6)! = 2^(n−3)·(n − 3)!·(2n − 7)!!,
  so a(n) = (2n − 5)·4(n − 3)(n − 4)·(2n − 7)!!/5!
  = C(n − 3, 2)·(2n − 5)!!/15, the OEIS formula. With k = n − 4 that is
  k(k + 1)/2 · (2k + 3)!!/15.
- **The program.** `b` is (2k + 3)!!/15 (an integer from k = 1 on, starting at
  5!!/15 = 1), so `b=k=1` is n = 5; each step raises k and multiplies b by
  2k + 3; it prints k(k + 1)/2·b, with `-~k` = k + 1.

**Notes**

- Checked against the Bessel polynomial coefficients for n < 150, and against
  the b-file.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1425.
- The b-file has 396 terms (n = 5 to 400); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001881), CC BY-SA 4.0.
