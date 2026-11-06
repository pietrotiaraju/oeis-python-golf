# A000559

> Generalized Stirling numbers of second kind.
> — [OEIS A000559](https://oeis.org/A000559)

Offset 3: 1, 12, 110, 945, 8092, 70756, 638423, 5971350, 57996774, 585092607, …

### Python 3 — 98 bytes

```python
*L,n=0,0,3
while 1:
 t=(3**n+3)//6-2**~-n;L=[t]+[t:=t+len(L)*L.pop(0)for _ in L*1]
 print(t)
 n+=1
```

**How it works**

- OEIS gives a(n)=Σⱼ S(n,j)S(j,3). The closed formula
  `(3**n+3)//6-2**~-n` supplies S(n,3) for n≥1. Since 3^n+3
  is divisible by 6, this equals (3^n−3·2^n+3)/6; `~-n` means n−1.
- For any input c(j), define T(0,j)=c(j) and
  T(i+1,j)=jT(i,j)+T(i,j+1). Then T(n,0)=Σⱼ S(n,j)c(j), the second-kind
  Stirling transform, by induction with the Stirling recurrence.
- `L` holds an antidiagonal from T(0,n) through T(n−1,1)=T(n,0). The next begins
  with the new input t; each following value adds the preceding new
  value to the old entry times its descending column index.
- `len(L)` is evaluated before `pop(0)`, and `L*1` fixes the iteration
  count while the old list is consumed. Printing begins at n=3.

- The input coefficients S(1,3), …, S(2,3) vanish.
  Their first 2 antidiagonal entries are therefore all zero.
  Seed L with those zeros and start at n=3, avoiding both the
  zero-only updates and a repeated output-offset test.

**Notes**

- The transform uses exact integers and O(n) storage. The input formula
  is evaluated only for positive n, where the stated closed form applies.
- The reference file contains 20 terms from the published OEIS entry; the verification
  bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 104 | first entry |
| 2026-11-06 | Python 3 | 98 | seed the zero antidiagonal and begin at the output offset |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000559), CC BY-SA 4.0.
