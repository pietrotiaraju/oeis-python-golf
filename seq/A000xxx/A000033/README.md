# A000033

> a(n) = A058087(n,n-2).
> — [OEIS A000033](https://oeis.org/A000033)

Offset 1: 0, 2, 3, 4, 40, 210, 1477, 11672, 104256, 1036050, 11338855, 135494844, …

### Python 3 — 67 bytes

```python
a=b=n=1;c=0
while[print(n*(c+(2-n)*b-a))]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- A058087 is the triangle of ménage hit polynomials
  U_n(t) = Σ_k 2n/(2n−k)·C(2n−k, k)·(n−k)!·(t−1)^k, read from the highest
  power down, so T(n, n−2) is the coefficient of t². Taking that coefficient
  term by term gives the sum on the OEIS page, a(n) = n·b(n) with
  b(n) = Σ_{k=2..n} (−1)^k (2n−k−1)! (n−k)! / ((2n−2k)! (k−2)!), which is
  [A000426](../A000426/). For n = 1 the sum is empty and a(1) = 0.
- b(n) = W_n − (n−2)·W_{n−1} + W_{n−2}, where W_m is the straight-table
  ménage number [A000271](../A000271/)(m), with Somos's values
  W_{−1} = −1 and W_0 = 1 at the start. This is proved on the A000426 page
  through the generating function of the straight-table hit polynomials:
  b(n) is the coefficient of t in the hit polynomial of the 2n − 3 cells
  (i, i), (i, i+1) of an (n−1)×(n−1) board.
- The program is A000426's with the print multiplied by n. At counter n the
  tuple is (a, b, c) = (−W_{n−2}, W_{n−1}, W_n), so `c+(2-n)*b-a` is b(n),
  and the update `a,b,c=-b,c,n*(b+c)-a` is the order-3 recurrence
  W_{n+1} = n(W_n + W_{n−1}) + W_{n−2}. The seeds `a=b=n=1;c=0` are
  (W_{−1}, W_0, W_1) = (−1, 1, 0) with a stored negated, and the identity
  holds from n = 1 on, so the first line printed is a(1) = 1·(0 + 1 − 1) = 0.
- `while[print(…)]:` is the usual loop: `print` returns `None` and `[None]` is
  true.

**Notes**

- A000426's other 63-byte form, counting from k = n − 1, needs the factor
  k + 1 as `-~k*(c-a-~k*b)`: 69 bytes here.
- The previous record (83 bytes) used a recurrence for b of order 4 with a
  (−1)ⁿ term, found by fitting the b-file and proved with Zeilberger's method
  in [`recurrence_check.py`](recurrence_check.py):

  ```python
  m=b=c=d=1;a=0
  while[print(m*a)]:m+=1;a,b,c,d=b,c,d,m*(b+c+d)+(m*c+d-b)//2+a+(-1)**m
  ```

  2b(n) = (2n−5)b(n−1) + (3n−9)b(n−2) + (2n−7)b(n−3) + 2b(n−4) − 2(−1)ⁿ for
  n ≥ 5; with m = n − 3 the right side over 2 is the last element of the
  tuple, and the halved part is always even. A000426 lists the homogeneous
  form of order 5 (the sum of this recurrence at n and n+1) with the index
  off by one: as printed it gives 49 for b(6) = 35.
- The OEIS sum itself, with j = k − 1, is 103 bytes (`perm(x)` is x!):

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
- Exact integer arithmetic, so the program is right for every n; it was also
  checked against the OEIS sum for n < 300. a(n) ~ 2n!/e², and a(1559) is
  the first term over the 4300-digit int-to-str limit of Python 3.11+, where
  the program stops with a `ValueError` after 1558 terms (in about 0.2 s
  here).
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s, which prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 83 | first entry |
| 2026-11-07 | Python 3 | 67 | A000426's W-identity program, print multiplied by n |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000033), CC BY-SA 4.0.
