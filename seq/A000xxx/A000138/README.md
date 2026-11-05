# A000138

> Expansion of e.g.f. exp(-x^4/4)/(1-x).
> — [OEIS A000138](https://oeis.org/A000138)

Offset 0: 1, 1, 2, 6, 18, 90, 540, 3780, 31500, 283500, 2835000, 31185000, …

### Python 3 — 54 bytes

```python
a=t=n=1
while[print(a)]:k=n%4<1;t*=-k|n;a=a*n+k*t;n+=1
```

**How it works**

- Dividing by 1 − x takes partial sums, so a(n)/n! = Σ_{i≤n/4} (−1)ⁱ/(i!·4ⁱ)
  and a(n) = n·a(n−1) + c(n), where c(n) = n!·[xⁿ] exp(−x⁴/4) is zero unless
  4 | n, and c(4m) = (−1)ᵐ (4m)!/(m!·4ᵐ). (This counts the permutations of n
  letters with no 4-cycle.)
- `t` holds (−1)ᵐ n!/(m!·4ᵐ) with m = ⌊n/4⌋. Between multiples of 4 it is
  multiplied by n. At n = 4m the new factor n in n! cancels the new 4m in
  m!·4ᵐ, so `t` only changes sign, and then it is exactly c(n).
- `k=n%4<1` flags the multiples of 4. `-k|n` is n when k = 0 and −1 when
  k = 1 (−1 has every bit set), so `t*=-k|n` does both updates.
- `a=a*n+k*t` is the recurrence above.

**Notes**

- Each term costs two big-integer products, so the b-file's 101 terms take
  milliseconds. The bar is the whole b-file in 60 s. Terms pass the
  4300-digit int-to-str limit near n = 1558.
- `t*=k*~n+n` does the same as `t*=-k|n` in two more bytes, and the walrus
  `t*=-(k:=n%4<1)|n` is one byte longer than the separate `k=n%4<1;`.
- The sign can also ride on the three steps between multiples of 4
  (`t*=k or-n`, since (−1)³ = −1), but that is two bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000138), CC BY-SA 4.0.
