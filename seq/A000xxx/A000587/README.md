# A000587

> Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 - exp(x)).
> — [OEIS A000587](https://oeis.org/A000587)

Offset 0: 1, -1, 0, 1, 1, -2, -9, -9, 50, 267, …

### Python 3 — 72 bytes

```python
L=[];t=-1
while[print(-t)]:t=1;L=[t]+[t:=len(L)*L.pop(0)-t for _ in L*1]
```

**How it works**

- The exponential generating function exp(1−exp(x)) is the
  second-kind Stirling transform of c(j)=(−1)^j. Thus
  a(n)=ΣⱼS(n,j)(−1)^j, with a(0)=1.
- For a Stirling transform, define T(0,k)=c(k) and
  T(i+1,k)=kT(i,k)+T(i,k+1). Then T(n,0)=a(n).
  Normalize U(i,k)=(−1)^kT(i,k); its initial row is all ones and

  **U(i+1,k)=kU(i,k)−U(i,k+1)**.

- L holds the antidiagonal U(0,n),U(1,n−1),…,U(n−1,1).
  Begin its successor with 1. For each following entry, multiply
  the old entry by its column k and subtract the preceding new
  entry t. `len(L)` gives k before `pop(0)` removes the old value;
  the copy `L*1` fixes the number of updates.
- For n>0, the k=0 recurrence gives a(n)=U(n,0)=−U(n−1,1),
  so print −t. Initially t=−1 supplies the separate a(0)=1;
  thereafter each antidiagonal supplies the next signed value.

**Notes**

- Exact signed integer additions and multiplications account for all
  cancellations. No numerical exponential or binomial table is used.
- One growing antidiagonal is retained. Python's integer-to-string
  conversion limit can eventually apply.
- The reference file has 596 terms. The unchanged verification
  bar is the complete file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 98 | first entry |
| 2026-11-06 | Python 3 | 72 | use a normalized signed Stirling antidiagonal |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000587), CC BY-SA 4.0.
