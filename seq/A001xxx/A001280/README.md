# A001280

> Number of permutations of length n by rises.
> — [OEIS A001280](https://oeis.org/A001280)

Offset 8: 11, 309, 5805, 95575, 1516785, 24206055, 396475975, …

A permutation of 1..n splits into maximal strings i, i+1, …, j of
consecutive integers standing next to each other in increasing order.
a(n) is the number of permutations of 1..n with exactly four such
strings of length at least 2: column k = 4 of the
triangle [A136123](https://oeis.org/A136123) (David, Kendall and
Barton's table of permutations by rises). For n = 8 one of the 11 is 12563478.

### Python 3 — 84 bytes

```python
a=b=c=e=0;d=9;w=1
while w:=w+1:d=d*(w+3)^1;a+=(w**3-w)*d;b+=a;c+=b;e+=c;print(e//24)
```

**How it works**

- Cut a permutation of 1..n into its maximal strings, singletons
  included. They are m intervals of 1..n, so their lengths form a
  composition of n into m parts, and the order of the strings is a
  permutation of 1..m with no succession (no i directly followed by
  i + 1, or the two strings would merge). Conversely, every composition
  with every succession-free order gives back one permutation with exactly
  these strings. Exactly k parts ≥ 2 can be placed in C(m,k) ways, and
  those k parts minus 1 each form a composition of n − m into k parts, so
  with S(m) succession-free permutations of 1..m the triangle is
  T(n,k) = Σₘ C(m,k)·C(n−m−1,k−1)·S(m).
- By inclusion–exclusion over the m − 1 possible successions,
  S(m) = Σⱼ (−1)ʲ C(m−1,j)(m−j)!. Since m·C(m−1,j) = (m−j)·C(m,j) and
  (m−j)·(m−j)! = (m+1−j)! − (m−j)!, m·S(m) = Σⱼ (−1)ʲ C(m,j)(m+1−j)! − D(m),
  and Pascal's rule turns D(m+1) = Σⱼ (−1)ʲ C(m+1,j)(m+1−j)! into the same
  sum, so m·S(m) = D(m+1), the derangement numbers of
  [A000166](../../A000xxx/A000166/) (S(m) is
  [A000255](../../A000xxx/A000255/)(m−1)).
- So f(m) = C(m,k)·S(m) = C(m−1,k−1)·D(m+1)/k, and T(n,k) =
  Σₘ C(n−m−1,k−1)·f(m) is f summed k times: with P₁(N) = f(1) + … + f(N)
  and each Pᵢ₊₁ the running sum of Pᵢ, P_k(N) = Σₘ C(N−m+k−1,k−1)·f(m),
  so a(N+4) = T(N+4,4) = P₄(N).
- Here f(m) = (m−1)(m−2)(m−3)·D(m+1)/24. The loop variable is w = m − 2,
  so the weight is (w+1)·w·(w−1) = w³ − w, d = D(w+3), and
  a, b, c, e = 24·P₁, 24·P₂, 24·P₃, 24·P₄ at m: `a+=(w**3-w)*d` adds
  24·f(m) and `b+=a;c+=b;e+=c` carry the running sums. e is 24 times the
  integer a(m+4), so `e//24` is exact.
- `d=d*(w+3)^1` is D(n) = n·D(n−1) + (−1)ⁿ with n = w + 3: D(n−1) is odd
  exactly when n − 1 is even, so `^1` adds 1 when n·D(n−1) is even (n
  even) and subtracts 1 when it is odd (n odd).
- f(m) = 0 for m < 4, so the loop starts at w = 1 (m = 3) with
  d = D(4) = 9 and all sums 0. The first pass, m = 4, gives d = 44,
  a = b = c = e = 264 and prints 11 = a(8). `w:=w+1` is never 0, so the
  loop never ends.

**Notes**

- Printing first from d = 44, a = b = c = e = 11, w = 2 with each step
  divided by 24 is 85 bytes; the loop variable v = m − 3 from 0, with
  weight `v*-~v*(v+2)`, is 85; a direct sum over a list of derangement
  numbers with `math.comb` is 125.
- Columns k = 1 to 4 are [A001277](../A001277/), [A001278](../A001278/),
  [A001279](../A001279/) and [A001280](../A001280/).
- Exact integer arithmetic, so the program is right for every n; a(1559)
  is the first term with more than 4300 digits, where `print` stops on
  Python's int-to-str limit.
- The b-file has 16 terms (n = 8 to 23, synthesized from the entry);
  the bar is the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001280), CC BY-SA 4.0.
