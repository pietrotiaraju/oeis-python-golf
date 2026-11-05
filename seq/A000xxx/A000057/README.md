# A000057

> Primes that divide at least one term in every Fibonacci sequence.
> — [OEIS A000057](https://oeis.org/A000057)

Offset 1: 2, 3, 7, 23, 43, 67, 83, 103, 127, 163, 167, 223, 227, 283, …

### Python 3 — 54 bytes

```python
W=n=a=b=1
while[W%n>0==print(n)]:W*=n*b;n+=1;a,b=b,a+b
```

**How it works**

- A prime p is a term exactly when the first Fibonacci number divisible by
  p is F(p+1), that is, when none of F(1), …, F(p) is a multiple of p
  (Max Alekseyev's comment on the OEIS page). This is the same as saying
  that p does not divide the product F(1)·F(2)···F(p): for every prime p
  the first multiple of p comes at most at F(p+1), because it divides
  F(p−1) or F(p+1) (F(5) = 5 for p = 5).
- `a,b` walk the Fibonacci numbers, and `W` is (n−1)! · F(1)·F(2)···F(n).
  Each step multiplies it by n and by `b` = F(n+1).
- The factorial is Wilson's theorem, as in [A000006](../A000006/): for a
  prime p, (p−1)! ≡ −1 (mod p), so W mod p is 0 exactly when p divides one
  of F(1), …, F(p). For composite n > 4, (n−1)! is already a multiple of n.
  For n = 4, 3! = 6 is not, but the Fibonacci product 1·1·2·3 = 6 brings
  the missing factor 2, so the usual squared factorial `P*=k*k` is not
  needed. For n = 1, W mod 1 = 0.
- `W%n>0==print(n)` is a chained comparison: `print(n)` runs only when
  W mod n > 0, and it is 1 byte shorter than `W%n and print(n)`.
- `while[...]:` prints in the loop condition: `[False]` is a non-empty
  list, so it is true.

**Notes**

- Without the factorial, `Q=n=a=b=1` +
  `while[Q%n>b%n<1==print(n)]:n+=1;Q*=b;a,b=b,a+b` is 56 bytes. It prints
  n when F(n+1) is the first Fibonacci number divisible by n, and that
  happens only for primes. The first index m with n | F(m) is the lcm of
  the first indices for the prime powers in n; since n+1 shares no factor
  with n, m = n+1 forces each of those to be the one of the prime itself,
  at most p+1, and for composite n their lcm is smaller than n+1 (for
  odd p and q, lcm(p+1, q+1) ≤ (p+1)(q+1)/2 ≤ pq).
- W grows like the Fibonacci product, about 0.1·n² digits, so the program
  slows down fast: 100 terms (up to 3643) take about 20 s and 140 terms
  (up to 5323) about 70 s. The bar is 100 terms in 60 s; the b-file has
  10000 terms (up to 619363).
- Computing the Fibonacci numbers modulo each prime is much faster but
  takes a nested loop and a separate primality test.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000057), CC BY-SA 4.0.
