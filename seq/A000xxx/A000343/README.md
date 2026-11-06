# A000343

> 5th power of rooted tree enumerator; number of linear forests of 5 rooted trees.
> — [OEIS A000343](https://oeis.org/A000343)

Offset 5: 1, 5, 20, 70, 230, 721, 2200, 6575, 19385, 56575, 163952, …

The g.f. is B(x)⁵, where B(x) = x·E(x) counts rooted trees
([A000081](../A000081/)) and E(x) = exp(Σₖ B(xᵏ)/k). So a(m + 5) = h(m), the
coefficient of xᵐ in E⁵. This is [A000300](../A000300/) (fourth power) with
the factor 4 changed to 5.

### Python 3 — 107 bytes

```python
*L,n=1,1,0
while[print(L[-2])]:
 n-=2
 for w in 5,1:L+=w*sum(d*L[~d]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- **Two recurrences, one kernel.** Writing e(m) for the coefficients of E,
  so that the number of rooted trees with k nodes is e(k − 1),
  **m·e(m) = Σₖ k·e(k − 1)·Σⱼ e(m − jk)** is the [A000081](../A000081/)
  recurrence. Since log E⁵ = 5·log E, the same derivation gives
  **m·h(m) = 5·Σₖ k·e(k − 1)·Σⱼ h(m − jk)**: only the factor w = 5 differs.
- One list holds both interleaved: `L` = [h(0), e(0), h(1), e(1), …], and
  each round appends h(m), then e(m). The loop condition prints `L[-2]` =
  h(m) = a(m + 5).
- With n = −2m and d = −2k, e(k − 1) sits at position 2k − 1 = `~d` in
  both passes, and `L[d::d]` steps back by 2k from the end: through
  h(m − k), h(m − 2k), … in the h pass and, one entry later, through
  e(m − k), e(m − 2k), … in the e pass. The factor 2 in d cancels against
  the 2 in n.
- `w*` comes before `//n`: 5·Σ is divisible by m, but Σ need not be
  (for m = 5 it is 721).

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(n) ~ 5·0.4399·2.9558ⁿ·n^(−3/2) (Kotesovec) has about 0.47·n
  digits, so the 4300-digit int-to-str limit is near n = 9150, beyond what
  the program reaches.
- The bar is the whole b-file (746 terms, n ≤ 750), which prints in about
  1 s here.
- The same alternatives as for [A000300](../A000300/) were tried: J. C. P.
  Miller's power recurrence h(m) = Σₖ (6k − m)·e(k)·h(m − k)/m next to the
  A000081 line, two separate lists `r` and `f` updated by
  `for X,w in(r,1),(f,5):` (120 bytes), and repeated dot products of the
  forest list; all are longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000343), CC BY-SA 4.0.
