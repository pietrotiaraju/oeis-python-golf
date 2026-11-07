# A000722

> Number of invertible Boolean functions of n variables: a(n) = (2^n)!.
> — [OEIS A000722](https://oeis.org/A000722)

Offset 0: 1, 2, 24, 40320, 20922789888000, 263130836933693530167218012160000000, …

### Python 3 — 42 bytes

```python
f=k=1
while[print(f)]:exec("k+=1;f*=k;"*k)
```

**How it works**

- An invertible map {0,1}ⁿ → {0,1}ⁿ is a permutation of the 2ⁿ points, so
  a(n) = (2ⁿ)!.
- `f` is k! with k = 2ⁿ. The string `"k+=1;f*=k;"*k` is built from the
  current k before it runs, so it multiplies `f` by k+1, …, 2k and leaves
  k = 2k: one term per `exec`, with no import and no inner loop.

**Notes**

- (2¹¹)! = 2048! has 5895 digits, past CPython's 4300-digit int-to-str
  limit, so the program prints 11 terms (n = 0..10) and then stops with a
  `ValueError` (an interpreter limit, not a wrong term).
- The b-file stops at n = 8 (values under 1000 digits); all 9 terms are
  the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000722), CC BY-SA 4.0.
