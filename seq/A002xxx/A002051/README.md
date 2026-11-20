# A002051

> Steffensen's bracket function [n,2].
> — [OEIS A002051](https://oeis.org/A002051)

Offset 1: 0, 0, 1, 9, 67, 525, 4651, 47229, 545707, 7087005, 102247051, 1622631549, 28091565547, …

### Python 3 — 70 bytes

```python
r=[t:=1];p=1
while[print(t-p>>1)]:p*=2;r=[t:=t+x for x in[sum(r)-t]+r]
```

**How it works**

- [n, 2] = Σ_{k=3}^{n} S₂(n, k)·(k − 1)!/2 (the entry's sum with k = s + 1):
  the partitions of {1, …, n} into k ≥ 3 blocks, with the blocks arranged
  in an undirected cycle. Without the halving and over all k,
  Σₖ S₂(n, k)·(k − 1)! counts necklaces of partitions of n labeled beads,
  [A000629](../../A000xxx/A000629/)(n − 1). Taking out k = 1 and k = 2
  (S₂(n, 1) = 1, S₂(n, 2) = 2ⁿ⁻¹ − 1) leaves
  **a(n) = (A000629(n − 1) − 2ⁿ⁻¹)/2**, for n = 1 too: (1 − 1)/2 = 0.
  For n ≥ 2 this is A000670(n − 1) − 2ⁿ⁻² (Goebel).
- The loop is the [A000629](../../A000xxx/A000629/) program (its `t` runs
  through A000629(0), A000629(1), …), with p = 2ⁿ⁻¹ doubling alongside;
  t − p is even, so `t-p>>1` halves it exactly.

**Notes**

- Using `len(r)` for the power, `print(t*2-2**len(r)>>2)`, is one byte
  longer.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 100 terms (n = 1 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002051), CC BY-SA 4.0.
