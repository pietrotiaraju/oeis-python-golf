# A002180

> Values taken by the half-totient function phi(m)/2.
> — [OEIS A002180](https://oeis.org/A002180)

Offset 2: 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, …

φ(m)/2 is an integer for m ≥ 3, so the terms are the v with φ(m) = 2v
for some m.

### Python 3 — 114 bytes

```python
f=[n:=0];w=2
while 1:n+=1;f+=n-sum(f[d]for d in range(1,n)if n%d<1),;n<w*len(bin(w))or[w in f!=print(w//2),w:=w+2]
```

**How it works**

- **Bound.** If φ(m) = w, then m < w·`len(bin(w))`, that is
  m ≤ w·(b + 1) with b the bit length of w:
  - m/φ(m) = Π_(p|m) p/(p − 1) is at most the same product over the
    first ω primes (ω the number of prime factors of m), and as the
    i-th prime is at least i + 1, that product is at most
    Π_(i≤ω) (i + 1)/i = ω + 1;
  - every odd prime factor p of m puts the even factor p − 1 into φ(m),
    so 2^(ω−1) divides w, and ω ≤ b.
  So whether w is a value of φ is settled by φ(1), …, φ(w·len(bin(w))).
- **φ by Gauss's identity.** Σ_(d|m) φ(d) = m gives
  φ(m) = m − Σ_(d|m, d<m) φ(d); `f` holds f[m] = φ(m) (f[0] = 0 is a
  placeholder) and `f+=n-sum(f[d]for d in range(1,n)if n%d<1),` adds
  φ(n).
- **Deciding.** w = 2v runs over 2, 4, 6, …; when n reaches
  w·len(bin(w)), `w in f` says whether w is a value, the term v = w/2 is
  printed if so, and w moves on. The bound grows by at least 8 per step,
  so each n decides at most one w. The list `[…, w:=w+2]` is built only
  for its side effects.

**Notes**

- The bound and exact integers: right for every n.
- The bound makes the program compute φ up to about 30 times the term,
  at O(n) per value: about 350 terms (v ≤ 616, m ≤ 14784) come in 14 s
  here. The b-file has 9999 terms; the bar is 400 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002180), CC BY-SA 4.0.
