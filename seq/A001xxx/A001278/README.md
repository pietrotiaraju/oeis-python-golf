# A001278

> Number of permutations of length n by rises.
> — [OEIS A001278](https://oeis.org/A001278)

Offset 4: 1, 11, 87, 693, 5934, 55674, 572650, 6429470, 78366855, …

A permutation of 1..n splits into maximal strings i, i+1, …, j of
consecutive integers standing next to each other in increasing order.
a(n) is the number of permutations of 1..n with exactly two such
strings of length at least 2: column k = 2 of the
triangle [A136123](https://oeis.org/A136123) (David, Kendall and
Barton's table of permutations by rises). For n = 4 the only one is 3412.

### Python 3 — 57 bytes

```python
d=a=b=m=2
while[print(b//2)]:m+=1;d=d*-~m^1;a+=~-m*d;b+=a
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
  so a(N+2) = T(N+2,2) = P₂(N).
- Here f(m) = (m−1)·D(m+1)/2. The loop variable is m, with d = D(m+1),
  a = 2·P₁(m) and b = 2·P₂(m): `a+=~-m*d` adds 2·f(m) = (m−1)·D(m+1)
  and `b+=a` adds the new running sum. b is twice the integer a(m+2), so
  `b//2` is exact.
- `d=d*-~m^1` is D(m+1) = (m+1)·D(m) + (−1)^(m+1): D(m) is odd exactly
  when m is even, so (m+1)·D(m) is odd for even m, where `^1` subtracts
  1, and even for odd m, where it adds 1.
- f(1) = 0 and f(2) = 1, so at m = 2 all four values are 2: d = D(3),
  a = b = 2, and the first line is b//2 = 1 = a(4). `[print(b//2)]` is a
  non-empty list, so the loop never ends.

**Notes**

- With n = m + 1 as the loop variable (`d=d*n^1`, `(n-2)*d`) it is 59
  bytes, halving each step (`~-m*d//2`, `print(b)`) is 59, the walrus
  loop is 60, and a direct sum over a list of derangement numbers with
  `math.comb` is 125.
- Columns k = 1 to 4 are [A001277](../A001277/), [A001278](../A001278/),
  [A001279](../A001279/) and [A001280](../A001280/).
- Exact integer arithmetic, so the program is right for every n; a(1559)
  is the first term with more than 4300 digits, where `print` stops on
  Python's int-to-str limit.
- The b-file has 22 terms (n = 4 to 25, synthesized from the entry);
  the bar is the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 57 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001278), CC BY-SA 4.0.
