# A001861

> Expansion of e.g.f. exp(2*(exp(x) - 1)).
> — [OEIS A001861](https://oeis.org/A001861)

Offset 0: 1, 2, 6, 22, 94, 454, 2430, 14214, 89918, 610182, 4412798, 33827974, …

### Python 3 — 48 bytes

```python
t,*r=1,
while[print(t)]:r=[t:=t+x for x in[t]+r]
```

**How it works**

- **The numbers.** a(n) = Σₖ 2ᵏ·S(n, k) counts the set partitions of n
  labeled points with each block painted one of 2 colours; the e.g.f.
  A = exp(2(eˣ − 1)) satisfies A′ = 2eˣ·A, so
  a(n + 1) = 2·Σⱼ C(n, j)·a(j) (twice the binomial transform, as on the
  OEIS page).
- **An Aitken array.** Put B(n, k) = 2·Σⱼ C(k, j)·a(n − k + j) for
  0 ≤ k ≤ n. Pascal's rule gives B(n, k) = B(n, k − 1) + B(n − 1, k − 1),
  the row starts with B(n, 0) = 2a(n), and it ends with
  B(n, n) = 2·Σⱼ C(n, j)·a(j) = a(n + 1). So each row starts with twice the
  last entry of the row above and adds the row above term by term, like the
  Bell triangle.
- **The program.** [A000110](../../A000xxx/A000110/)'s Bell program with
  `[0]` changed to `[t]`: `t` is the last entry of the previous row,
  a(n), and in `r=[t:=t+x for x in[t]+r]` the first step doubles it and the
  next ones add the previous row. After the pass t is the new last entry,
  a(n + 1), which the header prints. `t,*r=1,` starts with t = a(0) = 1 and
  an empty row.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 1939.
- The b-file has 559 terms (n = 0 to 558); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001861), CC BY-SA 4.0.
