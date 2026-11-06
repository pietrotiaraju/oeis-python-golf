# A000300

> 4th power of rooted tree enumerator: linear forests of 4 rooted trees.
> — [OEIS A000300](https://oeis.org/A000300)

Offset 4: 1, 4, 14, 44, 133, 388, 1116, 3168, 8938, 25100, 70334, 196824, …

The g.f. is B(x)⁴, where B(x) = x·E(x) counts rooted trees
([A000081](../A000081/)) and E(x) = exp(Σₖ B(xᵏ)/k). So a(m + 4) = h(m), the
coefficient of xᵐ in E⁴.

### Python 3 — 107 bytes

```python
*L,n=1,1,0
while[print(L[-2])]:
 n-=2
 for w in 4,1:L+=w*sum(d*L[~d]*sum(L[d::d])for d in range(n,0,2))//n,
```

**How it works**

- **Two recurrences, one kernel.** Writing e(m) for the coefficients of E,
  so that the number of rooted trees with k nodes is e(k − 1),
  **m·e(m) = Σₖ k·e(k − 1)·Σⱼ e(m − jk)** is the [A000081](../A000081/)
  recurrence. Since log E⁴ = 4·log E, the same derivation gives
  **m·h(m) = 4·Σₖ k·e(k − 1)·Σⱼ h(m − jk)**: only the factor w = 4 differs.
- One list holds both interleaved: `L` = [h(0), e(0), h(1), e(1), …], and
  each round appends h(m), then e(m). The loop condition prints `L[-2]` =
  h(m) = a(m + 4).
- With n = −2m and d = −2k, e(k − 1) sits at position 2k − 1 = `~d` in
  both passes, and `L[d::d]` steps back by 2k from the end: through
  h(m − k), h(m − 2k), … in the h pass and, one entry later, through
  e(m − k), e(m − 2k), … in the e pass. The factor 2 in d cancels against
  the 2 in n.
- `w*` comes before `//n`: 4·Σ is divisible by m, but Σ need not be
  (for m = 2 it is 7).

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n. a(n) has about 0.47·n digits, so the 4300-digit int-to-str limit
  is near n = 9200, beyond what the program reaches.
- About 3100 terms in 60 s here; the bar is the whole b-file (497 terms),
  which prints in under a second.
- J. C. P. Miller's power recurrence, h(m) = Σₖ (5k − m)·e(k)·h(m − k)/m,
  needs e(k) for k up to m, so it has to run next to the A000081 line for
  e: about 144 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000300), CC BY-SA 4.0.
