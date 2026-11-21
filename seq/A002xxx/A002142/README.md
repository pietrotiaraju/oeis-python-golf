# A002142

> Primes p == 1 (mod 4) where class number of Q(sqrt p) increases.
> — [OEIS A002142](https://oeis.org/A002142)

Offset 1: 5, 229, 401, 577, 1129, 1297, 7057, 8761, 14401, 32401, 41617, 57601, 90001

### Python 3 — 255 bytes

```python
k=s=1;m=0
while 1:
 k+=4;s+=-~s*-~s<=k;h=0;S={(a,b)for b in range(1,-~s*all(k%d for d in range(2,-~s)),2)for a in range(s-b+2&-2,s-~b,2)if(k-b*b)%(2*a)<1}
 while S:
  a,b=S.pop();h+=1
  while(a:=(k-b*b)//a,b:=s-(s+b)%a)in S:S-={(a,b)}
 if h>m:print(k);m=h
```

**How it works**

- **Which sequence.** The primes p ≡ 1 (mod 4) whose class number h(p)
  of the real field Q(√p) is larger than that of every smaller such
  prime: h = 1 up to 229, which has h = 3, then 5, 7, 9, 11, 21, 27, 43,
  45, … at the terms. The data are these records.
- **Candidates.** `k` runs over 5, 9, 13, … and `s` = ⌊√k⌋ follows it
  (`s+=-~s*-~s<=k`: one step of 4 passes at most one square once s ≥ 1,
  as (s + 2)² > s² + 2s + 4 ≥ k + 4). Trial division up to s tests
  primality; for a composite k the range of b is empty, so h = 0 and
  nothing is printed.
- **Reduced forms.** An indefinite form (a, b, c) of discriminant
  b² − 4ac = k is reduced when 0 < b < √k and √k − b < 2|a| < √k + b;
  then a and c have opposite signs. The set holds (A, b) with A = 2|a|:
  b odd (b² ≡ k (mod 4)) from 1 to s, A even with s − b < A ≤ s + b
  (√k is irrational; `s-b+2&-2` is the first even number above s − b),
  and 2A | k − b², which is 4|a| dividing k − b² = 4|ac|. Every form is
  primitive, as k is prime.
- **Cycles.** Gauss's reduction step ρ(a, b, c) = (c, b′, ·), with
  b′ ≡ −b (mod 2|c|) and √k − 2|c| < b′ < √k, permutes the reduced forms,
  and two of them are properly equivalent exactly when they lie on the
  same ρ-cycle (see D. A. Buell, *Binary Quadratic Forms*, Springer 1989,
  ch. 3). Changing (a, b, c) into (−a, b, −c) commutes with ρ and
  corresponds to multiplying an ideal by √k, of norm −k < 0, so the walk
  on (A, b), which forgets the signs, runs through a cycle together with
  its negative: these walks are the ideal classes in the wide sense, and
  their number is h(k). In the walk 2|c| = (k − b²)/A, and
  `s-(s+b)%a` is the largest b′ ≤ s with b′ ≡ −b (mod 2|c|).
- **Counting.** Each pass pops a form and walks its cycle, removing every
  form it meets, until the walk comes back to the popped one, which is no
  longer in the set: h is the number of pops. `m` is the largest h so
  far, and k is printed when h beats it.

**Notes**

- For a prime p ≡ 1 (mod 4) the fundamental unit has norm −1, so the
  wide and narrow class numbers agree; the count does not need this.
- Exact integer arithmetic throughout. Collecting the forms takes about
  k/4 steps per prime: the 13th term, 90001, comes after about 6
  reference seconds. The bar is the whole b-file, 13 terms, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 255 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002142), CC BY-SA 4.0.
