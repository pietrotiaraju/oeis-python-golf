# A000147

> Number of trees of diameter 5.
> — [OEIS A000147](https://oeis.org/A000147)

Offset 1: 0, 0, 0, 0, 0, 1, 2, 7, 14, 32, 58, 110, 187, 322, 519, 839, …

A tree of odd diameter has a central edge. Cutting it leaves two rooted
trees, and for diameter 5 both have height exactly 2; joining the roots of
any two such trees gives back a tree of diameter 5, and the central edge
makes the pair unordered and unique. A rooted tree of height at most 2 with
j + 1 nodes is a root whose branches are stars, so it is a partition of j;
height exactly 2 rules out the partition into ones. With c(j) = p(j) − 1
such trees, c(0) = c(1) = 0, and N = n − 2:

**a(n) = (Σ_j c(j)·c(N − j) + [N even]·c(N/2)) / 2**,

the number of unordered pairs (the formula on the OEIS page, by Franklin T.
Adams-Watters).

### Python 3 — 129 bytes

```python
*a,n=0,1,0
while[print(sum(~-a[i]*(a[~i]-(n!=2*i+3))for i in range(n,-1))//2)]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- The partitions come from the [A000041](../A000041/) program with the 0 in
  front from [A000094](../A000094/): `a` = [0, p(0), …, p(m)] and n = −m
  when a line is printed. That line is a(m + 1), so N = m − 1.
- For i from −m to −2, `a[i]` is p(m + 1 + i) and `a[~i]` = `a[-1-i]` is
  p(−2 − i): the two indices add up to m − 1 = N. They cover j = 1 … N, and
  j = 0 is not needed since c(0) = 0. `range(n,-1)` stops before i = −1,
  whose partner `a[0]` is the padding 0.
- `~-x` is x − 1, so each term is c(j)·(c(N − j) + δ), where δ = 1 when
  both indices are the same entry: m + 1 + i = −2 − i, that is n = 2i + 3.
  `a[~i]-(n!=2*i+3)` is p − 1 + δ in one step. The sum is twice a(n) and
  `//2` halves it exactly.
- For m = 0 and m = 1 the range is empty, which prints a(1) = a(2) = 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (1000 terms) prints in about 1.5 s, and about 6 800
  terms print in 60 s. The bar is the whole b-file in 60 s. a(n) has about
  2.2·√n digits, so Python's 4300-digit int-to-str limit is reached only near
  n ≈ 4·10⁶.
- `a=[n:=0,1]` in the first line is the same length. Without the 0 in front
  the sum gives a(m + 2) over `range(n,0)`, but the missing first term costs
  a `print(0)`, 6 bytes more in all. The middle term outside the sum,
  `+n%2*~-a[n//2-1]`, is 4 bytes longer than `-(n!=2*i+3)` inside it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000147), CC BY-SA 4.0.
