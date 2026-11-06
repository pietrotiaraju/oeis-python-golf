# A000435

> Normalized total height of all nodes in all rooted trees with n labeled nodes.
> — [OEIS A000435](https://oeis.org/A000435)

Offset 1: 0, 1, 8, 78, 944, 13800, 237432, 4708144, 105822432, 2660215680, …

### Python 3 — 75 bytes

```python
n=1
while 1:
 a=0;f=1
 for k in range(n-1,0,-1):f*=k;a=a*n+f
 print(a);n+=1
```

**How it works**

- The OEIS formula is a(n)=(n−1)!·Σₖ₌₀ⁿ⁻² nᵏ/k!.
  Expanding the factorial ratio makes every summand an integer,
  but computing each factorial separately would repeat work.
- Horner's rule evaluates the polynomial in n from its highest
  power down. With k descending from n−1 to 1, the update `f*=k`
  makes f=(n−1)!/(k−1)!, and `a=a*n+f` incorporates the
  coefficient of n^(k−1).
- For n=4, the successive pairs (f,a) are (3,3), (6,18),
  (6,78). This is 3!·(1+4+4²/2!)=78, with no rational
  intermediate values.
- At n=1 the loop is empty and the accumulator stays 0, the correct
  normalized total height of a one-node tree. For each larger n,
  `a=0;f=1` starts a fresh Horner evaluation.

**Notes**

- This is Luschny's integer Horner algorithm, linked on the OEIS
  page. It uses n−1 inner iterations and constant-size accumulator
  state, apart from the growing integers themselves.
- The exact factorial sum proves correctness beyond the reference
  values. Python 3.11+ eventually stops when output exceeds its
  default 4300-digit conversion limit, an interpreter limit.
- **Reference-file correction.** The repository's b-file restores
  leading digits missing from the downloaded OEIS values at indices
  841, 846, 857, 858, 859, 929, 936, 938, 939, 940 and 941.
  As recorded when the sequence was added, the repaired values were
  checked against both the factorial sum and this integer algorithm;
  the other reference values are unchanged.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000435), CC BY-SA 4.0.
