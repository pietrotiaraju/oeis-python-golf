# A002202

> Values taken by totient function phi(m) (A000010).
> — [OEIS A002202](https://oeis.org/A002202)

Offset 1: 1, 2, 4, 6, 8, 10, 12, 16, 18, 20, 22, 24, …

### Python 3 — 111 bytes

```python
f=[n:=0];w=1
while 1:n+=1;f+=n-sum(f[d]for d in range(1,n)if n%d<1),;n<w*len(bin(w))or[w in f!=print(w),w:=w+1]
```

**How it works**

The program is the one of [A002181](../A002181/) (least m with
φ(m) = w), printing w itself instead of the least m.

- **Bound.** If φ(m) = w, then m < w·`len(bin(w))`, that is
  m ≤ w·(b + 1) with b the bit length of w:
  - m/φ(m) = Π_(p|m) p/(p − 1) is at most the same product over the
    first ω primes (ω the number of prime factors of m), and as the
    i-th prime is at least i + 1, that product is at most
    Π_(i≤ω) (i + 1)/i = ω + 1;
  - every odd prime factor p of m puts the even factor p − 1 into φ(m),
    and at most one prime factor is 2, so 2^(ω−1) divides w and
    ω ≤ b.
  So whether w is a value of φ is settled by φ(1), …, φ(w·len(bin(w))).
  (The cruder φ(m) ≥ √(m/2) would need φ up to 2w², which is far
  slower.)
- **φ by Gauss's identity.** Σ_(d|m) φ(d) = m gives
  φ(m) = m − Σ_(d|m, d<m) φ(d); `f` holds f[m] = φ(m) (f[0] = 0 is a
  placeholder) and `f+=n-sum(f[d]for d in range(1,n)if n%d<1),` adds
  φ(n).
- **Deciding.** w runs over 1, 2, 3, …; when n reaches
  w·len(bin(w)), `w in f!=print(w)` prints w if it is a value (the
  chained comparison calls `print` only when `w in f` holds) and
  `w:=w+1` moves on. The bound grows by at least 3 per step, so each n
  decides at most one w. The list `[…]` is built only for its side
  effects.

**Notes**

- The bound and exact integers: right for every n.
- φ is computed up to about 10 to 15 times the term, at O(n) per value:
  about 540 terms (w ≤ 1986) come in 30 s here. The b-file has 10000
  terms; the bar is 500 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002202), CC BY-SA 4.0.
