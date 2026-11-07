# A000706

> Expansion of modular function 1/E_3 (cf. A013973).
> — [OEIS A000706](https://oeis.org/A000706)

Offset 0: 1, 504, 270648, 144912096, 77599626552, 41553943041744, 22251789971649504, 11915647845248387520, …

### Python 3 — 81 bytes

```python
a=1,
while[print(a[-1])]:a+=-504*sum(d**5*sum(a[d::d])for d in range(-len(a),0)),
```

**How it works**

- E_3 in the old notation (weight 6, now written E₆) is
  1 − 504·Σ σ₅(k)·qᵏ ([A013973](https://oeis.org/A013973)), with
  σ₅(k) = Σ_{d|k} d⁵. So a = 1/E₆ satisfies
  **a(N) = 504·Σ_{k=1..N} σ₅(k)·a(N − k)** for N ≥ 1, and grouping the
  divisor sums by d turns the right side into
  504·Σ_d d⁵·Σ_j a(N − dj) over j ≥ 1 with dj ≤ N.
- `a` is the tuple a(0), …, a(N−1); `d` runs over −N…−1 and the slice
  `a[d::d]` is a(N − |d|), a(N − 2|d|), …, the same layout as the
  [A000041](../A000041/) program. d⁵ is negative for negative d, hence
  `-504`.
- No division here, so no counter is needed: `-len(a)` is shorter than
  keeping n beside the list. The tuple `a=1,` is a byte under `a=[1]`, and
  `+=` on a tuple makes a new one, which costs N copies per term, little
  next to the slice sums.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
  a(n) ~ 0.94·e^(2πn) has about 2.73·n digits, so the 4300-digit
  int-to-str limit stops the program at n ≈ 1575, far past the b-file.
- The whole b-file (361 terms) prints in well under a second; the bar is
  the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000706), CC BY-SA 4.0.
