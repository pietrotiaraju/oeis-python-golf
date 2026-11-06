# A000429

> Number of n-node rooted trees of height 8.
> — [OEIS A000429](https://oeis.org/A000429)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 0, 1, 8, …

### Python 3 — 129 bytes

```python
L=[1]*7;n=0
while[print(L[-7]-L[-6])]:
 n-=7
 for h in range(7):L+=sum(d*L[(-d-6+h)*(h<6)]*sum(L[d::d])for d in range(n,0,7))//n,
```

**How it works**

- Let b_h(m) count rooted, unlabeled trees with m+1 nodes and height at
  most h, measured in edges. Removing the root leaves a multiset of
  subtrees of height at most h−1. Its generating function is
  ∏ₖ≥₁ (1−xᵏ)^(−b_(h−1)(k−1)), so

  m·b_h(m) = Σₖ₌₁ᵐ k·b_(h−1)(k−1)·Σⱼ≥₁ b_h(m−jk),
  with terms having negative indices omitted.

- One list interleaves the layers in rows:
  [b_8(0), b_7(0), …, b_2(0),
  b_8(1), b_7(1), …, b_2(1), …].
  Each initial entry is 1, the one-node tree. The missing bottom layer
  is b_1(m)=1, since there is exactly one star of each size.
- On computing row m, the variable `n` is −7m and the generator
  variable `d` is −7k. During pass h (a zero-based list column),
  `L[d::d]` selects b_(8−h)(m−k), b_(8−h)(m−2k), … .
  Already appended entries of the row shift the end of the list to
  the correct column for that pass.
- `-d-6+h` is the positive index 7(k−1)+h+1, which
  holds the weight from the next layer. At the last column,
  `(h<6)` makes that index 0 instead, selecting the constant
  1 of b_1. The factors −7 in d and n cancel in the quotient.
- `L[-7]-L[-6]` subtracts height at most 7
  from height at most 8, giving height exactly 8.
  Row m is printed as a(m+1), including the initial zeros.

**Notes**

- Exact integer arithmetic and exact divisions, from the multiset
  generating functions. A chain needs 9 nodes to have height
  8, explaining the first nonzero term a(9)=1.
- The list stores 7 entries per tree size. A negative-step
  slice ends at the start of the list, so no explicit bound on j is
  needed in the inner sum.
- [A000418](../A000418/) uses the same interleaving with one
  fewer layer. Keeping a separate list
  for each height would make the weight selection easier to read,
  but require more indexing code.
- The b-file has 200 terms (indices 1 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000429), CC BY-SA 4.0.
