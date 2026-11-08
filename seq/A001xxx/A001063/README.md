# A001063

> E.g.f. satisfies A'(x) = A(x/(1-x)).
> — [OEIS A001063](https://oeis.org/A001063)

Offset 0: 1, 1, 1, 3, 15, 111, 1131, 15081, 253473, 5220225, 128886921, …

### Python 3 — 63 bytes

```python
R=[s:=1];d=0
while[print(R[0])]:R=[s:=s+d*x for x in[0]+R];d+=1
```

**Why it works**

Instead of the Lah-number sum a(n+1) = Σ L(n,k)·a(k) in the entry, the
program uses a family of series that needs only a running sum:

- Let g(x) = x/(1−x) and U_j(x) = A^(j)(g(x))/(1−x)^j, with
  u_j(n) = n!·[x^n]U_j. Since g′ = 1/(1−x)², the chain rule gives
  (1−x)U_j′ = U_(j+1) + j·U_j, that is

  **u_j(n+1) = u_(j+1)(n) + (n+j)·u_j(n).**

- u_j(0) = A^(j)(0) = a(j), and U_0 = A(g) = A′, so u_0(n) = a(n+1).
- On the antidiagonal j + n = d, the multiplier n + j is the constant
  d − 1. Write R_d[i] = u_(d−i)(i) for i = 0..d. Then R_d[0] = a(d),
  R_d[i] = R_d[i−1] + (d−1)·R_(d−1)[i−1], and R_d[d] = u_0(d) = a(d+1),
  which is R_(d+1)[0]. Every value is determined by earlier ones, so this
  computes the sequence exactly.

**How it works**

- `R` is R_d and `d` its index; the new row is the running sum
  `s:=s+d*x` over `[0]+R` (the coefficient for row d + 1 is d).
- `s` ends each pass at the last entry, a(d+1), which is exactly the first
  entry of the next row, so it never needs resetting; the leading `0`
  makes the first new entry s itself.
- The program prints `R[0]` = a(d).

**Notes**

- Exact integer arithmetic, correct for every n by the identity above.
- O(n) small multiplications per term: over 1000 terms in 10 s; the bar is
  the whole b-file (301 terms) in 60 s. The direct Lah sum with
  `comb`/`perm` is about 107 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001063), CC BY-SA 4.0.
