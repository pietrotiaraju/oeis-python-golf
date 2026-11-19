# A002039

> Convolution inverse of A143348.
> — [OEIS A002039](https://oeis.org/A002039)

Offset 0: 1, 3, 5, 10, 25, 64, 160, 390, 940, 2270, 5515, 13440, 32735, 79610, 193480, 470306, …

### Python 3 — 91 bytes

```python
r=[s:=1,0]
while[print(s*r[-2])]:s=-s;r[-1:]=sum(d*sum(r[d::d])for d in range(-len(r),0)),0
```

**How it works**

- The g.f. is −x / Σ_{k>0} k(−x)ᵏ/(1 − (−x)ᵏ) (Somos). With x → −x and
  Σ_{k>0} k·xᵏ/(1 − xᵏ) = Σ σ(m)xᵐ, the numbers b(n) = (−1)ⁿa(n) have
  g.f. B(x) = x / Σ σ(m)xᵐ, so Σ_{m≥1} σ(m)·b(n + 1 − m) = 0 for n ≥ 1:
  **b(n) = −Σ_{m=2}^{n+1} σ(m)·b(n + 1 − m)**, b(0) = 1 (the same as
  the entry's formula with the signs (−1)^(k+1) taken out).
- `r` is b(0), …, b(n − 1) followed by a 0 that stands for the unknown
  b(n). For d = −e, `r[d::d]` reads r[−e], r[−2e], …, the terms
  b(n + 1 − m) for the multiples m of e, so Σ_d d·sum(r[d::d]) over
  d = −len(r), …, −1 is −Σ_m σ(m)·r[−m]. The m = 1 term hits the 0
  placeholder, so the sum is b(n).
- `r[-1:]=…,0` puts b(n) in the placeholder's slot and appends a new 0;
  `s` flips sign every pass, so `s*r[-2]` prints a(n) = (−1)ⁿb(n).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002039), CC BY-SA 4.0.
