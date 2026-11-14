# A001689

> 5th forward differences of factorial numbers A000142.
> — [OEIS A001689](https://oeis.org/A001689)

Offset 0: 44, 309, 2428, 21234, 205056, 2170680, 25022880, 312273360, 4196666880, …

### Python 3 — 48 bytes

```python
a,b=44,9;n=0
while[print(a)]:b+=a;n+=1;a=n*a+5*b
```

**How it works**

- Write T(k, n) = Δᵏ n! for the k-th forward difference of the factorials,
  so a(n) = T(5, n). Applying Δᵏ to (n + 1)! = (n + 1)·n! with the Leibniz
  rule for differences (Δ of n + 1 is 1, Δ² is 0) gives
  T(k, n + 1) = (n + 1)·T(k, n) + k·T(k − 1, n + 1), and by the definition
  of Δ, T(k − 1, n + 1) = T(k − 1, n) + T(k, n).
- So the pair a = T(5, n), b = T(4, n) moves one step with `b+=a` (now
  b = T(4, n + 1)), `n+=1` and `a=n*a+5*b`. At n = 0,
  T(k, 0) = Σⱼ (−1)ᵏ⁻ʲ C(k, j)·j! is the derangement number D(k): the start
  is a, b = D(5), D(4) = 44, 9.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- The pair (a, b) here is (A001689, [A001688](../A001688/)), and the start
  9 of b is A001688's own first term.
- The closed form a(n) = n!·(n⁵ + 10n⁴ + 45n³ + 100n² + 109n + 44) in
  Horner form is 62 bytes or more; Bala's recurrence
  a(n) = (n + 6)·a(n − 1) − (n − 1)·a(n − 2) (from n = 2, with a(0) = 44,
  a(1) = 309) is 53.
- Exact integers, so every term is right; a(1554) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.
- Differences of factorials: [A001563](../A001563/),
  [A001564](../A001564/), [A001565](../A001565/), [A001688](../A001688/),
  [A001689](../A001689/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001689), CC BY-SA 4.0.
