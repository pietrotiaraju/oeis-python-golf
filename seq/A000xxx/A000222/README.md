# A000222

> a(n) = A058057(n,n-2).
> — [OEIS A000222](https://oeis.org/A000222)

Offset 0: 0, 0, 1, 3, 6, 38, 213, 1479, 11692, 104364, 1036809, …

### Python 3 — 66 bytes

```python
a=n=0;b=c=1
while[print(2*(c-a+n%2)+~b)]:a,b,c=b,-c,n*(c-b)-a;n+=1
```

**How it works**

- Row n of A058057 lists the coefficients of the "straight table" ménage
  hit polynomial P_n(t) = Σ_k C(2n−k,k)·(n−k)!·(t−1)^k, highest power
  first (C(2n−k,k) are the rook numbers of the 2n−1 cells i = π(i) and
  i+1 = π(i)). So a(n) is the coefficient of t²: the number of
  permutations π of 1..n with exactly two i such that π(i) = i or i+1,
  and a(n) = Σ_k (−1)^k·C(k,2)·C(2n−k,k)·(n−k)! (Manyama's formula in
  the entry).
- The program uses a shorter identity: with
  W_n = [A000271](https://oeis.org/A000271)(n) = Σ_k (−1)^k·C(2n−k,k)·(n−k)!
  (the t⁰ coefficient),

  a(n) = 2W_n + W_{n−1} + 2W_{n−2} − (−1)ⁿ   for every n ≥ 0,

  where W_{−1} = −1 and W_{−2} = 0.
- Proof. Σ_k C(k,2)·C(2m+k,k)·w^k = (m+1)(2m+1)·w²/(1−w)^(2m+3), so
  with w = −z and m = n−k, A(z) = Σ a(n)zⁿ = z²·Σ_m (m+1)(2m+1)·m!·z^m/(1+z)^(2m+3),
  while Σ W_n zⁿ = Σ_m m!·z^m/(1+z)^(2m+1) (Gessel). Put t = z/(1+z)²,
  u = 1/t and f(t) = Σ m!·t^m, so that W(z) = f/(1+z) and
  A(z) = z²/(1+z)³·Σ (2m²+3m+1)·m!·t^m. Now
  Σ (2m²+3m+1)·m!·t^m = u(2u−3)·f − u(2u−1), since the coefficient of
  t^m on the right is 2(m+2)! − 3(m+1)! = (m+1)(2m+1)·m! and the
  coefficients of t^(−2) and t^(−1) are 2 − 2 = 0 and 2 − 3 + 1 = 0.
  With z²u/(1+z)³ = z/(1+z), z(2u−3) = 2+z+2z² and z(2u−1) = 2+3z+2z²,
  this gives

  A(z) = (2+z+2z²)·W(z) − (2+3z+2z²)/(1+z) = (2+z+2z²)·W(z) − 1 − 2z − 1/(1+z).

  Taking the coefficient of zⁿ (with W_k = 0 for k < 0) gives the identity
  plus −1 at n = 0 and −2 at n = 1, and these are exactly W_{−1} and
  2W_{−1} when W_{−1} = −1, so the identity holds as stated.
- W_{−1} = −1 and W_{−2} = 0 are Somos's extension, the same seeds as in
  [A000179](../A000179/): with them W_{n+1} = n(W_n + W_{n−1}) + W_{n−2}
  holds at every step from n = 0 (proof on that page).
- The state is a = −W_{n−2}, b = −W_{n−1}, c = W_n. The recurrence becomes
  `a,b,c=b,-c,n*(c-b)-a`, and the seeds at n = 0 are a = 0, b = c = 1:
  `b=c=1` is 3 bytes under `b=1;c=-1` and costs one `-` in the update.
- In these variables a(n) = 2(c − a) − b − (−1)ⁿ, and
  −(−1)ⁿ = 2(n mod 2) − 1, so a(n) = `2*(c-a+n%2)+~b` (`~b` is −b−1).

**Notes**

- Each term is a few big-integer operations. The whole b-file
  (151 terms) prints at once; the bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits); a(1559) has 4303. All 1559 printed terms agree
  with Manyama's sum.
- Same length: with X_k = (−1)^k·W_k the recurrence has plain copies and
  (−1)ⁿ·a(n) = 2X_n − X_{n−1} + 2X_{n−2} − 1, and a(n) ≥ 0 lets `abs`
  take the sign off: `a=n=0;b=c=1` /
  `while[print(abs(2*(a+c)+~b))]:a,b,c=b,c,n*(b-c)-a;n+=1` (66 bytes).
- Longer routes: Manyama's sum with `from math import*`, `comb(k,2)`
  and `perm(n-k)` is 107 bytes. Without the (−1)ⁿ term the shortest link
  to W has polynomial coefficients, 2a(n) = 3n·W_{n−1} + (n²+n+1)·W_{n−2} + (n+3)·W_{n−3};
  the best version found (a search over small changes of basis and
  index shifts) is 76 bytes,
  `a=b=n=0;c=1` / `while[print(n*(~n*a-b-3*c)-a-3*b>>1)]:a,b,c=c,a,~-n*(a+c)+b;n+=1`.
  a(n) itself satisfies a recurrence of order 4 with cubic coefficients,
  and the full polynomial P_n(t) has none of order ≤ 3 with coefficients
  of degree ≤ 2 in n and in t.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000222), CC BY-SA 4.0.
