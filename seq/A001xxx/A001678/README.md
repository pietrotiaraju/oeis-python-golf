# A001678

> Number of series-reduced planted trees with n nodes.
> — [OEIS A001678](https://oeis.org/A001678)

Offset 0: 0, 0, 1, 0, 1, 1, 2, 3, 6, 10, 19, 35, 67, 127, 248, 482, …

### Python 3 — 108 bytes

```python
A=[0,0,1];m=-1
for x in A:print(x);A+=sum(d*A[1-d]*sum(A[d::d]+A[d-1::d])for d in range(m,0))//m-A[-1],;m-=1
```

**How it works**

- The entry's g.f. (Harary and Palmer, eq. 3.3.8):
  A(x) = x²/((1 + x)·Π_{k≥1} (1 − x^k)^a(k+1)). With b(k) = a(k+1)
  (lone-child-avoiding rooted trees with k nodes, entry comment) and
  B(x) = A(x)/x = Σ b(k)x^k this reads
  **(1 + x)·B(x)/x = E(x) = Π_k (1 − x^k)^(−b(k))**: a root with any
  multiset of subtrees, minus the one-child case.
- So e(M) = [x^M]E = b(M+1) + b(M) = a(M+2) + a(M+1), and E is the Euler
  transform of b:
  **M·e(M) = Σ_{k=1..M} k·b(k)·Σ_{i≥1} e(M − ik)**. Each step finds
  e(M) and then a(M+2) = e(M) − a(M+1).
- `A` holds a(0), …, a(M+1). Each e(M − ik) is a(M+2−ik) + a(M+1−ik),
  so the inner sum is the two slices `A[-k::-k]` and `A[-k-1::-k]`
  joined into one list. They run down to index 0; the extra entries they
  pick up are a(0) and a(1), both 0.
- The counter runs negative, m = −M, and d = −k: then `A[d::d]` and
  `A[d-1::d]` are those slices, `A[1-d]` is a(k+1) = b(k),
  `range(m,0)` is k = M, …, 1, and dividing the negated sum by m = −M
  gives e(M). That is 3 bytes under `range(1,m+1)` with `A[-d::-d]`.
- `for x in A:` walks the list while it grows, one append per printed
  term, so the program needs no index: the list starts with a(0), a(1),
  a(2) and always stays ahead of the printing.

**Notes**

- Exact integer arithmetic, so the program is right for every n: the sum
  is −M·e(M), so `//m` is exact.
- The whole b-file (1001 terms, up to a(1000)) takes about 1.3 reference
  seconds; the bar is the whole b-file in 60 s.
- a(n) grows like 2.19ⁿ, so the 4300-digit int-to-str limit is reached
  only near n = 12600.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001678), CC BY-SA 4.0.
