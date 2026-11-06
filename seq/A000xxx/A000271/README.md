# A000271

> Sums of ménage numbers.
> — [OEIS A000271](https://oeis.org/A000271)

Offset 0: 1, 0, 0, 1, 3, 16, 96, 675, 5413, 48800, 488592, …

### Python 3 — 53 bytes

```python
a=b=n=1;c=0
while[print(b)]:a,b,c=-b,c,n*(b+c)-a;n+=1
```

**How it works**

- a(n) = W_n is the "straight table" ménage number: the number of
  permutations p of [n] with p(i) − i ∉ {0, 1}, and
  W_n = Σ_k (−1)^k·C(2n−k,k)·(n−k)!. Its differences are the ménage
  numbers [A000179](https://oeis.org/A000179), whose page uses the same
  recurrence.
- W satisfies W_q = (q−1)(W_{q−1} + W_{q−2}) + W_{q−3} for q ≥ 3 (listed
  in the OEIS entry). Proof: Gessel's g.f. Σ W_n xⁿ = f(t)/(1+x) with
  f(t) = Σ k!·t^k and t = x/(1+x)²; f satisfies t²f′ + (t−1)f + 1 = 0,
  which turns into x²(1+x)W′ = (1−x²−x³)W − (1−x²), and the coefficient
  of x^q of that is the recurrence, with corrections at q = 0 and q = 2
  only.
- At counter n the state is (a, b, c) = (−W_{n−2}, W_{n−1}, W_n), and the
  update computes W_{n+1} = n(W_n + W_{n−1}) + W_{n−2} = `n*(b+c)-a`. The
  program prints b, so the first value printed is W_0.
- The start n = 1 needs W_{−1}: with Somos's symmetric extension
  W(−1−n) = −W(n) it is −1, so the seeds are a = 1, b = W_0 = 1,
  c = W_1 = 0. The step n = 1 is the only one outside the proved range,
  and it gives 1·(0 + 1) − 1 = 0 = W_2.
- Storing a as −W_{n−2} turns three of the four seeds into 1, so one
  chained assignment `a=b=n=1` covers them. The price is one `-` in the
  update (`-b`); the unflipped seeds `a=-1;b=n=1;c=0` cost three bytes
  more.

**Notes**

- Three big-integer operations per term: the whole b-file (451 terms)
  prints in a fraction of a second; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits); a(1559) has 4302.
- Same recurrence, other layouts: printing the newest value,
  `a=n=0;b=-1;c=1` / `while[print(c)]:a,b,c=b,c,n*(b+c)+a;n+=1`, is
  55 bytes; printing the oldest, `a=1;b=c=0;n=2` with the plain update,
  is 54.
- No two-state update exists of the form W_n = p(n)W_{n−1} + q(n)W_{n−2}
  + r(n) + s(n)(−1)ⁿ with polynomials p, q, r, s of degree ≤ 4 (exact
  linear algebra on the first 80 terms). The known order-2 recurrence,
  (n−1)W_n = (n²−n−1)W_{n−1} + nW_{n−2} − 2(−1)ⁿ, needs a division and
  is far longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000271), CC BY-SA 4.0.
