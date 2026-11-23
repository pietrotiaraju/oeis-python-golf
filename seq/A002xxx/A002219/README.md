# A002219

> a(n) is the number of partitions of 2n that can be obtained by adding together two (not necessarily distinct) partitions of n.
> — [OEIS A002219](https://oeis.org/A002219)

Offset 1: 1, 3, 6, 14, 25, 53, 89, 167, 278, 480, 760, 1273, …

### Python 3 — 134 bytes

```python
p=lambda n,m=1:{B**n}|{B**k+q for k in range(m,n)for q in p(n-k,k)}
B=0
while 1:B+=3;E=p(B//3);print(len({a+b for a in E for b in E}))
```

**How it works**

- **Adding partitions** means joining them as multisets of parts: the
  entry's example adds the seven partitions of 5 in pairs and gets
  partitions of 10 such as 1¹⁰ = 1⁵ + 1⁵ and 1⁸2 = 1⁵ + 1³2. So a(n) is
  the number of distinct multisets λ₁ ∪ … ∪ λ₂ with every λᵢ a partition
  of n (two of them, repeats allowed). The program counts exactly this
  set, for every n.
- **Codes.** A partition is stored as the integer Σ B^part over its parts,
  so its digit j in base B is the multiplicity of the part j. The union of
  two partitions of n then has code equal to the sum of their codes: each
  digit is a multiplicity of the union, at most 2n (all parts 1), and B
  is larger than 2n, so no digit carries. Base-B digits are unique, so two
  unions are the same multiset exactly when their codes are equal, and
  counting distinct sums counts distinct unions.
- **Partitions** (`p(n,m)`): the code Bⁿ of the one-part partition n,
  together with Bᵏ + (a code from `p(n-k,k)`) for every first part k with
  m ≤ k < n. By induction on n it contains every partition of n whose
  parts are all ≥ m (take k = its smallest part, the rest has parts ≥ k),
  and everything in it is a partition of n (some with a last part below
  k, which is harmless: it is still a partition of n, and the set
  removes repeats). With m = 1 it is exactly the set of partitions of n.
- **Sums.** `B` runs through 3, 6, 9, …, so `B//3` is n and the base is
  B = 3n > 2n. `E` holds the codes of the partitions of n and
  `{a+b for a in E for b in E}` the codes of all unions of two of them;
  its size is a(n).

**Notes**

- Exact integers, no search bound: right for every n. The comprehension makes p(n)² set insertions, and
  the final set holds a(n) codes, so time and memory grow fast. The bar is
  26 terms in 30 s; the 26th arrives in a few seconds here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 134 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002219), CC BY-SA 4.0.
