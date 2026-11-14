# A001700

> a(n) = binomial(2*n+1, n+1): number of ways to put n+1 indistinguishable balls into n+1 distinguishable boxes = number of (n+1)-st degree monomials in n+1 variables = number of monotone maps from 1..n+1 to 1..n+1.
> — [OEIS A001700](https://oeis.org/A001700)

Offset 0: 1, 3, 10, 35, 126, 462, 1716, 6435, 24310, 92378, 352716, 1352078, …

### Python 3 — 39 bytes

```python
a=j=1
while[print(a)]:j+=2;a=a*4*j//-~j
```

**How it works**

- a(n) = C(2n + 1, n + 1) and a(n − 1) = C(2n − 1, n), so
  a(n)/a(n − 1) = (2n + 1)·2n/((n + 1)·n) = 4j/(j + 1) with j = 2n + 1.
- `j` runs over the odd numbers from 1, and `a=a*4*j//-~j` multiplies by 4j
  and then divides by j + 1 (`-~j`). The product a(n − 1)·4j is
  (j + 1)·a(n), so the floor division is exact.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- The same ratio written 4 − 2/(n + 1), the step of the central binomials
  [A000984](../../A000xxx/A000984/) with the counter moved first
  (`c=n=1` / `while[print(c)]:n+=1;c=4*c-2*c//n`), ties at 39 bytes; also
  a(n) = A000984(n + 1)/2. `math.comb` needs an import and is longer.
- Exact integers, so every term is right; a(7146) is the first term over
  4300 digits, so Python's int-to-str limit stops the program there.
- The b-file has 1201 terms (a(0) to a(1200)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001700), CC BY-SA 4.0.
