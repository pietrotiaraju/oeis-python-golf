# A002211

> Continued fraction for Khintchine's constant.
> — [OEIS A002211](https://oeis.org/A002211)

Offset 0: 2, 1, 2, 5, 1, 1, 2, 1, 1, 3, 10, 2, 1, 3, 2, 24, 1, 3, 2, 3, 1, …

### Python 3 — 383 bytes

```python
B=8;p=b=0
while B:=2*B:
 for U in 1<<B,-1<<B:
  z=l=-1;k=1
  while k<B:l+=(t:=U//(k<<k));z+=2*t//k;k+=1
  Z=[z+l*l//U]
  for m in range(5,B,2):Z+=sum(map(int.__mul__,Z,Z[::-1]))*2//(m*U),
  S=sum((z-U)//n//j for n,z in enumerate(Z,1)for j in range(n,2*n));E=U
  while k:E=U+E*S//(k*(l+B+4));k-=1
  a,b=b,E
 c=-U
 while c*U and a//c==b//U:p+=k==p!=print(a//c);k+=1;a,c,b,U=c,a%c,U,b%U
```

**How it works**

- **Bounds on K.** The first nine lines are the program of
  [A002210](../A002210/), which explains them: at precision B they
  compute K_lo ≤ K ≤ K_hi as a/2^B (`a`, from the pass U = 2^B) and
  b/(−2^B) (`b`, from the pass U = −2^B, which stores negated values), via
  ln K · ln 2 = Σ_(n≥1) c_n·(ζ(2n) − 1), Euler's recurrence for ζ(2n),
  a Taylor polynomial for exp, and directed floors.
- **Partial quotients of an interval.** If ⌊K_lo⌋ = ⌊K_hi⌋ = q, every
  number between them, K included, has integer part q, so q is the next
  partial quotient. Then t ↦ 1/(t − q) maps the interval (reversed) onto
  one that contains the complete quotient of K, and the test repeats.
  Euclid does both ends at once: a/c becomes c/(a mod c) and b/U becomes
  U/(b mod U); Python's `//` and `%` work with the negative denominator
  as well (b mod U has the sign of U, and the ratio stays positive). The
  loop stops at the first disagreement, or when an end becomes an exact
  integer (`c*U` is 0), which ends that level.
- **New terms only.** After Horner's loop `k` is 0, so it counts the
  quotients of this level; `p` counts the ones printed, and
  `p+=k==p!=print(a//c)` prints exactly when k reaches p (the chained
  comparison calls `print` only then). Every level starts again from
  the first quotient, so a level with a narrower agreement never prints
  anything new and never prints anything wrong. `c=-U` turns the sign of
  the last pass back into 2^B.

**Notes**

- Every printed term is proven by the two bounds. K is not known to be
  irrational: if it were rational, the program would wait forever at its
  last partial quotient (the interval would always contain an integer)
  instead of printing a wrong one. The 1000 terms of the b-file all come
  out.
- A partial quotient takes about 1.03 decimal digits on average (Lévy's
  constant), so a level gives about as many terms as digits: 617 at
  B = 2048 (after about 11 s here) and 1280 at B = 4096 (about 115 s
  here).
- The b-file has 1000 terms; the bar is 500 terms in 60 s, which arrive
  with the B = 2048 level, well within half the time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 383 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002211), CC BY-SA 4.0.
