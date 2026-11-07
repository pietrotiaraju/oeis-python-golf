# A000586

> Number of partitions of n into distinct primes.
> — [OEIS A000586](https://oeis.org/A000586)

Offset 0: 1, 0, 1, 1, 0, 2, 0, 2, 1, 1, …

### Python 3 — 122 bytes

```python
*a,n=1,0;t=1;P=[]
while[print(a[-1])]:n+=1;P+=[-n][:t%n];t*=n*n;a+=sum(p*(sum(a[p::2*p])-sum(a[2*p::2*p]))for p in P)//-n,
```

**How it works**

- **The recurrence.** The generating function is G(x) = Π_p (1 + x^p) over
  the primes p. Taking the logarithmic derivative,
  x·G′(x)/G(x) = Σ_p p·x^p/(1 + x^p) = Σ_p Σ_{m≥1} (−1)^(m−1)·p·x^(pm), and
  comparing coefficients of x^n gives

  n·a(n) = Σ_{p≤n} p·(a(n−p) − a(n−2p) + a(n−3p) − …),

  with a(k) = 0 for k < 0. The right side is n·a(n) exactly, so the floor
  division by n is exact.
- **Slices.** When a(n) is computed, the list `a` holds a(0), …, a(n−1).
  The primes are stored negated, so for p = −q the slice `a[p::2*p]` is
  a(n−q), a(n−3q), … and `a[2*p::2*p]` is a(n−2q), a(n−4q), …; a start index
  below −len gives an empty slice, which covers 2q > n. With the negated p
  the sum is −n·a(n), hence `//-n`.
- **The prime list.** Before n is tested, t = ((n−1)!)². By Wilson's theorem
  t ≡ 1 (mod n) for a prime n; for a composite n > 4, n divides (n−1)!, for
  n = 4 it divides 3!² = 36, and t%1 = 0. So `[-n][:t%n]` is [−n] exactly
  when n is prime, and `t*=n*n` prepares the next test.
- `*a,n=1,0` sets a = [1] and n = 0; `print(a[-1])` in the loop condition
  prints a(0) = 1 first and then each new term (the [A000007](../A000007/)
  loop).

**Notes**

- Other versions that print the same terms:
  - the subset-sum table doubled in length each round, printing its upper
    half (`A[p:]=map(sum,zip(A[p:],A))` for each prime p < n, same Wilson
    test): 130 bytes, the whole b-file in about 10 s;
  - the same table with the test inside the update,
    `A[p:]=map(sum,zip(A[p:],*[A][:t%p]))` on every p: 127 bytes, but about
    60 s for the b-file here, too close to the bar;
  - the form Π(1 − x^(2p))/(1 − x^p), `sum(a[p::p])-2*sum(a[2*p::2*p])`:
    also 122 bytes.
- Exact integer arithmetic, so the program is right for every n.
- About 15500 terms in 60 s here (the b-file takes about 27 s). The b-file has
  10001 terms (up to a(10000)); the bar is the whole b-file in 60 s.
- a(10000) has 32 digits and the growth is subexponential, so the 4300-digit
  int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 188 | first entry |
| 2026-11-06 | Python 3 | 146 | use squared-factorial Wilson tests and combine the initial state |
| 2026-11-07 | Python 3 | 122 | logarithmic-derivative recurrence with negated-prime slices |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000586), CC BY-SA 4.0.
