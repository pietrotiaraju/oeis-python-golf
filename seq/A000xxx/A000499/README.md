# A000499

> a(n) = Sum_{k=1..n-1} k^3*sigma(k)*sigma(n-k).
> — [OEIS A000499](https://oeis.org/A000499)

Offset 1: 0, 1, 27, 184, 875, 2700, 7546, 17600, 35721, 72750, …

### Python 3 — 79 bytes

```python
r=[1]
for n in r:r+=n+1,;print(n**3*sum(2*k**3+k-n*k*3for k in r if n%k<1)//24)
```

**How it works**

- Ridouane Oudra's formula in the entry,
  24a(n) = n³·(2σ₃(n) + (1 − 3n)·σ(n)), turns the convolution into one
  divisor sum: Σ_{k|n} (2k³ + k − 3nk).
- Why it holds: with G = Σ σ(k)qᵏ = (1 − E₂)/24, a(n) is the coefficient of
  qⁿ in G·D³G, where D = q·d/dq, so 576·G·D³G = E₂·D³E₂ − D³E₂. E₂·D³E₂ is
  a quasimodular form of weight 10, and that space has dimension 5, spanned
  by E₁₀, DE₈, D²E₆, D³E₄ and D⁴E₂, whose n-th coefficients are multiples of
  σ₉(n), nσ₇(n), n²σ₅(n), n³σ₃(n) and n⁴σ(n). These five sequences are
  linearly independent already on n = 1..5, so the formula, checked
  against the definition for n ≤ 300, holds for every n.
- The loop is the [A000203](../A000203/) one: `r` is the list being looped
  over and each pass appends n+1, so the `for` never ends and `r` holds
  1, …, n+1. The extra n+1 never divides n, so `if n%k<1` over all of `r`
  picks exactly the divisors of n.
- `n*k*3for` needs no space (only a `SyntaxWarning` on stderr). The `//24`
  is exact because the quotient is the integer a(n); single summands may be
  negative, the total is not.

**Notes**

- Other versions: the summand as `k*(2*k*k+1-3*n)` with `range(1,n+1)` and
  `while 1:…;n+=1`, 82 bytes (with the growing list, 80).
- Exact integer arithmetic; correctness for every n rests on the
  quasimodular argument above.
- Each term costs n divisibility tests: about 26300 terms in 60 s here. The
  b-file has 10000 terms (up to a(10000)); the bar is the whole b-file in
  60 s, which takes about 8 s.
- a(n) < n⁷, so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |
| 2026-11-07 | Python 3 | 79 | growing-list loop, expanded summand |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000499), CC BY-SA 4.0.
