# A000418

> Number of n-node rooted trees of height 7.
> — [OEIS A000418](https://oeis.org/A000418)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 1, 7, 34, …

### Python 3 — 129 bytes

```python
L=[1]*6;n=0
while[print(L[-6]-L[-5])]:
 n-=6
 for h in range(6):L+=sum(d*L[(-d-5+h)*(h<5)]*sum(L[d::d])for d in range(n,0,6))//n,
```

**How it works**

Write b_h(m) for rooted trees on m+1 nodes of height at most h.
Removing the root leaves a multiset of trees of height at most h-1,
so b_h is the Euler transform with weights b_(h-1)(k-1); b_1(m)=1.
The list interleaves b_7, b_6, …, b_2, initialized to 1 at m=0.
The Euler-transform recurrence m*b_h(m)=sum(k*b_(h-1)(k-1)*
sum(b_h(m-j*k),j>=1),k=1..m) supplies each new entry.
Negative indices d=-6*k and slices L[d::d] select the earlier
entries of the current layer, while the indexed weight selects
the next layer, or the constant 1 for the last layer. The first
two entries of each row differ by the number of height exactly 7.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 200 terms in 60 s; the official b-file contains 200 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000418), CC BY-SA 4.0.
