# A001248

> Squares of primes.
> — [OEIS A001248](https://oeis.org/A001248)

Offset 1: 4, 9, 25, 49, 121, 169, 289, 361, 529, 841, 961, 1369, …

### Python 3 — 42 bytes

```python
P=k=1
while[-P%k==1==print(k*k)]:P*=k;k+=1
```

**How it works**

- The Wilson-theorem prime loop of [A000040](../../A000xxx/A000040/),
  printing `k*k`. k ≥ 2 is prime exactly when (k − 1)! ≡ −1 (mod k).
- `P` is kept equal to (k − 1)!: it starts at 0! = 1, and `P*=k;k+=1`
  turns (k − 1)! into k! as k moves on.
- `-P%k` is `(-P)%k`, so `-P%k==1` is the theorem's test. For k = 1 every
  number is 0 mod 1, so 1 is skipped; for k = 4, 3! = 6 ≡ 2 (mod 4) fails,
  and every other composite k divides (k − 1)!.
- The chained comparison `-P%k==1==print(k*k)` means
  `-P%k==1 and 1==print(k*k)`, so the square is printed only for primes.
  The list around it is non-empty, so the loop never stops.

**Notes**

- The squared-factorial test of A000040, `P=k=1` /
  `while[P%k>0==print(k*k)]:P*=k*k;k+=1`, is also 42 bytes, and slower.
- P has about k log₂ k bits, so each step costs about k log k. The whole
  b-file (10 000 terms, up to 104 729²) prints in about 28 s here; the
  bar is the whole b-file in 60 s, as for A000040.
- Exact integer arithmetic, so the program is right for every n; the
  printed squares stay far below the 4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001248), CC BY-SA 4.0.
