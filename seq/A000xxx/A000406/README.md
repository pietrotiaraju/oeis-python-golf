# A000406

> Coefficients of iterated exponentials.
> — [OEIS A000406](https://oeis.org/A000406)

Offset 1: 1, 6, 57, 741, 12244, 245755, 5809875, 158198200, 4877852505, 168055077875, …

### Python 3 — 85 bytes

```python
Q=[[t:=1]]*6
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
```

**How it works**

- Put H(x)=−log(1−x). The e.g.f. is the sixfold composition
  H(H(H(H(H(H(x)))))). Substituting H(x) in a series takes its
  unsigned first-kind Stirling transform:
  b(n)=Σⱼ |s(n,j)|·c(j). Start with the coefficients of x,
  c(0)=0, c(1)=1, and c(n)=0 for n>1.
- For one transform, T(i,k)=Σⱼ |s(i,j)|·c(j+k) satisfies
  T(i+1,k)=i·T(i,k)+T(i,k+1), with T(0,k)=c(k).
  Its left edge T(n,0) is the transformed sequence. Unlike the
  second-kind triangle of [A000405](../A000405/), the weight is i.
- A list L holds [T(0,n), T(1,n−1), …, T(n,0)]. The next
  antidiagonal starts with the new input t; each following entry is
  the preceding new entry plus i·L[i]. That is the walrus update
  `t:=t+i*x` inside `enumerate(L)`.
- The last t of one level becomes the first entry needed by the next
  level. Six lists therefore apply six transforms without building
  the full Stirling triangle.
- Initially `t=1` supplies c(1). After each output `t=0` supplies
  the later zero coefficients of x. Assigning Q in the condition
  computes the next row before printing, so output starts at n=1.

**Notes**

- `Q=[[t:=1]]*6` shares its initial list safely: this algorithm only
  reads old lists and creates new ones. Its initial first entry would
  normally be c(0)=0, but it is multiplied by i=0 and never contributes,
  so using `[1]` saves a separate initialization.
- The outer list is always nonempty; using it as the `while` condition
  both stores the new antidiagonals and keeps the loop running.
- This is [A000310](../A000310/) with six levels instead of four.
  Each round handles six lists whose lengths grow by one, using exact
  integer arithmetic and linear storage in the number of terms.
- The rapidly growing coefficients eventually meet Python 3.11+'s
  default 4300-digit integer-to-string limit, an interpreter limit.
- The b-file has 100 terms (indices 1 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000406), CC BY-SA 4.0.
