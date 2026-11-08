# A001082

> Generalized octagonal numbers: k*(3*k-2), k=0, +- 1, +- 2, +-3, ...
> — [OEIS A001082](https://oeis.org/A001082)

Offset 1: 0, 1, 5, 8, 16, 21, 33, 40, 56, 65, …

### Python 3 — 31 bytes

```python
m=1
while[print(m*m//3)]:m+=m%3
```

**How it works**

- Put m = 3k − 1. Then k(3k − 2) = (m² − 1)/3, and since m is never a
  multiple of 3, m² ≡ 1 (mod 3), so the term is just `m*m//3`.
- As k runs 0, 1, −1, 2, −2, 3, …, m runs −1, 2, −4, 5, −7, 8, …: in
  absolute value 1, 2, 4, 5, 7, 8, …, the positive integers not divisible
  by 3, in increasing order. Only m² is used, so the program walks those.
- `m+=m%3` steps from one to the next: it adds 1 when m ≡ 1 and 2 when
  m ≡ 2 (mod 3), skipping each multiple of 3.
- At offset 1, a(1) = 1//3 = 0 for k = 0.

**Notes**

- Walking k itself with the [A001057](../A001057/) step,
  `k=0` / `while[print(k*(3*k-2))]:k=(k<1)-k`, is 37 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1000 terms (a(1) to a(1000)); the bar is the whole b-file
  in 60 s.
- The octagonal numbers themselves (k ≥ 0) are
  [A000567](../../A000xxx/A000567/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001082), CC BY-SA 4.0.
