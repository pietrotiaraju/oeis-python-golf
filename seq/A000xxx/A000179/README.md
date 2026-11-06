# A000179

> Ménage numbers: a(0) = 1, a(1) = -1, and for n >= 2, a(n) = number of permutations s of [0, ..., n-1] such that s(i) != i and s(i) != i+1 (mod n) for all i.
> — [OEIS A000179](https://oeis.org/A000179)

Offset 0: 1, −1, 0, 1, 2, 13, 80, 579, 4738, 43387, 439792, …

### Python 3 — 60 bytes

```python
a=b=n=1;c=0
while[print(a+b-1//n)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- The program runs the "straight table" ménage numbers
  W_n = [A000271](https://oeis.org/A000271)(n) = Σ_k (−1)^k·C(2n−k,k)·(n−k)!
  and prints their differences: a(n) = W_n − W_{n−1}. In generating
  functions, Σ W_n xⁿ = Σ_k k!·x^k/(1+x)^(2k+1) (Gessel) and
  Σ a(n) xⁿ = (1−x)·Σ W_n xⁿ (Jovovic's g.f. of A000179), which includes
  a(0) = W_0 = 1 and a(1) = W_1 − W_0 = −1.
- W satisfies W_n = (n−1)(W_{n−1} + W_{n−2}) + W_{n−3} for n ≥ 3
  (listed in A000271). Proof: f(t) = Σ k!·t^k satisfies
  t²f′ + (t−1)f + 1 = 0, and with t = x/(1+x)² this turns into
  x²(1+x)W′ = (1−x²−x³)W − (1−x²) for W(x) = f(t)/(1+x). Comparing the
  coefficients of xⁿ gives the recurrence plus corrections at n = 0 and
  n = 2 only.
- At counter n the state is (a,b,c) = (−W_{n−2}, W_{n−1}, W_n), the
  update computes W_{n+1} = n(W_n + W_{n−1}) + W_{n−2} = `n*(b+c)-a`, and
  the program prints the middle difference W_{n−1} − W_{n−2} = `a+b`.
  This is the [A000271](../A000271/) program with a different print.
- The start n = 1 needs W_{−1} = −1 (Somos's symmetry W(−1−n) = −W(n)),
  so the seeds are a = 1, b = W_0 = 1, c = W_1 = 0; storing a negated
  makes three of them 1, one chained assignment. The only step outside
  the proved range is n = 1, which gives 1·(0 + 1) − 1 = 0 = W_2.
- With W_{−1} = −1 the first difference is W_0 − W_{−1} = 2, the value
  a(0) = 2 that the D-finite recurrences of A000179 use; `-1//n`
  subtracts 1 at n = 1 only (the pass that prints a(0)), giving the
  conventional a(0) = 1.
- Printing the newest difference instead, from the state
  (W_{n−2}, W_{n−1}, W_n) with seeds `a=n=0;b=-1;c=1` and `-0**n`, was
  62 bytes.

**Notes**

- Each term is three big-integer operations. The whole b-file
  (451 terms) prints in well under a second; the bar is the whole
  b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits); a(1559) has 4302.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 62 | first entry |
| 2026-11-06 | Python 3 | 60 | print the middle state (seeds `a=b=n=1;c=0`), as in A000271 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000179), CC BY-SA 4.0.
