# A002025

> Smaller of an amicable pair: (a,b) such that sigma(a) = sigma(b) = a+b, a < b.
> — [OEIS A002025](https://oeis.org/A002025)

Offset 1: 220, 1184, 2620, 5020, 6232, 10744, 12285, 17296, 63020, 66928, 67095, …

### Python 3 — 130 bytes

```python
a=n=1
while 1:
 n*=2;s=[0]*n
 for d in range(1,n):s[2*d::d]=map(d.__add__,s[2*d::d])
 while a<n>(b:=s[a]):s[b]==a<b!=print(a);a+=1
```

**How it works**

- (a, b) is an amicable pair when s(a) = b and s(b) = a with a ≠ b,
  where s(m) = σ(m) − m is the sum of the proper divisors of m. The
  program checks every a in increasing order and prints the smaller member a.
- **Sieve.** `s[2*d::d]=map(d.__add__,s[2*d::d])` adds d to s[2d],
  s[3d], …, so after all d < n the list holds s(m) for every m < n.
- **Doubling.** The sieve is rebuilt for n = 2, 4, 8, …, and a carries
  on from where it stopped. `a<n>(b:=s[a])` sets b = s(a) and goes on
  only while b < n, so that s(b) can be read from the list; the first a
  with s(a) ≥ n waits for the next sieve, twice as long. So every a is
  checked exactly once, in order.
- `s[b]==a<b!=print(a)` is a chained comparison: it prints only when
  s(b) = a and a < b (print's None differs from b). a < b leaves out the
  perfect numbers and puts each pair under its smaller member.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Each
  stage costs about n ln n additions and repeats the earlier ones, at
  most doubling the work. The first a with s(a) ≥ n is near n/3, so a
  stage of size n settles the a up to about n/3.
- Memory is the limit: the list holds a separate int object for almost
  every entry, about 36 bytes each, so the stage n = 2²³ (which settles
  a up to about 2.5·10⁶) needs some 500 MB.
- The b-file has 415523 terms, a up to 10¹⁷. The bar is 35 terms in
  30 s: the stage n = 2²¹ ends with the 35th term, a = 643336, after
  about 13 s here; the next stage brings 12 more at about 29 s.
- Same program as [A002046](../A002046/) apart from the printed variable.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 130 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002025), CC BY-SA 4.0.
