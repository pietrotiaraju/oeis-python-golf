# A001309

> Order of real Clifford group L_n connected with Barnes-Wall lattices in dimension 2^n.
> — [OEIS A001309](https://oeis.org/A001309)

Offset 0: 2, 16, 2304, 5160960, 178362777600, 96253116206284800, …

For n ≥ 1 the entry gives a(n) = 2^(n²+n+2) · (2ⁿ − 1) · ∏_{k=1..n−1}
(4ᵏ − 1), the order of the real Clifford group found by Nebe, Rains and
Sloane; a(0) = 2 (the group {±1}).

### Python 3 — 46 bytes

```python
a=x=2
while[print(a)]:a*=x*x*(x*x+x-2)//2;x*=2
```

**How it works**

- For n ≥ 1 the formula gives a(n+1)/a(n) = 2^(2n+2) · (2ⁿ⁺¹ − 1)/(2ⁿ − 1)
  · (4ⁿ − 1) = 4ⁿ⁺¹ (2ⁿ⁺¹ − 1)(2ⁿ + 1), since 4ⁿ − 1 = (2ⁿ − 1)(2ⁿ + 1).
  The same expression at n = 0 is 4 · 1 · 2 = 8 = a(1)/a(0), so one rule
  covers every step from a(0) = 2.
- With x = 2ⁿ⁺¹ the ratio is x²(x − 1)(x + 2)/2 = x²(x² + x − 2)/2; x is
  even, so x² is a multiple of 4 and `//2` is exact.
- `a` and `x` both start at 2: a(0) = 2 and x = 2¹. Each step multiplies
  `a` by the ratio and then doubles `x`: x = 2 gives 4 · 4/2 = 8 and
  a(1) = 16, x = 4 gives 16 · 18/2 = 144 and a(2) = 2304.
- `print(…)` runs in the loop condition: it returns `None`, and `[None]`
  is a non-empty list, so the loop never ends.

**Notes**

- a(n) = 4ⁿ⁺¹ · [A001308](../A001308/)(n) for n ≥ 1: the same product
  times 2^(2n+2). Keeping x = 2ⁿ instead, `a=2` / `x=1` /
  `while[print(a)]:a*=4*x*x*(2*x*x+x-1);x*=2`, is 49 bytes.
- The terms grow like 2^(2n²+n+2): the program prints a(0) to a(84) (4274
  digits) and then stops with a `ValueError` at the interpreter's
  4300-digit int-to-str limit.
- The OEIS has no b-file for this entry; the one here is synthesized from
  the 9 terms of the entry (n = 0 to 8). The bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001309), CC BY-SA 4.0.
