# A000426

> Coefficients of ménage hit polynomials.
> — [OEIS A000426](https://oeis.org/A000426)

Offset 1: 0, 1, 1, 1, 8, 35, 211, 1459, 11584, 103605, …

a(n) = A000033(n)/n, where A000033(n) is the coefficient of t² in the
ménage hit polynomial U_n(t). It is also the coefficient of t in the hit
polynomial of the straight table: the number of permutations π of
{1, …, n−1} with exactly one i such that π(i) = i or π(i) = i + 1.

### Python 3 — 63 bytes

```python
a=b=n=1;c=0
while[print(c+(2-n)*b-a)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- With j = k − 1, the OEIS sum a(n) = Σ_{k=2}^{n} (−1)^k (2n−k−1)!(n−k)! /
  ((2n−2k)!(k−2)!) becomes a(n) = Σ_j (−1)^(j+1)·j·C(2m−j, j)·(m−j)! with
  m = n − 1. That is V′_m(0) for V_m(t) = Σ_j C(2m−j, j)·(m−j)!·(t−1)^j, the
  hit polynomial of the 2m − 1 cells (i, i), (i, i+1) of an m×m board (its
  rook numbers are C(2m−j, j)), which gives the counting description above.
  V_m(0) = W_m is the straight-table ménage number [A000271](../A000271/)(m).
- The program uses a(n) = W_{n−1} + n·W_{n−2} + W_{n−3}. Proof: summing over
  j first, Σ_m V_m(t)·x^m = Σ_k k!·x^k·(1 − (t−1)x)^(−2k−1). With
  u = x/(1+x)² and f(u) = Σ_k k!·u^k this gives W(x) = Σ W_m x^m = f(u)/(1+x)
  and, differentiating in t at t = 0, Σ_m a(m+1)·x^m = u·(2u·f′(u) + f(u)).
  The series f satisfies u²f′ = (1−u)f − 1 (compare coefficients), so that is
  (2−u)f − 2. On the other side W + (x²W)′ + x²W = (1+x)²W + x²W′, and with
  u′ = (1−x)/(1+x)³ and the same equation for f it is (2−u)f − 1 + x. So
  a(m+1) = W_m + (m+1)·W_{m−1} + W_{m−2} for m ≥ 2, and also for m = 0, 1
  with Somos's values W_{−1} = −1, W_{−2} = 0 (checked: 0 and 1).
- The A000271 program keeps (a, b, c) = (−W_{n−2}, W_{n−1}, W_n) at counter n
  with the update W_{n+1} = n(W_n + W_{n−1}) + W_{n−2} = `n*(b+c)-a`, from
  the seeds `a=b=n=1;c=0`. Eliminating W_{n−3} with
  W_n = (n−1)(W_{n−1} + W_{n−2}) + W_{n−3} turns the identity into
  a(n) = W_n − (n−2)·W_{n−1} + W_{n−2} = `c+(2-n)*b-a`, and that recurrence
  also holds at n = 1, 2 with the values above, so the print is right from
  a(1) on.

**Notes**

- Counting from k = n − 1 instead, `a=k=0;b=-1;c=1` with
  `while[print(c-a-~k*b)]:a,b,c=-b,c,k*(b+c)-a;k+=1` (`-~k*b` is (k+1)·W_{k−1}):
  also 63 bytes. The proved order-4 recurrence
  2a(n) = (2n−5)a(n−1) + (3n−9)a(n−2) + (2n−7)a(n−3) + 2a(n−4) − 2(−1)ⁿ
  (see [A000033](../A000033/)) as a program: 81; with the signs (−1)ⁿa(n)
  stored, which turns the (−1)ⁿ term into a constant: 82.
- Exact integer arithmetic, so the program is right for every n; the identity
  was also checked against the OEIS sum for n < 300.
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s.
- a(1560) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there (1559 terms in half a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |
| 2026-11-07 | Python 3 | 63 | a(n) = W_{n−1} + n·W_{n−2} + W_{n−3}: the A000271 program with another print |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000426), CC BY-SA 4.0.
