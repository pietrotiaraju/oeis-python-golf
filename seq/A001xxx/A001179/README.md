# A001179

> Leonardo logarithm of n.
> — [OEIS A001179](https://oeis.org/A001179)

Offset 1: 0, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, …

### Python 3 — 118 bytes

```python
n=0
while 1:
 k=n=n+1;m=c=0
 while k-m:
  m=k;a=b=k=1
  while a%m|~-b%m:a,b=b,a+b;k+=1
 while k>4:k//=5;c+=1
 print(c)
```

Uses the Pisano period loop of [A001175](../A001175/) and the chain of
[A001178](../A001178/).

**How it works**

- Iterating the Pisano period map π from n reaches a fixed point: 1 when
  n = 1, and otherwise 24·5^(j−1) for some j ≥ 1 (Fulton and Morris, Acta
  Arith. 16, 1969). The Leonardo logarithm is that j, and 0 for n = 1; this is
  the OEIS program, which divides the fixed point by 24 and then counts
  divisions by 5.
- The first part is the chain of [A001178](../A001178/): `while k-m:` sets m
  to the last period and computes k = π(m) by stepping exact Fibonacci numbers
  until F_k ≡ 0 and F_{k+1} ≡ 1 (mod m), and it stops when π(m) = m. So k
  ends as the fixed point.
- In base 5, 24·5^(j−1) is `44` followed by j − 1 zeros: j + 1 digits. So j
  is the number of base-5 digits minus one, which `while k>4:k//=5;c+=1`
  counts without dividing by 24; for the fixed point 1 it gives 0.

**Notes**

- Exact for every n.
- About 4700 terms in 25 s on the PC it was written on (the cost is the same as
  in [A001178](../A001178/)). The b-file has 10000; the bar is 4000 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001179), CC BY-SA 4.0.
