# A000558

> Generalized Stirling numbers of second kind.
> — [OEIS A000558](https://oeis.org/A000558)

Offset 2: 1, 6, 32, 175, 1012, 6230, 40819, 283944, 2090424, 16235417, …

### Python 3 — 94 bytes

```python
L=[];n=1
while 1:
 t=2**~-n-1;L=[t]+[t:=t+len(L)*L.pop(0)for _ in L*1]
 if n>=2:print(t)
 n+=1
```

**How it works**

- OEIS gives a(n)=Σⱼ S(n,j)S(j,2). The closed formula
  `2**~-n-1` supplies S(n,2)=2^(n−1)−1 for n≥1; `~-n` means n−1.
- For any input c(j), define T(0,j)=c(j) and
  T(i+1,j)=jT(i,j)+T(i,j+1). Then T(n,0)=Σⱼ S(n,j)c(j), the second-kind
  Stirling transform, by induction with the Stirling recurrence.
- `L` holds an antidiagonal from T(0,n) through T(n−1,1)=T(n,0). The next begins
  with the new input t; each following value adds the preceding new
  value to the old entry times its descending column index.
- `len(L)` is evaluated before `pop(0)`, and `L*1` fixes the iteration
  count while the old list is consumed. Printing begins at n=2.

**Notes**

- The transform uses exact integers and O(n) storage. The input formula
  is evaluated only for positive n, where the stated closed form applies.
- The reference file contains 557 terms from the OEIS b-file; the verification
  bar is 557 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 94 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000558), CC BY-SA 4.0.
