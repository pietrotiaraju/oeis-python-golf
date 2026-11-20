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

## First 600 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 600 terms have to arrive in time.

### Python 3, 600 terms — 76 bytes

```python
s=0;n=F=1
while[print(s)]:s+=sum(1%n==pow(k,F,n)for k in range(n));n+=1;F*=n
```

**How it works**

- φ(n) counts the k in [0, n) that are units modulo n. F = n! is a
  multiple of φ(n), which is at most n, so k^F ≡ 1 (mod n) for every unit
  k (Euler's theorem); a non-unit k shares a prime factor with n, and so
  does every power of it, so k^F ≢ 1. Hence `1%n==pow(k,F,n)` is exactly
  the test gcd(k, n) = 1, also at n = 1, where 1 % 1 = 0 = pow(0, 1, 1)
  counts the one k (the test of [A000010](../../A000xxx/A000010/)).
- s adds up φ(1) + … + φ(n) and is printed before each step, so a(0) = 0
  comes first; `F*=n` after `n+=1` keeps F = n!.

**Limits**

- F = n! has about n·log₂ n bits, so every power takes that many
  squarings and term n costs about n²·log n steps: the first 600 terms come
  in about 22 reference seconds, and a(1000) would take over a minute. Counting
  with `math.gcd(n,k)<2` is much faster but three bytes longer (79).

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 116 | first entry |

**Python 3, 600 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 76 | first entry: Euler's theorem with F = n! |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002088), CC BY-SA 4.0.
