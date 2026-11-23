# A002221

> a(n) is the number of partitions of 4n that can be obtained by adding together four (not necessarily distinct) partitions of n.
> — [OEIS A002221](https://oeis.org/A002221)

Offset 1: 1, 5, 15, 55, 140, 448, 1022, 2710, 6048, 14114, 28831, 64091, …

### Python 3 — 151 bytes

```python
p=lambda n,m=1:{B**n}|{B**k+q for k in range(m,n)for q in p(n-k,k)}
B=0
while 1:B+=5;E=S=p(B//5);exec("S={s+e for s in S for e in E};"*3);print(len(S))
```

**How it works**

- **Adding partitions** means joining them as multisets of parts: the
  entry's example adds the seven partitions of 5 in pairs and gets
  partitions of 10 such as 1¹⁰ = 1⁵ + 1⁵ and 1⁸2 = 1⁵ + 1³2. So a(n) is
  the number of distinct multisets λ₁ ∪ … ∪ λ₄ with every λᵢ a partition
  of n (four of them, repeats allowed). The program counts exactly this
  set, for every n.
- **Codes.** A partition is stored as the integer Σ B^part over its parts,
  so its digit j in base B is the multiplicity of the part j. The union of
  four partitions of n then has code equal to the sum of their codes: each
  digit is a multiplicity of the union, at most 4n (all parts 1), and B
  is larger than 4n, so no digit carries. Base-B digits are unique, so two
  unions are the same multiset exactly when their codes are equal, and
  counting distinct sums counts distinct unions.
- **Partitions** (`p(n,m)`): the code Bⁿ of the one-part partition n,
  together with Bᵏ + (a code from `p(n-k,k)`) for every first part k with
  m ≤ k < n. By induction on n it contains every partition of n whose
  parts are all ≥ m (take k = its smallest part, the rest has parts ≥ k),
  and everything in it is a partition of n (some with a last part below
  k, which is harmless: it is still a partition of n, and the set
  removes repeats). With m = 1 it is exactly the set of partitions of n.
- **Sums.** `B` runs through 5, 10, 15, …, so `B//5` is n and the base
  is B = 5n > 4n. `E` holds the codes of the partitions of n. Starting
  from `S=E`, each of the 3 passes of the `exec` string replaces `S` by
  the set of sums s + e (s in `S`, e in `E`), so afterwards `S` holds
  the codes of all unions of four partitions of n, each union once (the
  set removes repeats after every pass, which keeps the work at
  |S|·|E| per pass instead of p(n)⁴). Its size is a(n).

**Notes**

- Exact integers, no search bound: right for every n. A pass costs p(n) set
  insertions per code already in `S`, and
  the final set holds a(n) codes, so time and memory grow fast. The bar is
  14 terms in 20 s; the 14th arrives in a few seconds here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 151 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002221), CC BY-SA 4.0.
