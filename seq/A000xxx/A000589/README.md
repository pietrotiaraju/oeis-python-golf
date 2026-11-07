# A000589

> a(n) = 11*binomial(2n,n-5)/(n+6).
> — [OEIS A000589](https://oeis.org/A000589)

Offset 5: 1, 11, 77, 440, 2244, 10659, 48279, 211508, 904475, 3798795, …

a(n) is the coefficient of x^(n−5) in C(x)¹¹, the 11th power of the Catalan
generating function, and also the ballot number C(2n, n−5) − C(2n, n−6).

### Python 3 — 54 bytes

```python
a=1;j=5
while[print(a)]:j+=1;a=a*j*(4*j-2)//(j*-~j-30)
```

**How it works**

- **The recurrence.** Dividing the formula at n by the formula at n − 1,
  the factorials of (2n)!/((n−5)!·(n+5)!) leave 2n(2n−1)/((n−5)(n+5)) and
  the factor 1/(n+6) leaves (n+5)/(n+6), so

  a(n) = a(n−1)·2n(2n−1)/((n−5)(n+6)) for n ≥ 6, with a(5) = 1.
- **Exactness.** The equation a(n)·(n−5)(n+6) = a(n−1)·2n(2n−1) holds in
  integers, so the product `a*j*(4*j-2)` is a multiple of the positive
  (j−5)(j+6) and `//` is exact.
- **Golf.** `j*(4*j-2)` is 2j(2j−1), and `j*-~j-30` is j(j+1) − 30 =
  (j−5)(j+6), 3 bytes under `(j-5)*(j+6)` and 2 under `//(j-5)//(j+6)`.
  The loop prints a before each update (the [A000007](../A000007/) loop),
  starting at a(5) = 1.

**Notes**

- Other versions that print the same terms: the binomial with m = 2n + 1, as
  in [A000588](../A000588/), `import math` / `m=11` /
  `while[print(11*math.comb(m,m//2+6)//m)]:m+=2`: 61 bytes; the first version
  of this page, `from math import*` with `11*comb(2*n,n-5)//(n+6)`: 64 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 196 terms (up to a(200)) and all of them print at once; the
  bar is the whole b-file in 60 s.
- a(7151) is the first term with more than 4300 digits, so the int-to-str
  limit stops the program after a(7150), about 2 s in here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |
| 2026-11-07 | Python 3 | 54 | hypergeometric recurrence, (j−5)(j+6) as `j*-~j-30` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000589), CC BY-SA 4.0.
