# A001900

> Successive numerators of Wallis's approximation to Pi/2 (unreduced).
> — [OEIS A001900](https://oeis.org/A001900)

Offset 0: 1, 2, 4, 16, 64, 384, 2304, 18432, 147456, 1474560, 14745600, 176947200, …

### Python 3 — 34 bytes

```python
a=n=1
while[print(a)]:n+=1;a*=n&-2
```

**How it works**

- **The product.** Wallis's product π/2 = (2·2·4·4·6·6⋯)/(1·3·3·5·5·7⋯); a(n)
  is the unreduced numerator after n factors, 2·2·4·4⋯ (n of them), so
  a(n) = a(n − 1)·2⌈n/2⌉, from a(0) = 1.
- **The program.** The loop's `n` runs one ahead of the index (it is 1 while
  a(0) is printed). When it becomes k + 1, `a*=n&-2` multiplies by n with its
  last bit cleared, 2⌊(k + 1)/2⌋ = 2⌈k/2⌉, which turns a(k − 1) into a(k).

**Notes**

- Checked against the product of the first n factors of 2, 2, 4, 4, 6, 6, …
  for n < 200, and against the b-file.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 1558.
- The b-file has 450 terms (n = 0 to 449); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001900), CC BY-SA 4.0.
