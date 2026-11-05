# A000001

> Number of groups of order n.
> — [OEIS A000001](https://oeis.org/A000001)

Offset 0: 0, 1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, …

There is no formula for a(n) in general; the b-file values (n ≤ 2047) come
from group-theory software and its library of small groups. A short program
can only enumerate group tables, so it gets a handful of terms.

### Python 3 — 255 bytes

```python
from itertools import*
print(0);n=1;Q=product
while P:=[*permutations(R:=range(n))]:k=len(P)//n;print(sum(all(p[t[a][b]]==t[p[a]][p[b]]for a,b in Q(R,R))for t in Q(*batched(P,k))if all(t[t[a][b]][c]==t[a][t[b][c]]for a,b,c in Q(R,R,R))for p in P)//k);n+=1
```

**How it works**

- A table on {0, …, n−1} is a tuple of rows, row x being the permutation
  y ↦ x·y. For each x the program picks a row with x·0 = x, so 0 is a right
  identity. `permutations` comes out in lexicographic order, so the rows that
  start with x are exactly block x of `batched(P,k)` with k = (n−1)!
  (`batched` needs Python 3.12).
- Associativity is the only check left: in a finite associative table whose
  rows are permutations, every x has some y with x·y = 0, and a semigroup with
  a right identity and right inverses is a group.
- Counting up to isomorphism without canonical forms (Burnside): a group G
  shows up as (n−1)!/|Aut G| labelled tables with identity 0, so
  Σ |Aut T| over all tables T is a(n)·(n−1)!. The program counts the pairs
  (table, permutation p) where p is an automorphism, p(ab) = p(a)p(b), and
  divides by k.
- a(0) = 0 is printed up front, since `len(P)//n` would divide by zero.

**Limits**

- The search runs over ((n−1)!)ⁿ tables: 1296 for n = 4, 7 962 624 for n = 5
  (about 35 s), about 3·10¹² for n = 6. In practice the program prints
  a(0)…a(5), which is the bar for this sequence (6 terms in 120 s).
- Other shapes tried: a set of canonical relabelled tables (276 bytes); the
  row filter `[q for q in P if q[0]==x]` instead of `batched` (273); all
  (n!)ⁿ row tuples plus a column check (269, but it stops at a(4) and misses
  the bar). Folding both checks into one `all` over the triples (235 bytes)
  is correct but tests associativity once per pair (table, p): about
  9.6·10⁸ pairs for n = 5, so it stops at a(4) and misses the bar.

**Notes**

- The 256-byte version began its `while 1:` body with
  `P=[*permutations(…)];`. Naming the value in the loop condition is 1 byte
  shorter and keeps the loop going, because the list of permutations is
  never empty.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 260 | first entry |
| 2026-11-05 | Python 3 | 256 | `for a,b in Q(R,R)` (pietrotiaraju) |
| 2026-11-05 | Python 3 | 255 | value named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000001), CC BY-SA 4.0.
