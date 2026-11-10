# A001469

> Genocchi numbers (of first kind); unsigned coefficients give expansion of x*tan(x/2).
> — [OEIS A001469](https://oeis.org/A001469)

Offset 1: -1, 1, -3, 17, -155, 2073, -38227, 929569, -28820619, 1109652905, -51943281731, …

### Python 3 — 70 bytes

```python
r=[-1,-1]
while 1:r=[t:=-sum(r)//2]+[t:=t+x for x in r];t and print(t)
```

**How it works**

- Let G_m be the Genocchi numbers, 2x/(eˣ + 1) = Σ G_m·x^m/m!. The OEIS
  e.g.f. 2x/(1 + eˣ) = x + Σ_{n≥1} a(n)·x^(2n)/(2n)! says
  **a(n) = G_{2n}**, G_0 = 0, G_1 = 1 and G_m = 0 for odd m ≥ 3.
- Multiplying by eˣ + 1 gives (eˣ + 1)·Σ G_m·x^m/m! = 2x, that is
  Σ_k C(m,k)·G_k + G_m = 0 for every m ≥ 2: the binomial transform
  BT(m) = Σ_k C(m,k)·G_k equals −G_m.
- Euler–Seidel table: A(0,j) = G_j and A(i,j) = A(i−1,j) + A(i−1,j+1),
  so A(i,0) = Σ_k C(i,k)·G_k. The program keeps one antidiagonal
  i + j = m, from A(0,m) = G_m to A(m,0) = BT(m). Since
  A(i,m−i) = A(i−1,m−i+1) + A(i−1,m−i), the new antidiagonal is G_m
  followed by the running sums of the old one, and its last entry is
  BT(m) = G_m + sum(old). With BT(m) = −G_m this gives
  **G_m = −sum(old)/2**, an exact halving.
- The rows are kept negated (every step is linear, so negating the start
  negates everything): the first entry `-sum(r)//2` is −G_m and the last,
  which the walrus `t` holds after the comprehension, is −BT(m) = G_m.
  The start is the negated antidiagonal for m = 1, −[G_1, G_0 + G_1] =
  [−1, −1].
- For odd m ≥ 3 the row ends in G_m = 0 and `t and print(t)` skips it;
  for even m, G_m = 2(1 − 2^m)·B_m is never 0 (B_m ≠ 0 for even m),
  so exactly the terms a(1), a(2), … are printed.

**Notes**

- Seidel's triangle of [A000366](../A000366/), which also holds the
  unsigned Genocchi numbers 1, 1, 3, 17, … at the other end of its rows,
  with the sign flipped at every row, `r=[-1]` / `while[print(r[0])]:s=sum(r);t=0;r=[t:=t-(s:=s-x)-x for x in[0]+r]`,
  prints a term per row but is 72 bytes.
- Exact integer arithmetic, so the program is right for every n. Row m
  has m+1 entries, so the first N terms take about 2N² big-integer
  additions; the whole b-file (275 terms) prints in about 0.1 s, and that
  is the bar. The 4300-digit int-to-str limit stops the program at
  a(921).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001469), CC BY-SA 4.0.
