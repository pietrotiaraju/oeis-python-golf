# A001223

> Prime gaps: differences between consecutive primes.
> — [OEIS A001223](https://oeis.org/A001223)

Offset 1: 1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4, 2, 4, 14, 4, 6, 2, 10, 2, 6, …

### Python 3 — 51 bytes

```python
P=k=q=2
while[P%k and print(-q+(q:=k))]:P*=k*k;k+=1
```

**How it works**

- `P` is 2·((k−1)!)². By Wilson's theorem ((k−1)!)² ≡ 1 modulo a prime k,
  so `P%k` is 2 for every odd prime; for a composite k it is 0, because
  k | ((k−1)!)² (for k = 4, 3!² = 36). Starting at `P=k=q=2` makes the
  first test k = 2 with `P%k` = 0, so the prime 2 only becomes the
  previous prime `q`.
- At each odd prime `-q+(q:=k)` prints k − q and moves `q` on in one go.

**Notes**

- The factorial grows, so the terms slow down: about 6700 gaps in 30 s
  here. The b-file has 100000 terms; the bar is 5000 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001223), CC BY-SA 4.0.
