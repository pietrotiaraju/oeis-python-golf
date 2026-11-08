# A001069

> Log2*(n) (version 2): take log_2 of n this many times to get a number < 2.
> — [OEIS A001069](https://oeis.org/A001069)

Offset 1: 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, …

### Python 3 — 54 bytes

```python
A=[0]
for x in A:print(x);A+=A[len(bin(~len(A)))-5]+1,
```

**How it works**

- Taking log₂ once more is the same as going from n to ⌊log₂ n⌋: the
  thresholds 2, 4, 16, 65536, … where the count changes are integers, so
  log₂ applied j times is < 2 exactly when it is < 2 after flooring.
  Hence a(1) = 0 and a(n) = a(⌊log₂ n⌋) + 1 for n ≥ 2.
- The list A holds a(1), a(2), …, with A[i] = a(i + 1). Iterating over A
  while appending to it prints every term as it is reached.
- The next term is a(n) for n = len(A) + 1, and ⌊log₂ n⌋ − 1, the index
  of a(⌊log₂ n⌋), is `len(bin(~len(A)))-5`: ~L = −(L + 1), and
  `bin(-(L+1))` is `-0b` followed by the binary digits of n, one character
  longer than `bin(n)`. That is 1 byte under `len(bin(len(A)+1))-4`.

**Notes**

- Exact: only integer bit lengths, no floating-point logarithms.
- The list holds one small integer per term, so memory, not time, is the
  only limit; the whole b-file (1000 terms) prints at once and is the
  bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001069), CC BY-SA 4.0.
