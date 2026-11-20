# A002088

> Sum of totient function: a(n) = Sum_{k=1..n} phi(k), cf. A000010.
> — [OEIS A002088](https://oeis.org/A002088)

Offset 0: 0, 1, 2, 4, 6, 10, 12, 18, 22, 28, 32, 42, 46, 58, 64, 72, 80, 96, 102, …

### Python 3 — 116 bytes

```python
N=1
while 1:
 s=0;P=[*range(N:=N*2)]
 for k in range(1,N):k<N//2or print(s);s+=P[k];P[k::k]=[x-P[k]for x in P[k::k]]
```

**How it works**

- **Sieve.** Gauss's identity Σ_(d | n) φ(d) = n gives
  φ(n) = n − Σ_(d | n, d < n) φ(d). A pass starts from P[j] = j and, for
  k = 1, 2, … in increasing order, subtracts P[k] from P[k], P[2k], P[3k],
  … (`P[k::k]`). When k is reached, every proper divisor of k has already
  subtracted its φ from P[k], so P[k] = φ(k) at that moment.
- **Sums.** Before the subtraction (which zeroes P[k], no longer needed),
  `s` holds φ(1) + … + φ(k−1) = a(k−1), and `s+=P[k]` adds φ(k).
- **Doubling.** A sieve needs a bound, so the passes run with
  N = 2, 4, 8, …, each from scratch with `s=0`. A pass prints a(k−1) only
  for N/2 ≤ k < N, that is a(N/2 − 1), …, a(N − 2), and the next pass
  starts at a(N − 1): every term once, in order, and a(0) = 0 from the
  first pass. Redoing the earlier part at most doubles the work.

**Notes**

- A pass costs about N·ln N list operations; the whole b-file (50001
  terms, up to n = 50000) comes in about a second, with N = 65536 at the
  end. The bar is the whole b-file in 60 s.
- Counting φ(n) one n at a time is shorter but quadratic: see the separate
  record below.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002088), CC BY-SA 4.0.
