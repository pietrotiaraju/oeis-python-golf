# A000341

> Number of ways to pair up {1..2n} so sum of each pair is prime.
> — [OEIS A000341](https://oeis.org/A000341)

Offset 1: 1, 2, 3, 6, 26, 96, 210, 1106, 3759, 12577, 74072, 423884, …

### Python 3 — 144 bytes

```python
f=lambda s:s<{0}or sum(f(s-{i})for i in s if{i+len(s)}-C)
n=1
while R:=range(3,4*n,2):C={a*b//2for a in R for b in R};print(f({*range(n)}));n+=1
```

**How it works**

- Two odd or two even numbers add up to an even number of at least 4, so
  every pair is one odd and one even number, and a(n) counts the perfect
  matchings between the odd numbers 2i + 1 (i = 0…n−1) and the even numbers
  2, 4, …, 2n with prime sums.
- `s` is the set of the i whose odd number 2i + 1 is still free. The even
  numbers are matched from the top down, so the next one is 2·len(s), and
  the sum is 2(i + len(s)) + 1. `f` tries every free i and recurses;
  `s<{0}` (a proper subset of {0}) is true only for the empty set, which
  counts 1.
- Primes by their complement: `C` holds (ab − 1)/2 = `a*b//2` for odd
  a, b ≥ 3, so for m ≥ 1, 2m + 1 is prime exactly when m is not in `C`.
  Every odd composite up to 4n − 1 is such a product (its smaller factor is
  at least 3 and its larger at most (4n − 1)/3), and the sums are at most
  4n − 1. `{i+len(s)}-C` is a non-empty set, hence true, exactly when the
  sum is prime: 4 bytes under `i+len(s)not in C`.
- The range of odd factors is named in the loop condition (never empty).

**Notes**

- Exact integers, a direct count of the matchings.
- A set of primes built by trial division,
  `Q:={p//2for p in range(4*n)if all(p%d for d in range(2,p))}`, is
  11 bytes longer. Matching the smallest free number to any partner
  (`s-{min(s),x}`) is longer than fixing the order of the even numbers.
- The search has no memo, so its time grows like a(n): a(12) = 423884
  prints within 10 s, a(13) = 2333828 at about 20 s, and a(14) would take
  minutes. The bar is 11 terms in 60 s; the b-file has 36 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 144 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000341), CC BY-SA 4.0.
