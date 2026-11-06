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

Write b_h(m) for rooted trees on m+1 nodes of height at most h.
Removing the root leaves a multiset of trees of height at most h-1,
so b_h is the Euler transform with weights b_(h-1)(k-1); b_1(m)=1.
The list interleaves b_8, b_7, …, b_2, initialized to 1 at m=0.
The Euler-transform recurrence m*b_h(m)=sum(k*b_(h-1)(k-1)*
sum(b_h(m-j*k),j>=1),k=1..m) supplies each new entry.
Negative indices d=-7*k and slices L[d::d] select the earlier
entries of the current layer, while the indexed weight selects
the next layer, or the constant 1 for the last layer. The first
two entries of each row differ by the number of height exactly 8.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 200 terms in 60 s; the official b-file contains 200 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000429), CC BY-SA 4.0.
