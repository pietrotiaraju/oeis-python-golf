# A001855

> Sorting numbers: maximal number of comparisons for sorting n elements by binary insertion.
> — [OEIS A001855](https://oeis.org/A001855)

Offset 1: 0, 1, 3, 5, 8, 11, 14, 17, 21, 25, 29, 33, 37, 41, 45, 49, 54, 59, 64, 69, …

### Python 3 — 43 bytes

```python
s=n=0
while[print(s)]:n+=1;s+=len(bin(n))-2
```

**How it works**

- Binary insertion puts the k-th element into the k − 1 sorted ones with at most ⌈log₂ k⌉
  comparisons, so a(n) = ∑_(k=1..n) ⌈log₂ k⌉ = n⌈log₂ n⌉ − 2^⌈log₂ n⌉ + 1 (the closed form in
  the entry).
- So a(n + 1) − a(n) = ⌈log₂(n + 1)⌉, which is the bit length of n: `len(bin(n))-2` (one byte
  under `n.bit_length()`). `s` is the running sum, printed before each step, starting from
  a(1) = 0.

**Notes**

- Exact integer arithmetic. The b-file has 10000 terms; the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001855), CC BY-SA 4.0.
