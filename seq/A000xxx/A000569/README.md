# A000569

> Number of graphical partitions of 2n.
> — [OEIS A000569](https://oeis.org/A000569)

Offset 1: 1, 2, 5, 9, 17, 31, 54, 90, 151, 244, …

### Python 3 — 249 bytes

```python
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def f(p):
 p=sorted(p,reverse=True)
 return not p or p[0]<len(p)and f([x-(i<p[0])for i,x in enumerate(p[1:])if x-(i<p[0])])
n=0
while 1:n+=1;print(sum(map(f,P(2*n))))
```

**How it works**

- Generate every partition of 2n in nondecreasing order, with positive
  parts only. Such a partition is a candidate degree sequence with no
  isolated vertices.
- The Havel–Hakimi criterion removes the largest degree d and subtracts
  one from the next d largest degrees. A sequence is graphical exactly
  when this process reaches the empty sequence without a negative entry.
- `f` sorts before each reduction. If the largest degree is at least the
  current vertex count it rejects immediately; zero degrees are removed
  after the subtraction. Each accepted partition is counted once.

**Notes**

- This follows a necessary-and-sufficient graphicality criterion, with
  exact integer degrees and no probabilistic graph construction.
- Integer partition enumeration grows rapidly; the bar is 12 terms.
- The reference file contains 860 terms from the OEIS b-file; the verification
  bar is 12 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 249 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000569), CC BY-SA 4.0.
