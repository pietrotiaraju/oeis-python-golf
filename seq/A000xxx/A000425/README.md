# A000425

> Coefficients of ménage hit polynomials.
> — [OEIS A000425](https://oeis.org/A000425)

Offset 1: 2, 0, 0, 8, 30, 192, 1344, 10800, 97434, 976000, …

a(n) is the coefficient of t in the ménage hit polynomial U_n(t) (a diagonal
of A058087). For n ≥ 3 it is the number of permutations π of
{0, …, n−1} with exactly one i such that π(i) = i or π(i) = i + 1 (mod n).

### Python 3 — 57 bytes

```python
a=b=n=1;c=0
while[print(2*n*b)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- Riordan's hit polynomial is
  U_n(t) = Σ_k 2n/(2n−k)·C(2n−k, k)·(n−k)!·(t−1)^k. The coefficient of t in
  (t−1)^k is (−1)^(k−1)·k, and 2n/(2n−k)·C(2n−k, k)·k = 2n·C(2n−k−1, k−1).
  With j = k − 1,

  a(n) = 2n·Σ_j (−1)^j·C(2(n−1)−j, j)·(n−1−j)! = 2n·W_{n−1},

  where W_m = Σ_j (−1)^j·C(2m−j, j)·(m−j)! is the straight-table ménage
  number [A000271](../A000271/)(m).
- The rest is the A000271 program with a different print. W satisfies
  W_{m+1} = m(W_m + W_{m−1}) + W_{m−2}; at counter n the state is
  (a, b, c) = (−W_{n−2}, W_{n−1}, W_n), the update is `n*(b+c)-a`, and the
  print is 2n·W_{n−1} = `2*n*b`. The seeds `a=b=n=1;c=0` use Somos's
  extension W_{−1} = −1; see the A000271 and [A000179](../A000179/) pages
  for the proof of the recurrence and the start.

**Notes**

- Storing 2W instead of W, with `a=b=2;c=0;n=1` and `print(n*b)`: also 57
  bytes.
- Mathar's conjecture on the OEIS page, a(n) = 2n·A000271(n), is off by one:
  the derivation above proves a(n) = 2n·A000271(n−1) (for n = 1,
  2·A000271(1) = 0 but a(1) = 2). The OEIS formula with Bessel functions is
  numerical and not used.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 22 terms (up to a(22)); the bar is the whole b-file in 60 s.
- a(1559) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there (1558 terms in half a second).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000425), CC BY-SA 4.0.
