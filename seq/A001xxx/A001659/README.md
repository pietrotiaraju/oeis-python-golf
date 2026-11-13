# A001659

> Expansion of bracket function.
> — [OEIS A001659](https://oeis.org/A001659)

Offset 1: 1, 1, −1, 2, −5, 13, −33, 80, −184, 402, −840, 1699, −3382, 6750, …

### Python 3 — 87 bytes

```python
d=[];m=0
while 1:m+=1;v=sum(m%-~k<1for k in range(m));d=[v:=v-x for x in[0]+d];print(v)
```

**How it works**

- The entry gives a(n) = Σ_{k=1..n} (−1)ⁿ⁻ᵏ·C(n−1, k−1)·τ(k), with τ the
  number of divisors (equivalently: the g.f. is Σ τ(k)·xᵏ/(1+x)ᵏ, or the
  inverse binomial transform of A006218). That sum is the (n−1)-th forward
  difference of τ at 1: a(n) = Δⁿ⁻¹τ(1). So the terms are the last entries
  of the rows of the difference table of τ(1), τ(2), τ(3), …, read along
  its diagonal.
- `d` holds the newest diagonal: after step m, d[i] = Δⁱτ(m − i) for
  i = 0 … m−1. A new value v = τ(m) gives the next diagonal by
  e₀ = τ(m), eᵢ = eᵢ₋₁ − d[i−1]: that is `[v:=v-x for x in[0]+d]`, where the
  walrus carries the running value from one entry to the next. Its last
  entry, left in `v`, is Δᵐ⁻¹τ(1) = a(m), which is printed.
- `sum(m%-~k<1for k in range(m))` counts the k = 1 … m that divide m
  (`-~k` is k + 1).

**Notes**

- Exact integer arithmetic, so every term is right. The whole b-file (1000
  terms) prints in well under a second; the bar is the whole b-file.
- Starting from v = 0 and writing `for x in[v-sum(…)]+d` saves the `v=…;`
  but costs the `v=0`: also 87 bytes. The double sum over the Lambert
  series, Σ_{i,j} (−1)^(n+ij)·C(n−1, ij−1), is about 105.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001659), CC BY-SA 4.0.
