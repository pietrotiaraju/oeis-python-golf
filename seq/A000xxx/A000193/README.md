# A000193

> Nearest integer to log n.
> — [OEIS A000193](https://oeis.org/A000193)

Offset 1: 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, …

### Python 3 — 97 bytes

```python
n=m=1
while 1:
 N=F=d=1
 while-N%F<m**d:N=N*d+m**d;F*=d;d+=1
 m+=n*n*F>N;n+=n*n*F<=N!=print(m//2)
```

**How it works**

- round(ln n) = ⌊(x + 1)/2⌋ with x = 2 ln n = ln n². For n ≥ 2, x is never
  an integer (e^m is irrational for m ≥ 1), so if m is the least integer
  with n² < e^m, then m = ⌊x⌋ + 1 and a(n) = ⌊m/2⌋ = `m//2`. For n = 1
  the least m ≥ 1 is m = 1, which gives 0.
- The inner loop is the floor(e^m) loop of [A000149](../A000149/): N/F is
  the partial sum of Σ m^k/k! with F = (d − 1)!, and it stops only once
  the gap from N/F up to the next integer exceeds the tail of the series,
  so N//F = ⌊e^m⌋ exactly. Since e^m is not an integer,
  n² < e^m ⇔ n² ≤ ⌊e^m⌋ ⇔ n²·F ≤ N.
- Each pass handles one pair (n, m). If n² > e^m, `m+=n*n*F>N` moves on to
  the next m (the second test then fails too, so nothing is printed). If
  not, the chained comparison `n*n*F<=N!=print(m//2)` calls `print` only
  because the first link is true; `N!=None` is then true and n moves on.
  m never has to go back down, since n only grows.
- This is 2 bytes under the two-loop form that computes ⌊e^m⌋ once per m
  and prints `while n*n*F<=N:print(m//2);n+=1` before `m+=1` (99 bytes,
  about 11× faster).

**Notes**

- Exact integer arithmetic, correct for every n; the only fact used is
  that e^m is irrational for m ≥ 1, which also makes the inner loop end.
  The series is recomputed for every term, about 3m steps for
  n ≈ e^(m/2). The whole b-file (10000 terms) prints in under 2 seconds,
  and about 320000 terms come out in 40 s. The bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000193), CC BY-SA 4.0.
