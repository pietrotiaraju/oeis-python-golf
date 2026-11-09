# A001317

> Sierpiński's triangle (Pascal's triangle mod 2) converted to decimal.
> — [OEIS A001317](https://oeis.org/A001317)

Offset 0: 1, 3, 5, 15, 17, 51, 85, 255, 257, 771, 1285, 3855, 4369, 13107, 21845, 65535, …

Row n of Pascal's triangle mod 2, read as the binary digits of a number:
a(n) = Σₖ (C(n, k) mod 2)·2ᵏ.

### Python 3 — 26 bytes

```python
a=1
while[print(a)]:a^=2*a
```

**How it works**

- Row 0 is the single entry 1, so a(0) = 1. The rows are palindromes, so it
  does not matter which end of the row is the units digit.
- Pascal's rule C(n+1, k) = C(n, k) + C(n, k−1) becomes, mod 2, addition
  without carries, that is XOR. The terms C(n, k−1) are row n moved up one
  place, which is 2·a(n) in binary, so a(n+1) = a(n) XOR 2·a(n) (the formula
  of Paul D. Hanna in the entry). `a^=2*a` is that step.
- `print` returns `None` and `[None]` is a non-empty list, so the loop never
  ends. Exact integers, so it is right for every n.

**Notes**

- `a^=a+a` is also 26 bytes. Lucas's theorem (C(n, k) is odd exactly when
  the bits of k are a subset of those of n) gives the direct
  `n=0` + `while[print(sum(1<<k for k in range(n+1)if n&k==k))]:n+=1`,
  61 bytes and quadratic.
- a(n) has n + 1 bits, so the terms pass the 4300-digit int-to-str limit of
  Python 3.11+ at n = 14285 (4301 digits), where the program stops with a
  `ValueError`.
- The b-file has 3322 terms (n = 0 to 3321, the last one 1000 digits long);
  the bar is the whole b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 26 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001317), CC BY-SA 4.0.
