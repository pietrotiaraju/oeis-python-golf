# A001249

> Squares of tetrahedral numbers: a(n) = binomial(n+3,n)^2.
> — [OEIS A001249](https://oeis.org/A001249)

Offset 0: 1, 16, 100, 400, 1225, 3136, 7056, 14400, 27225, 48400, …

### Python 3 — 38 bytes

```python
n=2
while[print((n**3-n)**2//36)]:n+=1
```

**How it works**

- C(n+3, 3) = (n+1)(n+2)(n+3)/6. With m = n + 2 this is (m−1)·m·(m+1)/6
  = (m³ − m)/6, so a(n) = (m³ − m)²/36. The loop variable is m: it starts
  at 2, which gives (8 − 2)²/36 = 1 = a(0).
- m³ − m is a product of three consecutive integers, so 6 divides it, 36
  divides its square, and `//36` is exact.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends.

**Notes**

- Squaring the tetrahedral number of [A000292](../../A000xxx/A000292/)
  as `((n**3-n)//6)**2` is 1 byte longer than dividing the square by 36.
- Exact integer arithmetic, so the program is right for every n; the
  terms grow like n⁶/36, so the 4300-digit int-to-str limit is never
  reached in practice.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001249), CC BY-SA 4.0.
