# A000033

> a(n) = A058087(n,n-2).
> — [OEIS A000033](https://oeis.org/A000033)

Offset 1: 0, 2, 3, 4, 40, 210, 1477, 11672, 104256, 1036050, 11338855, 135494844, …

### Python 3 — 83 bytes

```python
m=b=c=d=1;a=0
while[print(m*a)]:m+=1;a,b,c,d=b,c,d,m*(b+c+d)+(m*c+d-b)//2+a+(-1)**m
```

**How it works**

- A058087 is the triangle of ménage hit polynomials
  U_n(t) = Σ_k 2n/(2n−k)·C(2n−k, k)·(n−k)!·(t−1)^k, read from the highest
  power down, so T(n, n−2) is the coefficient of t². Taking that coefficient
  term by term gives the sum on the OEIS page, a(n) = n·b(n) with
  b(n) = Σ_{k=2..n} (−1)^k (2n−k−1)! (n−k)! / ((2n−2k)! (k−2)!), which is
  [A000426](https://oeis.org/A000426). For n = 1 the sum is empty and a(1) = 0.
- The program does not use the sum but a recurrence for b, valid for n ≥ 5:

  2b(n) = (2n−5)b(n−1) + (3n−9)b(n−2) + (2n−7)b(n−3) + 2b(n−4) − 2(−1)ⁿ.

  With m = n − 3 the coefficients are 2m+1, 3m and 2m−1, so the right side
  over 2 is m(b(n−1)+b(n−2)+b(n−3)) + (m·b(n−2) + b(n−1) − b(n−3))/2 + b(n−4)
  + (−1)^m. That is the last element of the tuple, with `a,b,c,d` holding
  b(n−4), …, b(n−1). The halved part is b(n) minus whole numbers, so it is
  always even and `//2` is exact.
- When `print` runs, `a,b,c,d` are b(m), …, b(m+3), so the loop prints
  m·b(m) = a(m). It starts at m = 1 with b(1..4) = 0, 1, 1, 1, hence
  `m=b=c=d=1;a=0`; `m+=1` then makes m equal to n − 3 for the new term n = m + 3.
- `while[print(…)]:` is the usual loop: `print` returns `None` and `[None]` is
  true.

**Why the recurrence holds**

- It was found by fitting the b-file and then proved with Zeilberger's method:
  [`recurrence_check.py`](recurrence_check.py) gives the certificate G(n, k)
  (a rational function of n and k times the k-th term of b(n)), checks with
  sympy that the recurrence's summand telescopes to G(n, k+1) − G(n, k), and
  adds the terms at the ends of the rows by hand; they leave exactly −2(−1)ⁿ.
  It also checks the recurrence against the sum directly for n = 5..400.
- A000426 lists the homogeneous form of order 5, the sum of this recurrence at
  n and n+1, but with the index off by one: as printed,
  "a(n) = ((2n−5)a(n−1) + (5n−11)a(n−2) + …)/2 for n ≥ 6" gives 49 for
  b(6) = 35. Written for b(n+1) it is right. As a program it needs a fifth
  value and is 95 bytes, the (−1)ⁿ costing less than the extra state.

**Notes**

- The sum itself, with j = k − 1, is 103 bytes (`perm(x)` is x!):

  ```python
  from math import*
  n=1
  while[print(n*sum((-1)**j*-j*comb(2*n-j-2,j)*perm(n-j-1)for j in range(n)))]:n+=1
  ```

- The whole hit polynomial satisfies
  (n−2)U_n = n(n−2)U_{n−1} + n(t−1)²U_{n−2} − 4(t−1)ⁿ (at t = 0, the classical
  ménage recurrence; checked coefficient by coefficient for n < 120).
  Reading t² off U_n(B) for a big base B would need B > n!, so B has to grow
  and every term starts over: about 120 bytes. Kotesovec's order-3 recurrence
  for a(n) itself has quartic coefficients and is longer still.
- Exact integer arithmetic, so the program is right for every n. a(n) ~
  2n!/e², and a(1559) is the first term over the 4300-digit int-to-str limit
  of Python 3.11+, where the program stops with a `ValueError`. The b-file
  (100 terms) prints at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000033), CC BY-SA 4.0.
