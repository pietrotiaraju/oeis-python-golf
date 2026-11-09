# A001217

> Sorted list of orders of Weyl groups of types A_n, B_n, D_n, E_n, F_4, G_2.
> — [OEIS A001217](https://oeis.org/A001217)

Offset 1: 1, 2, 4, 6, 8, 12, 24, 48, 120, 192, 384, 720, 1152, 1920, 3840, 5040, 23040, …

### Python 3 — 118 bytes

```python
S={1,12,1152,51840,2903040,696729600}
k=f=1
while[print(v)for v in sorted(S)if k>=v//f>0]:k+=1;f*=k;S|={f,f<<k,f<<k-1}
```

**How it works**

- The orders are |A_n| = (n+1)!, |B_n| = 2ⁿ·n!, |D_n| = 2ⁿ⁻¹·n!, and the
  exceptional 12 (G₂), 1152 (F₄), 51840, 2903040, 696729600 (E₆, E₇, E₈).
  E₃, E₄, E₅ (= A₂×A₁, A₄, D₅) repeat orders already there, and the data
  counts order 1 (A₀) and 4 (D₂ = A₁×A₁).
- Round k, with f = k!, adds the three values of index k to the set `S`:
  f, f·2ᵏ = `f<<k` and f·2ᵏ⁻¹ = `f<<k-1`. It then prints, sorted, the
  members of `S` in [k!, (k+1)!), tested as `k>=v//f>0`.
- That window is complete: a value of index m is at least m!, so every
  order below (k+1)! has index ≤ k and is already in `S`. And the window
  always holds k! itself, so the list is never empty and the `while` never
  stops. The set merges repeats (2 = |A₁| = |B₁|, 24 = |A₃| = |D₃|, …).

**Notes**

- The whole b-file (34 terms, up to 2¹⁰·10! = 3715891200) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001217), CC BY-SA 4.0.
