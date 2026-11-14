# A001747

> 2 together with primes multiplied by 2.
> — [OEIS A001747](https://oeis.org/A001747)

Offset 1: 2, 4, 6, 10, 14, 22, 26, 34, 38, 46, 58, 62, 74, 82, 86, 94, 106, 118, …

### Python 3 — 41 bytes

```python
P=k=1
while[~P%k or print(2*k)]:P*=k;k+=1
```

**How it works**

- The terms are 2k for k = 1 and for k prime. By Wilson's theorem a k ≥ 2
  divides (k − 1)! + 1 exactly when k is prime, and k = 1 divides
  everything, so the test "k divides (k − 1)! + 1" picks exactly these k
  (k = 4: 3! + 1 = 7, no; composite k > 4 divide (k − 1)! itself).
- `P` is kept equal to (k − 1)!: it starts at 0! = 1 and `P*=k;k+=1` turns
  (k − 1)! into k!. `~P` is −(P + 1), so `~P%k` is 0 exactly when k | P + 1,
  and then `or` runs `print(2*k)`.
- The list `[…]` around the test is non-empty, so the loop never ends, as in
  [A000040](../../A000xxx/A000040/).

**Notes**

- Admitting k = 1 is what makes the test one byte shorter than A000040's
  `-P%k==1==print(k)`.
- P has about k log₂ k bits; the b-file (1000 terms, up to 2 · 7907) prints
  in well under a second, and the bar is the whole b-file in 60 s.
- Multiples of primes: [A001747](../A001747/) (2), [A001748](../A001748/)
  (3), [A001749](../A001749/) (4), [A001750](../A001750/) (5).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001747), CC BY-SA 4.0.
