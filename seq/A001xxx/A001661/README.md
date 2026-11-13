# A001661

> Largest number not the sum of distinct positive n-th powers.
> — [OEIS A001661](https://oeis.org/A001661)

Offset 2: 128, 12758, 5134240, 67898771, 11146309947, 766834015734, …

128 is the largest number that is not a sum of distinct squares (Sprague),
12758 the largest that is not a sum of distinct cubes, and so on. Only
seven terms are known; a(6) was proved by Fuller and Nichols.

### Python 3 — 143 bytes

```python
n=1
while 1:
 n+=1;S=k=1;X=16<<n*n
 while~S>>(P:=k**n)&(1<<P)-1:r=X<2*P;X<<=r;S|=S<<P&(1<<X)-1;S**=r<1;k+=1-k*r
 print(len(bin(~S&(1<<P)-1))-3)
```

**How it works**

- `S` is a bitset of subset sums: bit m is set when m is a sum of distinct
  powers among 1ⁿ, …, (k−1)ⁿ. It starts as 1 (the empty sum) and each new
  power P = kⁿ adds the shifted copy, `S|=S<<P`, cut to the X lowest bits
  (`&(1<<X)-1`). Powers are positive, so a sum that once reaches X never
  comes back below it: the cut `S` is exactly the set of sums below X.
- Before adding P the loop tests the window P, P + 1, …, 2P − 1:
  `~S>>P&(1<<P)-1` is 0 exactly when all these bits of `S` are set (which
  needs 2P ≤ X). Then the answer is the largest m < P whose bit is clear:
  `~S&(1<<P)-1` keeps the clear bits below P and `len(bin(x))-3` is the
  position of its top one.
- If the window does not fit (`r=X<2*P`), X doubles and the search starts
  again from S = 1, k = 1 (`S**=r<1` is `S**=0`, and `k+=1-k*r` sets k
  to 1); otherwise `S**=True` leaves S alone and `k+=1-k*r` is `k+=1`.
  X starts at 2^(n²+4) bits, so n = 2, 3, 4 need a few cheap restarts and
  n = 5 (window at k = 37, 2P ≈ 1.4·10⁸ bits) none.

**Why it is right for every n**

Write R_j for the set of sums of distinct numbers among 1ⁿ, 2ⁿ, …, jⁿ (the
empty sum 0 included). When the loop stops, P = kⁿ, the bits P, …, 2P − 1
of `S` are all set, so 2P ≤ X, and `S` agrees with R_{k−1} below X.

1. *2kⁿ ≥ (k + 1)ⁿ.* Otherwise ((k+1)/k)ⁿ > 2, and then (j/(j+1))ⁿ < 1/2
   for every j ≤ k, so jⁿ < kⁿ/2^(k−j) and 1ⁿ + … + (k−1)ⁿ < kⁿ = P: every
   element of R_{k−1} is below P, and the bits P, …, 2P − 1 could not be
   set. Since ((j+1)/j)ⁿ decreases in j, also 2jⁿ ≥ (j + 1)ⁿ for all j ≥ k.
2. *Every m ≥ P is a sum of distinct n-th powers.* R_{k−1} contains the
   interval [P, P + L) with L = kⁿ. If R_{j−1} contains [P, P + L) with
   L ≥ jⁿ, then R_j ⊇ R_{j−1} ∪ (R_{j−1} + jⁿ) contains [P, P + L + jⁿ),
   and L + jⁿ ≥ 2jⁿ ≥ (j + 1)ⁿ by step 1. By induction the intervals grow
   without bound.
3. *The printed number is a(n).* A number m < P = kⁿ can only use powers
   below kⁿ, so it is a sum of distinct n-th powers exactly when m ∈ R_{k−1},
   i.e. when bit m of `S` is set. The program prints the largest m < P whose
   bit is clear; all m between it and P are sums, and so is every m ≥ P
   by step 2. Such an m exists: the loop never stops at k = 1 (bit 1 of
   S = 1 is clear), so P ≥ 4, and 2 is never a sum of distinct n-th
   powers.
4. *The loop stops.* Sprague (1948) proved that every large enough number is
   a sum of distinct n-th powers, so a = a(n) exists (Kim gave an explicit
   bound; see the entry). For every large k both (k−1)ⁿ − (k−2)ⁿ > a and
   2kⁿ < (k−1)ⁿ + 2(k−2)ⁿ hold (the differences grow without bound, and the
   second inequality divided by kⁿ tends to 2 < 3). Then every m in
   [kⁿ, 2kⁿ) is in R_{k−1}: y = m − (k−1)ⁿ > a is a sum of distinct powers;
   if y < (k−1)ⁿ those powers are at most (k−2)ⁿ; otherwise
   z = y − (k−2)ⁿ > a is a sum of distinct powers with
   z < 2kⁿ − (k−1)ⁿ − (k−2)ⁿ < (k−2)ⁿ, so those are at most (k−3)ⁿ. Either
   way m uses distinct powers below kⁿ, so the test passes at that k.
5. *The restarts end.* Let k₁ be such a k. With a fixed X, a run either
   stops at some k with 2kⁿ ≤ X or reaches a k with 2kⁿ > X and doubles X.
   Once X ≥ 2k₁ⁿ, the run reaches k₁ at the latest and stops there.

**Golf notes**

- `1<<P` instead of `2**P`: CPython computes `2**P` by repeated squaring,
  and for P ≈ 2·10⁸ that alone takes seconds.
- Without the cut and the restarts, `S|=S<<P` on the whole set is 98 bytes
  and just as exact, but `S` then holds every sum up to 1ⁿ + … + kⁿ; for
  n = 6 it grows by tens of megabytes per second until the program is
  killed. With the cut, n = 6 starts with X = 2⁴⁰ bits (128 GiB), and the
  first `1<<X` fails at once with a MemoryError, after the bar; a machine
  with that much memory would go on and find a(6) without a restart.
- `S|=S<<P&(1<<X)-1` cuts only the shifted copy: `S` is already below 2^X.

**Notes**

- Exact integer arithmetic throughout; the stopping test and the answer
  rest on the lemma above, and the loop's end on Sprague's theorem, so the
  program is right for every n given the memory.
- a(2), a(3), a(4) come at once, a(5) after a few seconds (about 11 s on
  this busy machine, peak 240 MB); then n = 6 stops the program with a
  MemoryError, as above. The b-file has the 7 known terms; the bar is 4
  terms (up to a(5)) in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 143 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001661), CC BY-SA 4.0.
