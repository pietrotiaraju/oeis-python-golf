# A001204

> Continued fraction for e^2.
> — [OEIS A001204](https://oeis.org/A001204)

Offset 0: 7, 2, 1, 1, 3, 18, 5, 1, 1, 6, 30, 8, 1, 1, 9, 42, 11, 1, 1, 12, 54, …

### Python 3 — 52 bytes

```python
k=2
while[print(4*k-2+2//k,k,1,1,k+1,sep='\n')]:k+=3
```

**How it works**

- e² = [7; 2, 1, 1, 3, 18, 5, 1, 1, 6, 30, …]: after the 7 the partial
  quotients come in blocks 3j−1, 1, 1, 3j, 12j+6 (j ≥ 1). This is Euler's
  expansion of e^(2/m) for m = 1 (Perron, *Die Lehre von den
  Kettenbrüchen*, 1929, p. 138); it also follows from tanh 1 =
  [0; 1, 3, 5, 7, …], as the OEIS comment notes.
- Cut the blocks one place earlier, as 12j+6, 3j+2, 1, 1, 3j+3 for
  j ≥ 0: then the first block starts with 7 = 6+1. With k = 3j+2 the block
  is 4k−2, k, 1, 1, k+1, and `2//k` adds the 1 only at k = 2.
- One `print` per block, `sep='
'` puts each quotient on its own line.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001204), CC BY-SA 4.0.
