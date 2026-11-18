# A001943

> Expansion of reciprocal of theta series of E_8 lattice.
> — [OEIS A001943](https://oeis.org/A001943)

Offset 0: 1, -240, 55440, -12793920, 2952385680, -681306078240, …

### Python 3 — 83 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=240*sum(d**3*sum(a[d::d])for d in range(n,0)),
```

**How it works**

- **The series.** The theta series of the E₈ lattice, counting vectors by
  norm 2k, is the Eisenstein series E₄(q) = 1 + 240 Σ_{k≥1} σ₃(k)·q^k
  ([A004009](https://oeis.org/A004009)), and a(n) is the coefficient of
  q^n in 1/E₄. Since E₄ starts with 1, a(0) = 1 and
  a(m) = −240 Σ_{k=1..m} σ₃(k)·a(m−k) for m ≥ 1.
- **Divisor sums for free.** Writing σ₃(k) = Σ_{d|k} d³ and grouping by d,
  Σ_k σ₃(k)·a(m−k) = Σ_{d≥1} d³·(a(m−d) + a(m−2d) + …), so no divisors
  are ever listed.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d < 0 the slice `a[d::d]` is
  a(m−|d|), a(m−2|d|), …, and `d**3` is −|d|³, which supplies the minus
  sign of the recurrence: no division at all.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The terms
  grow like e^(π√3·n) (|a(n)| has about 2.36·n digits), so printing stops
  with Python's 4300-digit int-to-str limit near n = 1820; the b-file ends
  at n = 422.
- The bar is the whole b-file (423 terms, n = 0 to 422) in 60 s, which
  takes about 2 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001943), CC BY-SA 4.0.
