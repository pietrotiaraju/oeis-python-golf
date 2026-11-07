# A000520

> Nearest integer to log_10(n).
> — [OEIS A000520](https://oeis.org/A000520)

Offset 1: 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, …

### Python 3 — 39 bytes

```python
n=1
while[print(len(str(n*n))//2)]:n+=1
```

**How it works**

- If n² has d decimal digits, then 10^(d−1) ≤ n² < 10^d, so
  d − 1 ≤ 2·log₁₀ n < d and (2·log₁₀ n + 1)/2 lies in [d/2, (d+1)/2). The
  nearest integer ⌊log₁₀ n + 1/2⌋ is therefore ⌊d/2⌋, which is
  `len(str(n*n))//2`.
- There are no ties: log₁₀ n = k + 1/2 would make n² = 10^(2k+1), which is
  not a square.
- The test needs only integer squaring and a decimal conversion, so no
  floating-point logarithm can round the wrong way.

**Notes**

- `len(f'{n*n}')//2` is the same length. A counter that steps up when
  n² passes 10^(2k+1), `n=1;k=0` / `while[print(k)]:n+=1;k+=n*n>10*100**k`,
  is 45 bytes.
- Exact integer arithmetic, so the program is right for every n. The
  4300-digit int-to-str limit would only matter for n near 10^2150.
- The b-file has 1000 terms (up to a(1000)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000520), CC BY-SA 4.0.
