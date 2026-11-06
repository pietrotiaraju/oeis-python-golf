# A000506

> One half of the number of permutations of [n] such that the differences have 5 runs with the same signs.
> — [OEIS A000506](https://oeis.org/A000506)

Offset 6: 61, 841, 7311, 51663, 325446, 1910706, 10715506, 58258210, 309958755, 1623847695, …

### Python 3 — 116 bytes

```python
n=2;A=[0,1,0,0,0,0]
while 1:
 n+=1;A=[0]+[k*A[k]+2*A[k-1]+(n-k)*A[k-2]*(k>1)for k in range(1,6)]
 if n>5:print(A[5])
```

**How it works**

- Let p(n,k) be half the number of permutations of [n] with k alternating
  runs (maximal runs of successive differences of one sign). Inserting
  the new largest element gives
  p(n,k)=k*p(n−1,k)+2*p(n−1,k−1)+(n−k)*p(n−1,k−2).
- `A` stores columns k=0,…,5. The initial row n=2 is [0,1,0,0,0,0]:
  the two permutations both have one run, and the sequence divides by 2.
- Every new row is computed from the old one in a list comprehension.
  Multiplying the k−2 term by `k>1` suppresses the negative-index case.
  Printing begins at n=6, the OEIS offset.

**Notes**

- Only six counters are stored, so the computation is linear in the
  number of terms apart from integer sizes.
- The recurrence continues indefinitely; the short reference table is
  not embedded in the program.
- The reference file contains 18 terms from the OEIS b-file; the verification
  bar is 18 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000506), CC BY-SA 4.0.
