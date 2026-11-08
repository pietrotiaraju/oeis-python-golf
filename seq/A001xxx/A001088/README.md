# A001088

> Product of totient function: a(n) = Product_{k=1..n} phi(k) (cf. A000010).
> — [OEIS A001088](https://oeis.org/A001088)

Offset 0: 1, 1, 1, 2, 4, 16, 32, 192, 768, 4608, 18432, 184320, 737280, 8847360, 53084160, 424673280, 3397386240, 54358179840, 326149079040, 5870683422720, …

### Python 3 — 74 bytes

```python
a=n=F=1
while[print(a)]:a*=sum(1%n==pow(k,F,n)for k in range(n));n+=1;F*=n
```

**How it works**

- a(n) = a(n − 1)·φ(n), so the program multiplies a, starting at
  a(0) = 1, by φ(1), φ(2), φ(3), … after printing each term.
- φ(n) counts the k < n with k^F ≡ 1 (mod n), where F = n! is kept by
  `F*=n`. For a k coprime to n, the order of k divides φ(n), which is at
  most n − 1 and so divides n!; for a k sharing a factor with n, no
  positive power is 1 mod n. That avoids importing gcd (the
  `math.gcd(k,n)<2` version is 79 bytes).
- `1%n==` instead of `==1` makes n = 1 count its single residue 0, so
  φ(1) = 1 (mod 1 everything is 0).

**Notes**

- Exact integer arithmetic; only Euler's theorem is used.
- The modular powers with an n!-sized exponent make term n cost about
  n² log n multiplications mod n. The whole b-file (497 terms) prints in
  about 16 s, and 698 terms in 60 s; the bar is the whole b-file.
- a(n) passes the 4300-digit int-to-str limit of Python 3.11+ around
  n ≈ 1700, far beyond 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 74 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001088), CC BY-SA 4.0.
