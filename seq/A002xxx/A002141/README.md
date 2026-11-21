# A002141

> Class numbers of quadratic fields.
> — [OEIS A002141](https://oeis.org/A002141)

Offset 3: 1, 1, 5, 6, 7, 7, 9, 53, 60, 66, 83, 83, 136, 136, 185, 185, 185, 312, …

### Python 3 — 201 bytes

```python
r=7;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,;a=h=0
  while any(pow(-r,d//2,d)<2for d in Q):r+=24
  while 3*a*a<r:a+=1;h+=sum((x:=b*b+r>>2)%a<1>a*a-x+(b<0)for b in range(-a|1,a,2))
  print(h)
 P*=q*q;q+=1
```

**How it works**

- **Which sequence.** The entry gives only the name and the source, the
  table of D. H. Lehmer, E. Lehmer and D. Shanks, *Integer sequences
  having prescribed quadratic character*, Math. Comp. 24 (1970),
  433–451. Its terms are the class numbers h(−N) of Q(√−N), where N is
  the least positive integer ≡ 7 (mod 8) with Legendre(−N, q) = −1 for
  every odd prime q ≤ p, and a(n) belongs to p = prime(n − 1) (a(3) to
  p = 3, a(4) to p = 5, …). This is the integer version of
  [A001988](../A001988/)/[A001989](../A001989/), which ask N to be prime
  and give 7, 7, 127, 463, … with class numbers 1, 1, 5, 7, …; here
  N = 7, 7, 127, 247, 463, 487, 1423, 33247, …, and 247 = 13·19 gives the
  even term 6. The reconstruction matches all 37 terms: an exact search
  finds N up to p = 163 (N = 3402396344407 for the last four terms), and
  the class numbers, from counting forms up to N = 2430943 and, for the
  nine larger N, from Cohen's rapidly converging series for L(1, χ),
  agree with the data.
- **Odd primes.** `q` runs over 3, 4, 5, … with `P` = ((q − 1)!)², so by
  Wilson's theorem `P%q` is 1 exactly when q is prime, and each new odd
  prime is appended to `Q` and gives one term.
- **The search.** −N is a non-residue of the odd prime d exactly when
  `pow(-r,d//2,d)` is d − 1 (Euler's criterion; it is 0 when d | r and
  1 for a residue). Legendre(−N, 3) = −1 means N ≡ 1 (mod 3), so N runs
  over 7, 31, 55, … ≡ 7 (mod 24). Every condition for p is also one for
  the next prime, so the search resumes at the last N.
- **N is squarefree.** If N = f²m with f > 1, then f is odd and prime to
  every q ≤ p (Legendre(−N, q) ≠ 0), so m ≡ N (mod 8) and
  Legendre(−m, q) = Legendre(−N, q): m < N would also qualify. So −N is
  a fundamental discriminant, h(−N) is the class number of Q(√−N), and
  every form of discriminant −N is primitive.
- **Class number.** It counts the reduced forms ax² + bxy + cy² with
  4ac − b² = N: |b| ≤ a ≤ c, and b ≥ 0 when |b| = a or a = c (b is
  odd). The loop takes b odd in [−a, a) and x = (b² + N)/4 = ac
  (`b*b+r>>2` is exact), and counts the pairs with a | x and
  a² − x + [b < 0] ≤ 0, that is c > a, or c = a with b > 0. The forms
  with |b| < a and c > a come once each; (a, a, c) is counted as b = −a;
  of the pair (a, ±b, a) only b > 0 is kept; and (a, −a, a) would mean
  N = 3a², which is not squarefree. Unlike the prime case of
  [A001989](../A001989/), N may be composite, so a = c and |b| = a > 1 do
  occur. a ≤ c gives 3a² ≤ N, so a runs while 3a² < r (N is never 3a²).

**Notes**

- Exact integer arithmetic throughout. The search and the count both
  grow with N: here (about 1.9 times slower than the reference) a(22),
  N = 2430943, comes after 1 s, and a(23), N = 242675623, after 40 s;
  the bar is 20 terms (a(3) to a(22)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-21 | Python 3 | 201 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002141), CC BY-SA 4.0.
