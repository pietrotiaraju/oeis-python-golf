# A001034

> Orders of noncyclic simple groups (without repetition).
> — [OEIS A001034](https://oeis.org/A001034)

Offset 1: 60, 168, 360, 504, 660, 1092, 2448, 2520, 3420, 4080, 5616, 6048, 6072, 7800, 7920, 9828, 12180, 14880, 20160, 25308, 25920, 29120, …

### Python 3 — 945 bytes

```python
from math import*
j=0
while j:=j+1:
 L=8**j;S={sum((c-35)*92**i for i,c in enumerate(w))for w in rb"+y '8. ;g7 sGW wLj #7,0 /:*: {){[ KuQc #7HI& sSFT/ S{r:[ /R${/9 +EGE%g k%SKwh #74@7n #7|fpih SCxodN1$ o&I6|<u' '\Ca#*z*- S[FY3-ea4 #7th551o_+ #7LJ@x[/m+ #K]+y/G,k~$ #7H9v}kb=x*I& #KEIr$Sw0A>B{j-gd$ #7@Cqz&gWwIdg}eg1CgWHWQXn6a*".split()}|{factorial(n)//2for n in range(5,4*j)}
 for q in range(2,2<<j):
  if all(q%d or d**j%q<1for d in range(2,isqrt(q)+1)):
   for Q in q,-q:
    x=y=i=1;S|={prod((R:=Q**(d-48))*(R-1)//Q for d in D)//gcd(9%len(D),Q-1)for D in b"26 268< 25689< 268:<>B 28<>BDHN".split()}|{q**12*(q**8+q**4+1)*(q**6-1)*(q*q-1),(z:=(q%-~(p:=gcd(q,6))==p>1<q>4)*q**p*(q**p+1)*(q-1)),z*(p<3)*q**10*(q**6+1)*(q*q-1)*(q**3+1)}
    while x*x<L**6:i+=1;t=Q**~-i*(Q**i-1);x*=t;y*=t**(~i%2);r=q**(i//2);S|={abs(x)//gcd(i,Q-1),y>>q%2}|{y//r//(r+s)//gcd(4,r-s)*(i>5)for s in(1,-1)}
 [print(x)for x in sorted(S-{6,12,72,720,12096})if L//8<x<=L]
```

**How it works**

- By the classification of finite simple groups, a noncyclic simple group
  is an alternating group Aₙ (n ≥ 5), a group of Lie type, the Tits group
  ²F₄(2)′ or one of the 26 sporadic groups. Round j collects in a set `S`
  every such order up to L = 8ʲ and prints, sorted, the ones in
  (L/8, L]; the set takes care of coincidences (|A₈| = |PSL(3,4)|,
  PSL(2,4) ≅ PSL(2,5), …).
- Sporadic and Tits orders: a bytes literal of 27 numbers, each written in
  base 92 with the least significant digit first and digit d as the
  character chr(35 + d); `sum((c-35)*92**i for i,c in enumerate(w))`
  reads one back. Base 92 keeps out the space and the quote.
- Alternating: n!/2 for 5 ≤ n < 4j, since (4j)!/2 > 8ʲ.
- Lie type over F_q: no group over F_q is smaller than PSL(2,q), of order
  q(q² − 1)/gcd(2, q − 1) > 8ʲ once q ≥ 2ʲ⁺¹, so q < `2<<j`. q is a prime
  power iff q divides dʲ for each divisor d ≤ √q of q (its exponent is
  at most j): `all(q%d or d**j%q<1for d in range(2,isqrt(q)+1))`.
- Ennola duality: the order polynomial of the unitary group ²Aₙ(q) and of
  ²E₆(q) is that of Aₙ(q) or E₆(q) evaluated at −q, up to sign. So every
  q is run as `Q` = q and `Q` = −q; negative values never get printed.
- Classical groups: `x` = Q^(i(i−1)/2)·∏ₗ₌₂..ᵢ (Qˡ − 1) is ±|SL(i,q)| or
  ±|SU(i,q)|, and x/gcd(i, Q − 1) is |PSL(i,q)| or |PSU(i,q)|. `y` takes
  only the factors with l even (`t**(~i%2)`), which is ±|Sp(2m,q)| at
  i = 2m: `y>>q%2` is |PSp(2m,q)| = |Ω(2m+1,q)|, and with r = qᵐ,
  y/(r(r + s))/gcd(4, r − s) is |PΩ^±(2m,q)| for s = ±1, kept for
  2m ≥ 6 (`*(i>5)`, else 0).
- Exceptional groups: |G(q)| = q^Σ(d−1)·∏(q^d − 1)/|Z| over the degrees d
  of the Weyl group's invariants, stored as chr(48 + d): "26" G₂, "268<"
  F₄, "25689<" E₆, "268:<>B" E₇, "28<>BDHN" E₈. The center is
  gcd(3, q − 1) for E₆, gcd(2, q − 1) for E₇ and trivial otherwise, which
  is `gcd(9%len(D),Q-1)`: 9 mod 2, 4, 8 is 1, 9 mod 6 is 3, 9 mod 7 is 2.
  With Q = −q the same line gives ²E₆(q).
- ³D₄(q) = q¹²(q⁸ + q⁴ + 1)(q⁶ − 1)(q² − 1). With p = gcd(q, 6), the Suzuki
  and small Ree groups are q^p(q^p + 1)(q − 1) for q = 2²ⁿ⁺¹ and 3²ⁿ⁺¹,
  that is q ≡ p (mod p + 1) with p > 1, and q > 4 drops Sz(2) and ²G₂(3);
  ²F₄(q) is the Suzuki order times q¹⁰(q⁶ + 1)(q² − 1)(q³ + 1) (`p<3`).
- The rank loop runs `while x*x<L**6`: once |x| ≥ L³, every classical
  group of larger rank over this q is larger than L, because the smallest
  later order, cubed, exceeds |x| (|x| < 2q^(i²−1), the later orders are
  above q^(i(i+1)/2)/8; for q < 600 and i < 40, where that estimate is not
  enough, it was checked directly).
- The formulas also give the non-simple PSL(2,2) ≅ S₃, PSL(2,3) ≅ A₄,
  PSU(3,2), Sp(4,2) ≅ S₆ and G₂(2), of orders 6, 12, 72, 720 and 12096; no
  simple group has those orders, so they are removed. ²F₄(2) is kept out
  by q > 4 and its derived group, the Tits group, is in the table.

**Notes**

- Exact integer arithmetic. It relies on the classification of finite
  simple groups and the standard order formulas (R. A. Wilson, The Finite
  Simple Groups, Table 1.1; the ATLAS for the sporadic orders).
- Each round redoes everything, which is cheap: the whole b-file (10 000
  terms, up to 526 696 525 195 500) comes out in about 12 s; the bar is the
  whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 945 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001034), CC BY-SA 4.0.
