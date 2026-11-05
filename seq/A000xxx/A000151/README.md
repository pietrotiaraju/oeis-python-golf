# A000151

> Number of oriented rooted trees with n nodes. Also rooted trees with n nodes and 2-colored non-root nodes.
> — [OEIS A000151](https://oeis.org/A000151)

Offset 1: 1, 2, 7, 26, 107, 458, 2058, 9498, 44947, 216598, 1059952, 5251806, …

The g.f. satisfies A(x) = x·∏ₖ (1−xᵏ)^(−2aₖ): a tree is a root with a multiset
of subtrees, each attached in one of two colours.

### Python 3 — 88 bytes

```python
R=[n:=1]
while[print(R[-1])]:R+=2*sum(-~j*R[j]*sum(R[~j::~j])for j in range(n))//n,;n+=1
```

**How it works**

- Taking x·d/dx of the logarithm of A(x)/x gives
  x·A′/A − 1 = Σₖ 2k·aₖ·Σ_{m≥1} x^{km}. Multiplying by A and reading off
  the coefficient of x^{n+1}:

  n·a(n+1) = 2·Σₖ₌₁ⁿ k·aₖ·(a(n+1−k) + a(n+1−2k) + ⋯),

  where the inner sum runs while km ≤ n.
- `R` holds a(1), …, a(n), oldest first, and `n` is its length. For
  k = j+1, `-~j` is k, `R[j]` is aₖ, and `R[~j::~j]` is
  `R[-k]`, `R[-2k]`, …, which are a(n+1−k), a(n+1−2k), … and stop exactly
  when km would pass n.
- The new term is appended and printed on the next pass. The division by n is
  exact, so `//` is safe.

**Notes**

- Each step costs about n·log n big-integer operations, so the program prints
  the 1300 terms of the b-file in about 5 s and about 2800 terms in a minute.
  The bar is the whole b-file (1300 terms) in 60 s.
- a(n) grows like 5.65ⁿ, so it reaches Python's 4300-digit int-to-str limit
  near n = 5700; the program is correct beyond that once the limit is lifted.
- `for x in R:print(x);` in place of the `while` header, or
  `enumerate(R)` with `//len(R)` in place of the counter `n`, cost the same
  88 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000151), CC BY-SA 4.0.
