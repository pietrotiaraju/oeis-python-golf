# A000025

> Coefficients of the 3rd-order mock theta function f(q).
> — [OEIS A000025](https://oeis.org/A000025)

Offset 0: 1, 1, −2, 3, −3, 3, −5, 7, −6, 6, −10, 12, −11, 13, −17, 20, …

### Python 3 — 118 bytes

```python
m=0
while r:=[1]*-~m:
 k=m
 while k:
  for j in[*range(k,m+1)]*2:r[j]-=r[j-k]
  k-=1;r=[1]+[0]*2*k+r
 print(r[m]);m+=1
```

**How it works**

- Ramanujan's definition is f(q) = Σ_{n≥0} q^(n²) / ((1+q)²(1+q²)²⋯(1+qⁿ)²).
  Since q^(n²) = q·q³⋯q^(2n−1), the sum nests (Horner form):

  f = 1 + q/(1+q)² · (1 + q³/(1+q²)² · (1 + q⁵/(1+q³)² · (…))).

- For each m the program evaluates this from the inside out with k = m, …, 1,
  keeping the coefficients in the list `r`, and prints the coefficient of qᵐ.
- Dividing a series by 1 + q^k is `r[j]-=r[j-k]` for ascending j. Running
  over `[*range(k,m+1)]*2` does it twice, which divides by (1 + q^k)².
- `k-=1;r=[1]+[0]*2*k+r` then multiplies by q^(2k−1) (with the old k) and
  adds 1. The list keeps growing, but only the first m + 1 entries are ever
  read or divided.
- The innermost level is multiplied by q^m on the way out, so only its
  constant term reaches qᵐ: starting from `[1]*-~m` instead of
  `[1]+[0]*m` changes nothing, and levels with 2k − 1 > m are harmless.

**Notes**

- Each term is recomputed from scratch in about m² steps, so the program
  prints 400 terms in about 25 s and 509 in a minute. The bar is 400 terms in
  60 s; the b-file has 10 001.
- Fine's form f(q) = 1 − Σ_{n≥1} (−1)ⁿ qⁿ / ((1+q)⋯(1+qⁿ)) needs only one
  division per level but m levels and a fix for a(0); it came out at
  131 bytes.
- Packing the series into one big integer, with the divisions done as
  modular inverses `pow(1+B**k,-2,M)`, is exact but needs a signed decode of
  the digit and was longer (about 142 bytes).
- The 119-byte version began its `while 1:` body with `r=[1]*-~m;`. Naming
  the value in the loop condition is 1 byte shorter and keeps the loop
  going, because the list has m + 1 ≥ 1 entries.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 119 | first entry |
| 2026-11-05 | Python 3 | 118 | value named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000025), CC BY-SA 4.0.
