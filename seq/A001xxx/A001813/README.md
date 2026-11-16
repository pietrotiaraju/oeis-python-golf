# A001813

> Quadruple factorial numbers: a(n) = (2n)!/n!.
> — [OEIS A001813](https://oeis.org/A001813)

Offset 0: 1, 2, 12, 120, 1680, 30240, 665280, 17297280, 518918400, 17643225600, …

### Python 3 — 33 bytes

```python
a=1;n=2
while[print(a)]:a*=n;n+=4
```

**How it works**

- a(n)/a(n − 1) = (2n)(2n − 1)/n = 4n − 2, so a(n) is the product
  2·6·10·…·(4n − 2) of the first n numbers ≡ 2 (mod 4), and a(0) = 1.
- `a` starts at 1 and `n` at 2, the first factor; each pass multiplies
  by `n` and moves it on by 4.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Same length: `a=n=1` / `while[print(a)]:a*=n+n;n+=2` (factors 2·(2k − 1)).
- Same shape as [A001147](../A001147/) (odd double factorials, step 2) and
  [A000165](../A000165/) (2ⁿ·n!, step 2 from 2).
- a(1310) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001813), CC BY-SA 4.0.
