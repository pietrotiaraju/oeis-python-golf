# A001279

> Number of permutations of length n by rises.
> — [OEIS A001279](https://oeis.org/A001279)

Offset 6: 3, 53, 680, 8064, 96370, 1200070, 15778800, 220047400, …

A permutation of 1..n splits into maximal strings i, i+1, …, j of
consecutive integers standing next to each other in increasing order.
a(n) is the number of permutations of 1..n with exactly three such
strings of length at least 2: column k = 3 of the
triangle [A136123](https://oeis.org/A136123) (David, Kendall and
Barton's table of permutations by rises). For n = 6 they are 125634, 341256 and 563412.

### Python 3 — 71 bytes

```python
a=b=c=w=0;d=2
while w:=w+1:d=d*(w+3)^1;a+=-~w*w*d;b+=a;c+=b;print(c//6)
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
  so a(N+3) = T(N+3,3) = P₃(N).
- Here f(m) = (m−1)(m−2)·D(m+1)/6. The loop variable is w = m − 2, with
  d = D(m+1) = D(w+3) and a, b, c = 6·P₁, 6·P₂, 6·P₃ at m: `a+=-~w*w*d`
  adds (w+1)·w·D(w+3) = 6·f(m), and `b+=a;c+=b` carry the running sums.
  c is six times the integer a(m+3), so `c//6` is exact.
- `d=d*(w+3)^1` is D(n) = n·D(n−1) + (−1)ⁿ with n = w + 3: D(n−1) is odd
  exactly when n − 1 is even, so `^1` adds 1 when n·D(n−1) is even (n
  even) and subtracts 1 when it is odd (n odd).
- f(1) = f(2) = 0, so the loop starts at w = 0 (m = 2) with d = D(3) = 2
  and all sums 0. The first pass, m = 3, gives d = 9, a = b = c = 18 and
  prints 3 = a(6). `w:=w+1` is never 0, so the loop never ends.

**Notes**

- Printing first (`while[print(c//6)]:w+=1;…` from d = 9,
  a = b = c = 18, w = 1) is 72 bytes; the same with m as the loop
  variable and each step divided by 6 is 72 too.
- Columns k = 1 to 4 are [A001277](../A001277/), [A001278](../A001278/),
  [A001279](../A001279/) and [A001280](../A001280/).
- Exact integer arithmetic, so the program is right for every n; a(1559)
  is the first term with more than 4300 digits, where `print` stops on
  Python's int-to-str limit.
- The b-file has 20 terms (n = 6 to 25, synthesized from the entry);
  the bar is the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001279), CC BY-SA 4.0.
