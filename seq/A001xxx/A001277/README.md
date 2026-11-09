# A001277

> Number of permutations of length n by rises.
> — [OEIS A001277](https://oeis.org/A001277)

Offset 2: 1, 3, 12, 56, 321, 2175, 17008, 150504, 1485465, 16170035, …

A permutation of 1..n splits into maximal strings i, i+1, …, j of
consecutive integers standing next to each other in increasing order.
a(n) is the number of permutations of 1..n with exactly one such
string of length at least 2: column k = 1 of the
triangle [A136123](https://oeis.org/A136123) (David, Kendall and
Barton's table of permutations by rises). For n = 3 they are 123, 231 and 312.

### Python 3 — 43 bytes

```python
d=s=1;n=2
while[print(s)]:n+=1;d=d*n^1;s+=d
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
- For k = 1 the second binomial is 1 for every m < n, so
  a(n) = Σ_{m=1}^{n−1} D(m+1) = D(2) + D(3) + … + D(n). This also proves
  the entry's "apparently a(n) = A173184(n) − 1".
- `d=d*n^1` is the derangement step D(n) = n·D(n−1) + (−1)ⁿ: D(n−1) is
  odd exactly when n − 1 is even (induction on the same step), so
  n·D(n−1) is even for even n, where `^1` adds 1, and odd for odd n,
  where it subtracts 1.
- The loop starts at n = 2 with d = s = D(2) = a(2) = 1, prints the sum
  and adds the next derangement number. `[print(s)]` is a non-empty
  list, so the loop never ends.

**Notes**

- The walrus loop `while n:=n+1:` with `print(s)` at the end is 44
  bytes, `s+=(d:=d*n^1)` is 44 and `(-1)**n` instead of `^1` is 49.
- R. J. Mathar's conjectured recurrence a(n) = n·a(n−1) − (n−1)·a(n−3)
  holds for n ≥ 5: a(n) − a(n−1) = D(n) = (n−1)(D(n−1) + D(n−2))
  = (n−1)(a(n−1) − a(n−3)). As a three-variable loop it is 54 bytes.
- Columns k = 1 to 4 are [A001277](../A001277/), [A001278](../A001278/),
  [A001279](../A001279/) and [A001280](../A001280/).
- Exact integer arithmetic, so the program is right for every n; a(1559)
  is the first term with more than 4300 digits, where `print` stops on
  Python's int-to-str limit.
- The b-file has 22 terms (n = 2 to 23, synthesized from the entry);
  the bar is the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001277), CC BY-SA 4.0.
