# A000587

> Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 - exp(x)).
> — [OEIS A000587](https://oeis.org/A000587)

Offset 0: 1, -1, 0, 1, 1, -2, -9, -9, 50, 267, …

### Python 3 — 55 bytes

```python
r=[];t=1
while[print(t)]:r=[t]+[t:=t+x for x in r];t=-t
```

**How it works**

- **A recurrence for a(n).** With E(x) = exp(1 − eˣ) we have
  E′(x) = −eˣ·E(x), and comparing coefficients of xⁿ/n! gives
  a(n+1) = −Σ_{k=0}^{n} C(n, k)·a(k).
- **The triangle.** Put T(n, 0) = a(n) and
  T(n, k) = T(n, k−1) + T(n−1, k−1) for 1 ≤ k ≤ n (the Bell triangle,
  A011971, with a(n) in place of the Bell numbers). By induction on k,
  T(n, k) = Σ_{i=0}^{k} C(k, i)·a(n−k+i): the two terms of the recurrence give
  C(k−1, i−1) and C(k−1, i), which add up to C(k, i). So
  T(n, n) = Σ_i C(n, i)·a(i) = −a(n+1): each row starts with minus the last
  entry of the row before.
- **The loop.** `r` is row n−1 and `t` is a(n) when `print(t)` runs. The new
  row is `[t]` followed by running sums: `t:=t+x` adds T(n−1, k−1) to
  T(n, k−1), so the walrus chain leaves t = T(n, n), and `t=-t` makes it
  a(n+1). The comprehension reads the old `r`, which is only replaced after
  it ends.
- `r=[];t=1` starts with an empty row −1 and a(0) = 1.

**Notes**

- Other versions that print the same terms:
  - printing −t and negating at the start of the row,
    `r=[];t=-1` / `while[print(-t)]:r=[t:=-t]+[t:=t+x for x in r]`: 56 bytes;
  - the first version of this page, an antidiagonal of the Stirling-transform
    array with `pop(0)`: 72 bytes;
  - summing the signed Stirling rows (−1)^k·S(n, k),
    `R=[1]` / `while[print(sum(R))]:R=[k*a-b for k,(a,b)in enumerate(zip(R+[0],[0]+R))]`:
    78 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 596 terms (up to a(595)) and all of them print in about
  0.2 s; the bar is the whole b-file in 60 s.
- a(2020) is the first term with more than 4300 digits, so after about 2.5 s
  the int-to-str limit stops the program; a(0)–a(2019) are printed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 98 | first entry |
| 2026-11-06 | Python 3 | 72 | use a normalized signed Stirling antidiagonal |
| 2026-11-07 | Python 3 | 55 | Bell-type triangle whose rows start with minus the last entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000587), CC BY-SA 4.0.
