# A228444

> Primes expressible as concatenation of phi(sigma(n)) and sigma(phi(n)).
> — [OEIS A228444](https://oeis.org/A228444)

Offset 1: 11, 23, 43, 67, 127, 631, 839, 3631, 1831, 4831, 3691, 6491, …

For n = 1, 2, 3, … write φ(σ(n)) and then σ(φ(n)) as one decimal number;
the terms are the ones that come out prime, in order of n. So the sequence is
neither sorted nor free of repeats: a(8) = 3631 comes from n = 32 and
a(9) = 1831 from n = 34, and 108127 appears for n = 160 and n = 170.

### Python 3 — 127 bytes

```python
g=lambda m,e=0:m+sum(e*d or-g(d)for d in range(1,m)if m%d<1)
n=1
while[g(p:=int(f"{g(g(n,1))}{g(g(n),1)}"))>p-2!=print(p)]:n+=1
```

**How it works**

- `g(m)` is φ(m) and `g(m,1)` is σ(m), from one lambda and no `import`:
  - σ(m) = m + the sum of the proper divisors d of m;
  - φ(m) = m − Σ φ(d) over the proper divisors d, which is Gauss's identity
    Σ_{d|m} φ(d) = m solved for the d = m term.
- The two differ only in what each proper divisor adds: `e*d or-g(d)` is d
  when e = 1 (d ≥ 1 is truthy) and −φ(d) when e = 0. For m = 1 the range is
  empty and both give 1.
- `int(f"{g(g(n,1))}{g(g(n),1)}")` is the concatenation of φ(σ(n)) and
  σ(φ(n)). Both parts are at least 1, so p ≥ 11.
- p is prime exactly when φ(p) = p − 1, i.e. `g(p)>p-2`: for composite p a
  divisor 1 < d < p is not coprime to p, so φ(p) ≤ p − 2.
- `g(p:=…)>p-2!=print(p)` is a chained comparison: print runs only when the
  first link holds. `while[…]:n+=1` loops forever (`[x]` is always true).

**Notes**

- Everything is exact integer arithmetic, and the recursion depth of `g` is
  the length of a divisor chain, at most log₂ m.
- It is slow on purpose: every n costs a sweep up to p, and p grows like n².
  Here the 16th term appears after about 32 s and the 18th after 60 s; the
  bar is 16 terms in 60 s. The b-file goes up to n = 972375 and
  p ≈ 5·10¹², far beyond any of these programs. All 1020 b-file terms
  match a sieve with a deterministic Miller–Rabin test.
- Faster but longer versions:
  - `import math` and `g=lambda m,e=0:sum(k**e for k in range(m+e)if math.gcd(k,m)==k**e)`
    with the same main loop: 146 bytes, 25 terms in 60 s. `range(m+e)`
    covers both cases: for φ it is 0…m−1 (k = 0 counts only when m = 1),
    for σ it is 0…m, and k = 0 adds 0.
  - The same with trial division up to √p,
    `all(p%k for k in range(2,isqrt(p)+1))and print(p)`: 182 bytes,
    102 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 127 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A228444), CC BY-SA 4.0.
