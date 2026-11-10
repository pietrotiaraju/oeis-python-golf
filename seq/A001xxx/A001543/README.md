# A001543

> a(0) = 1, a(n) = 5 + Product_{i=0..n-1} a(i) for n > 0.
> — [OEIS A001543](https://oeis.org/A001543)

Offset 0: 1, 6, 11, 71, 4691, 21982031, 483209576974811, …

### Python 3 — 32 bytes

```python
p=a=1
while[print(a)]:a=p+5;p*=a
```

**How it works**

- The definition: a(n) = 5 + a(0)·a(1)·…·a(n−1). `p` holds that product:
  `a=p+5` is a(n), and `p*=a` adds it to the product for the next term.
- Since a(0) = 1, the start `p=a=1` serves both as a(0) and as the product
  a(0) = 1 that a(1) = 5 + 1 = 6 needs.

**Notes**

- Charles Greathouse's form a(n) = a(n−1)·(a(n−1) − 5) + 5 holds only
  from n = 2 (a(0) = 1 is a fixed point of it), so it needs a(0) apart:
  `print(1);a=6` / `while[print(a)]:a=a*(a-5)+5` is 40 bytes.
- The same program with 6 in place of 5 is [A001544](../A001544/).
- Exact integer arithmetic, so the program is right for every n. a(n)
  grows doubly exponentially (the number of digits doubles at each step):
  a(14) has 3760 digits and a(15) 7519, so Python's 4300-digit
  int-to-str limit stops the program after a(14).
- The b-file has 13 terms (a(0) to a(12), up to 940 digits); the bar is
  the whole b-file in 60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 32 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001543), CC BY-SA 4.0.
