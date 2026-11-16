# A001880

> Coefficients of Bessel polynomials y_n (x).
> — [OEIS A001880](https://oeis.org/A001880)

Offset 4: 1, 15, 210, 3150, 51975, 945945, 18918900, 413513100, 9820936125, 252070693875, 6957151150950, 205552193096250, …

### Python 3 — 43 bytes

```python
b=k=1
while[print(k*-~k*b//2)]:k+=1;b*=k-~k
```

**How it works**

- **The Bessel coefficient.** y_n(x) = Σₖ (n + k)!/((n − k)!·k!·2ᵏ)·xᵏ; this
  sequence is the coefficient of x^(n−4), a(n) = (2n − 4)!/(4!·(n − 4)!·2^(n−4)).
- **Splitting off a double factorial.** (2n − 4)! = 2^(n−2)·(n − 2)!·(2n − 5)!!,
  so a(n) = 4(n − 2)(n − 3)·(2n − 5)!!/4! = C(n − 2, 2)·(2n − 5)!!/3.
  With k = n − 3 that is k(k + 1)/2 · (2k + 1)!!/3.
- **The program.** `b` is (2k + 1)!!/3 (an integer from k = 1 on, starting at
  3!!/3 = 1), so `b=k=1` is n = 4; each step raises k and multiplies b by
  `k-~k` = 2k + 1; it prints k(k + 1)/2·b, with `-~k` = k + 1.

**Notes**

- Checked against the Bessel polynomial coefficients for n < 150, and against
  the b-file.
- The single recurrence (n − 4)·a(n) = (n − 2)(2n − 5)·a(n − 1) costs 11
  bytes more.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1425.
- The b-file has 97 terms (n = 4 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001880), CC BY-SA 4.0.
