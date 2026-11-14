# A001748

> a(n) = 3 * prime(n).
> — [OEIS A001748](https://oeis.org/A001748)

Offset 1: 6, 9, 15, 21, 33, 39, 51, 57, 69, 87, 93, 111, 123, 129, 141, 159, 177, …

### Python 3 — 42 bytes

```python
P=k=1
while[-P%k==1==print(3*k)]:P*=k;k+=1
```

**How it works**

- The terms are 3k for k prime, in order, so the program is
  [A000040](../../A000xxx/A000040/) with `print(3*k)`.
- Wilson's theorem: k ≥ 2 is prime exactly when (k − 1)! ≡ −1 (mod k).
  `P` is kept equal to (k − 1)!: it starts at 0! = 1 and `P*=k;k+=1` turns
  (k − 1)! into k!.
- `-P%k==1==print(3*k)` is `-P%k==1 and 1==print(3*k)`, so the print runs
  only for primes. k = 1 fails (everything is 0 mod 1), and so does k = 4
  (3! ≡ 2 mod 4), the only composite with (k − 1)! not ≡ 0.
- The list `[…]` around the test is non-empty, so the loop never ends.

**Notes**

- A000040's other 40-byte forms, `while k:=k+1:~P%k or print(k);P*=k` and the
  squared factorial, `while[P%k>0==print(k)]:P*=k*k;k+=1`, tie here too
  (42 bytes).
- P has about k log₂ k bits, so each step costs about k log k. The b-file has 20000 terms (up to 3 · 224737). On GitHub's runner the first 12000 arrive in about 24 s and about 17700 terms in the 60 s, so the bar is 12000 terms in 60 s.
- Multiples of primes: [A001747](../A001747/) (2), [A001748](../A001748/)
  (3), [A001749](../A001749/) (4), [A001750](../A001750/) (5).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001748), CC BY-SA 4.0.
