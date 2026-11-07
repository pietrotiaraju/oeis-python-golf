# A000590

> a(n) = 13*binomial(2n,n-6)/(n+7).
> — [OEIS A000590](https://oeis.org/A000590)

Offset 6: 1, 13, 104, 663, 3705, 19019, 92092, 427570, 1924065, 8454225, …

a(n) is the coefficient of x^(n−6) in C(x)¹³, the 13th power of the Catalan
generating function, and also the ballot number C(2n, n−6) − C(2n, n−7).

### Python 3 — 54 bytes

```python
a=1;j=6
while[print(a)]:j+=1;a=a*j*(4*j-2)//(j*-~j-42)
```

**How it works**

- **The recurrence.** Dividing the formula at n by the formula at n − 1,
  the factorials of (2n)!/((n−6)!·(n+6)!) leave 2n(2n−1)/((n−6)(n+6)) and
  the factor 1/(n+7) leaves (n+6)/(n+7), so

  a(n) = a(n−1)·2n(2n−1)/((n−6)(n+7)) for n ≥ 7, with a(6) = 1.
- **Exactness.** The equation a(n)·(n−6)(n+7) = a(n−1)·2n(2n−1) holds in
  integers, so the product `a*j*(4*j-2)` is a multiple of the positive
  (j−6)(j+7) and `//` is exact.
- **Golf.** `j*(4*j-2)` is 2j(2j−1), and `j*-~j-42` is j(j+1) − 42 =
  (j−6)(j+7), 3 bytes under `(j-6)*(j+7)`. The same program with 30 is
  [A000589](../A000589/). The loop prints a before each update (the
  [A000007](../A000007/) loop), starting at a(6) = 1.

**Notes**

- Other versions that print the same terms: the binomial with m = 2n + 1, as
  in [A000588](../A000588/), `import math` / `m=13` /
  `while[print(13*math.comb(m,m//2+7)//m)]:m+=2`: 61 bytes; the first version
  of this page, `from math import*` with `13*comb(2*n,n-6)//(n+7)`: 64 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 195 terms (up to a(200)) and all of them print at once; the
  bar is the whole b-file in 60 s.
- a(7151) is the first term with more than 4300 digits, so the int-to-str
  limit stops the program after a(7150), about 2 s in here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |
| 2026-11-07 | Python 3 | 54 | hypergeometric recurrence, (j−6)(j+7) as `j*-~j-42` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000590), CC BY-SA 4.0.
