# A001597

> Perfect powers: m^k where m > 0 and k >= 2.
> — [OEIS A001597](https://oeis.org/A001597)

Offset 1: 1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, …

### Python 3 — 102 bytes

```python
j=0
while[*map(print,sorted({m**k for m in range(2<<j)for k in range(2,2*j+3)if 0<m**k>>2*j<4}))]:j+=1
```

**How it works**

- The program prints the perfect powers block by block, block j holding
  the x with 4ʲ ≤ x < 4ʲ⁺¹. `m**k>>2*j` is ⌊x/4ʲ⌋, which is 1, 2 or 3
  exactly when x lies in the block, so `0<m**k>>2*j<4` keeps those.
- Every perfect power of the block is generated. If x = mᵏ with k ≥ 2 then
  m² ≤ x < 4ʲ⁺¹, so m < 2ʲ⁺¹ (`range(2<<j)`); and if m ≥ 2, then
  2ᵏ ≤ x < 2²ʲ⁺², so k ≤ 2j + 1. The exponent range goes one further, to
  2j + 2, only so that block 0 contains 1 = 1²; m = 0 gives 0, which the
  test drops.
- The set merges the many ways to write the same number (64 = 2⁶ = 4³ =
  8²), and `sorted` puts the block in order. Each block contains 4ʲ itself,
  so the list of `print` results is never empty and `while[…]:` goes on to
  the next block.

**Notes**

- Exact integer arithmetic, so the program is right for every n. Block j
  computes 2ʲ⁺¹(2j + 1) powers; the whole b-file (10000 terms, up to
  90706576 in block 13) prints in under a second, and the bar is the whole
  b-file.
- Testing every integer is shorter (65 bytes, below), but it walks through
  all 9·10⁷ integers below the last b-file term and keeps one dict entry
  per integer, so it runs out of memory long before the b-file ends.

## First 1000 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 1000 terms have to arrive in time.

### Python 3, 1000 terms — 65 bytes

```python
D={1:0};n=0
while 1:
 n+=1;m=D.pop(n,n);D[n*m]=m
 if m<n:print(n)
```

**How it works**

- The program walks through every integer n with a dict `D` that maps an
  upcoming perfect power to its base. When n is in `D` with base m, n is a
  perfect power: it is printed and its chain moves on to n·m. When it is
  not, `D.pop(n,n)` returns n itself, so `D[n*m]=m` starts the chain
  n², n³, … of the new base n.
- Only numbers that are not perfect powers start chains, and two such
  bases r ≠ s never share a power: rᵃ = sᵇ would make r and s powers of a
  common base (unique factorization), so one of them would be a perfect
  power. So each key of `D` belongs to one chain, nothing is overwritten,
  and every perfect power rᵏ (k ≥ 2, r not a perfect power) is reached
  along r's chain. `D={1:0}` covers 1: it pops base 0 < 1.

**Limits**

- Exact integers, so the program is right for every n, but it keeps a
  pending power for every integer below n: about 100 bytes each. The
  1000th term is 804357, reached in under 2 s with about 150 MB, which is
  where the bar is set; the whole b-file would need 9·10⁷ entries, about
  9 GB.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-13 | 102 | first entry |

**Python 3, 1000 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-13 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001597), CC BY-SA 4.0.
