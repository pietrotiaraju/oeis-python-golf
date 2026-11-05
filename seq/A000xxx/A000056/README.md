# A000056

> Order of the group SL(2,Z_n).
> — [OEIS A000056](https://oeis.org/A000056)

Offset 1: 1, 6, 24, 48, 120, 144, 336, 384, 648, 720, 1320, 1152, 2184, 2016, 2880, 3072, 4896, 3888, 6840, 5760, …

### Python 3 — 81 bytes

```python
f=lambda n:n*n-sum(f(d)for d in range(1,n)if n%d<1)
n=1
while[print(n*f(n))]:n+=1
```

**How it works**

- a(n) = n·J₂(n), where J₂(n) is the number of rows (a, b) mod n with
  gcd(a, b, n) = 1 (Jordan's totient). The first row of a matrix with
  ad − bc ≡ 1 is such a row, since a common divisor of a, b and n divides 1.
  Every such row is a first row: Bézout gives ax + by + nz = 1, so
  (a b; −y x) has determinant 1. For a fixed row, (c, d) ↦ ad − bc is onto
  Z_n (scale that completion by r to get determinant r), so each value, 1
  among them, is hit by n²/n = n pairs (c, d).
- Each of the n² pairs (a, b) has gcd(a, b, n) = n/d for exactly one
  divisor d of n, and the pairs with that gcd are (n/d)·(a′, b′) with
  (a′, b′) mod d and gcd(a′, b′, d) = 1: J₂(d) of them. So n² = Σ_{d|n} J₂(d),
  and `f` is J₂(n) = n² − Σ J₂(d) over the divisors d < n.
- `f` has no cache: it recomputes J₂ of every divisor, and of their divisors
  in turn. Divisor chains are short, so this stays cheap.
- `while[print(…)]:n+=1` prints in the loop condition: `[None]` is a
  non-empty list, so it is true.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  recursion is only as deep as a chain of divisors, at most log₂ n + 1
  calls, far from the recursion limit.
- The whole b-file (1000 terms) prints in about 0.2 s; the bar is the whole
  b-file in 60 s.
- Counting the rows directly is also 81 bytes:
  `import math` / `n=1` /
  `while[print(n*sum(math.gcd(n,i//n,i)<2for i in range(n*n)))]:n+=1`.
  i runs over all pairs (i mod n, i//n), and gcd(n, i, i//n) =
  gcd(n, i mod n, i//n). It costs n² gcds a term, though: the whole b-file
  takes about 58 s, too close to the bar to count on.
- `sum(math.gcd(n,i,i//n)<2for i in range(n**3))` counts the triples
  (a, b, c), which is a(n) itself, and saves the `n*` (80 bytes). With n³
  gcds a term it prints about 180 terms a minute, under the bar.
- Keeping the J₂ values in a list,
  `L=[1];n=1` / `while[print(n*L[-1])]:n+=1;L+=n*n-sum(L[d-1]for d in range(1,n)if n%d<1),`,
  is 83 bytes.
- Having `f` return a(n) through n³ = Σ_{d|n} a(d)·n/d (the Dirichlet series
  ζ(s−3)/ζ(s−1)) is 86 bytes, and trial division with `a-=a//p//p` for each
  prime p | n, starting from a = n³, is 103.
- With sympy, n·Σ_{d|n} μ(n/d)·d² through `mobius` and `divisors` is
  86 bytes, longer than the plain program, so there is no sympy entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000056), CC BY-SA 4.0.
