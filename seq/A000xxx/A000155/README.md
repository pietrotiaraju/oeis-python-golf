# A000155

> Nearest integer to modified Bessel function K_n(1).
> — [OEIS A000155](https://oeis.org/A000155)

Offset 0: 0, 1, 2, 7, 44, 361, 3654, 44207, 622552, 10005041, 180713290, …

### Python 3 — 50 bytes

```python
a=0;b=m=1
while[print(a)]:a,b=b,a+m*b+(b^m&2);m+=2
```

**How it works**

- For integer n ≥ 1, [DLMF 10.31.1](https://dlmf.nist.gov/10.31.E1) at
  z = 1 writes K_n(1) as a finite sum
  Σ_{k=0}^{n−1} T(n,k), with T(n,k) = (−1)ᵏ·2^(n−1−2k)·(n−1−k)!/k!, plus
  ln 2·(−1)ⁿ·Iₙ(1) and a series with digamma coefficients. The terms with
  2k ≤ n−1 are integers; call their sum S(n) (S(0) = 0). This is Mark van
  Hoeij's formula on the OEIS page, and also the "conjectured" Chebyshev
  integral ∫₀^∞ U_{n−1}(x)e^(−x) dx term by term.
- a(n) = S(n) for every n: for n ≥ 3 the rest is under ½. The first
  fractional term has size 1/n (n even) or 1/(n²−1) (n odd), and the ratio of
  consecutive ones is 1/(4(k+1)(n−1−k)) ≤ 1/8, so the fractional tail is at
  most 8/(7n). The logarithm term is at most ln 2·e^(1/4)·2^(−n)/n!, and the
  digamma series at most e^(1/4)(n + 5/2)·2^(−n−1)/n!. Together that is below
  ½ for n ≥ 3 (0.48 at n = 3, and it decreases). For n = 0, 1, 2,
  K_n(1) = 0.421…, 0.601…, 1.624… and S(n) = 0, 1, 2.
- The terms satisfy T(n+1,k) = 2n·T(n,k) + T(n−1,k−1). Summing over the
  integer ranges leaves one boundary term when n is even, so for n ≥ 1

  a(n+1) = 2n·a(n) + a(n−1) + d(n), with d(n) = 2·(−1)^(n/2) for even n
  and d(n) = 0 for odd n.

- By induction this gives a(n) ≡ n (mod 4). So for even n, a(n) ≡ 0 (mod 4)
  exactly when d(n) = +2, and a(n) ≡ 2 exactly when d(n) = −2: in both cases
  a(n) ^ 2 = a(n) + d(n).
- In the loop `a`, `b` are a(n−1), a(n) and `m` is 2n−1, so `m&2` is 2 exactly
  when n is even. Then `b^m&2` is a(n) + d(n), and `a+m*b+(b^m&2)` is
  a(n−1) + 2n·a(n) + d(n) = a(n+1).

**Notes**

- The program prints the 201 terms of the b-file at once. a(n) ~ (n−1)!·2^(n−1)
  passes Python's 4300-digit int-to-str limit at n = 1425, where the program
  stops with a `ValueError`; it is correct beyond that once the limit is
  lifted.
- Van Hoeij's homogeneous recurrence
  a(n) = 2(n−1)a(n−1) + 2(n−3)a(n−3) + a(n−4) needs four starting values and
  costs 72 bytes; writing the correction of the 3-term recurrence as
  `2*a-(a^a%2*2)` (through a(n−1) ≡ n−1 mod 4) instead of the XOR on `b`
  costs 54.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000155), CC BY-SA 4.0.
