# A002181

> Least number k such that phi(k) = m, where m runs through the values (A002202) taken by phi.
> — [OEIS A002181](https://oeis.org/A002181)

Offset 1: 1, 3, 5, 7, 15, 11, 13, 17, 19, 25, 23, 35, …

### Python 3 — 120 bytes

```python
f=[n:=0];w=1
while 1:n+=1;f+=n-sum(f[d]for d in range(1,n)if n%d<1),;n<w*len(bin(w))or[w in f!=print(f.index(w)),w:=w+1]
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
  So every m with φ(m) = w is among 1, …, w·len(bin(w)).
- **φ by Gauss's identity.** Σ_(d|m) φ(d) = m gives
  φ(m) = m − Σ_(d|m, d<m) φ(d); `f` holds f[m] = φ(m) (f[0] = 0 is a
  placeholder) and `f+=n-sum(f[d]for d in range(1,n)if n%d<1),` adds
  φ(n).
- **Deciding.** w runs over 1, 2, 3, …; when n reaches w·len(bin(w)),
  `w in f` says whether w is a value of φ, and if so `f.index(w)`, the
  first position holding w, is the least k with φ(k) = w. The bound
  grows by at least 3 per step, so each n decides at most one w. The
  list `[…, w:=w+1]` is built only for its side effects.

**Notes**

- The bound and exact integers: right for every n.
- The bound makes the program compute φ up to about 30 times the value,
  at O(n) per value: about 350 terms come in 14 s here. The b-file has
  10000 terms; the bar is 400 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002181), CC BY-SA 4.0.
