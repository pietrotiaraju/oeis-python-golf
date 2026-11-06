# A000346

> a(n) = 2^(2*n+1) - binomial(2*n+1, n+1).
> — [OEIS A000346](https://oeis.org/A000346)

Offset 0: 1, 5, 22, 93, 386, 1586, 6476, 26333, 106762, 431910, …

### Python 3 — 49 bytes

```python
a=c=n=1
while[print(a)]:n+=1;c=4*c-6*c//n;a=4*a+c
```

**How it works**

- Write b(n) = C(2n+1, n+1) = C(2n+1, n), so a(n) = 2·4^n − b(n). Then
  a(n+1) − 4a(n) = 4b(n) − b(n+1), and since b(n+1) = b(n)·2(2n+3)/(n+2) this
  is 2b(n)/(n+2) = C(2n+2, n+1)/(n+2), the Catalan number C_{n+1}. So
  a(n+1) = 4a(n) + C_{n+1}, which is the OEIS remark that a is the
  convolution of the Catalan numbers with the powers of 4.
- `c` runs through the Catalan numbers exactly as in the
  [A000108](../A000108/) record: with `n` one more than the index,
  `n+=1;c=4*c-6*c//n` steps C_{n−2} to C_{n−1}, and the division is exact.
- `a=4*a+c` then adds the new Catalan number. `a=c=n=1` sets a(0) = 1,
  C_0 = 1 and the counter at once.

**Notes**

- Printing in the walrus, `a=0;c=n=1` + `while[print(a:=4*a+c)]:n+=1;c=4*c-6*c//n`,
  is 50 bytes: a(−1) = 0 needs its own assignment.
- Keeping b and p = 2·4^n, `b=1;p=k=2` + `while[print(p-b)]:b=4*b-2*b//k;p*=4;k+=1`,
  is 50. The closed form with `import math`, stepping m = 2n + 1 by 2, is
  `2**m-math.comb(m,m//2)` in 57 bytes.
- Exact integers, so every term is right. a(7142) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 501 terms (n = 0 to 500) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000346), CC BY-SA 4.0.
