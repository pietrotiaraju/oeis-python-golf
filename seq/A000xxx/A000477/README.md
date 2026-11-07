# A000477

> a(n) = Sum_{k=1..n-1} k^2*sigma(k)*sigma(n-k).
> — [OEIS A000477](https://oeis.org/A000477)

Offset 1: 0, 1, 15, 76, 275, 720, 1666, 3440, 6129, 11250, …

### Python 3 — 78 bytes

```python
r=[1]
for n in r:r+=n+1,;print(n*n*sum(k-4*n*k+3*k**3for k in r if n%k<1)//24)
```

**How it works**

- The convolution has a closed form (Ridouane Oudra, 2020, on the OEIS
  page): 24·a(n) = n²·(3σ₃(n) + (1 − 4n)·σ(n)), where σ₃ is the sum of
  the cubes of the divisors. Summing per divisor k, the term is
  k − 4nk + 3k³, written `k-4*n*k+3*k**3` so that it ends in a digit:
  `3for` needs no space (only a SyntaxWarning on stderr). The identity
  makes the total divisible by 24.
- Why the identity holds: with S = Σσ(k)qᵏ = (1 − P)/24 and D = q·d/dq,
  the left side is the coefficient of qⁿ in D²S·S, and the right side
  combines D²S, D³S and D²Q. Ramanujan's equations DP = (P² − Q)/12,
  DQ = (PQ − R)/3, DR = (PR − Q²)/2 for the Eisenstein series
  P = E₂, Q = E₄, R = E₆ turn both sides into polynomials in P, Q and R,
  and the two polynomials are equal.
- The loop is the divisor-sum loop of [A000203](../A000203/): `r` is the
  list being iterated, and each pass appends n + 1, so the `for` never
  ends and `r` holds 1, …, n + 1 when the sum runs. The extra n + 1 never
  divides n, so `for k in r if n%k<1` runs over the divisors of n.
- At n = 1 the only term is 3 + 1 − 4 = 0, the leading 0 of the sequence.

**Notes**

- The factored term `k*(3*k*k+1-4*n)` is 79 bytes. The `while` form
  `n=1` / `while[print(…for k in range(1,n+1)if n%k<1)//24)]:n+=1` is 80
  bytes with that term; with `while 1:` and `n**2` it was 82.
- Exact integer arithmetic, so the program is right for every n.
- O(n) per term: the whole b-file (10000 terms) takes about 10 s here; the
  bar is the whole b-file in 60 s.
- [A000441](../A000441/) (weight k) and [A000499](../A000499/) (weight k³)
  are the same convolution with other weights.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |
| 2026-11-07 | Python 3 | 79 | self-extending list as loop and divisor range |
| 2026-11-07 | Python 3 | 78 | expanded term ending in `3for` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000477), CC BY-SA 4.0.
