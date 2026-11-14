# A001688

> 4th forward differences of factorial numbers A000142.
> — [OEIS A001688](https://oeis.org/A001688)

Offset 0: 9, 53, 362, 2790, 24024, 229080, 2399760, 27422640, 339696000, …

### Python 3 — 47 bytes

```python
a,b=9,2;n=0
while[print(a)]:b+=a;n+=1;a=n*a+4*b
```

**How it works**

- Write T(k, n) = Δᵏ n! for the k-th forward difference of the factorials,
  so a(n) = T(4, n). Applying Δᵏ to (n + 1)! = (n + 1)·n! with the Leibniz
  rule for differences (Δ of n + 1 is 1, Δ² is 0) gives
  T(k, n + 1) = (n + 1)·T(k, n) + k·T(k − 1, n + 1), and by the definition
  of Δ, T(k − 1, n + 1) = T(k − 1, n) + T(k, n).
- So the pair a = T(4, n), b = T(3, n) moves one step with `b+=a` (now
  b = T(3, n + 1)), `n+=1` and `a=n*a+4*b`. At n = 0,
  T(k, 0) = Σⱼ (−1)ᵏ⁻ʲ C(k, j)·j! is the derangement number D(k): the start
  is a, b = D(4), D(3) = 9, 2.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- The closed form a(n) = n!·(n⁴ + 6n³ + 17n² + 20n + 9) becomes
  (n − 1)!·(n²((n + 2)n + 5) + 1) with n shifted by one, and in the factorial
  loop of [A001565](../A001565/) that is
  `f=n=1` / `while[print(f*n*n*((n+2)*n+5)+f)]:f*=n;n+=1`, 49 bytes. Bala's
  recurrence a(n) = (n + 5)·a(n − 1) − (n − 1)·a(n − 2), which holds only
  from n = 2, needs both a(0) and a(1): 51 bytes.
- Exact integers, so every term is right; a(1555) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Differences of factorials: [A001563](../A001563/),
  [A001564](../A001564/), [A001565](../A001565/), [A001688](../A001688/),
  [A001689](../A001689/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001688), CC BY-SA 4.0.
