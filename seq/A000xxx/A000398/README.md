# A000398

> Numbers of form x^2 + 2y^2 + 2yz + 4z^2.
> — [OEIS A000398](https://oeis.org/A000398)

Offset 1: 0, 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, …

### Python 3 — 79 bytes

```python
s={n:=0}
while[s&{2*n-2*j-7*k for j in s for k in s}and print(n)]:n+=1;s|={n*n}
```

**How it works**

- Doubling the form and completing the square removes the cross term:
  2(x² + 2y² + 2yz + 4z²) = 2x² + (2y + z)² + 7z². Conversely, if
  2n = 2x² + a² + 7b², then a² + 7b² is even, so a ≡ b (mod 2), and
  z = b, y = (a − b)/2 are integers that give n. So n is in the sequence
  exactly when 2n − 2x² − 7b² is a square for some squares x², b².
- `s` is the set of squares 0², 1², …, n², which contains every square up
  to 2n (n² ≥ 2n for n ≥ 2, and {0} and {0, 1} are enough for n = 0, 1).
  The program builds all 2n − 2j − 7k with j, k in `s` and prints n when
  that set meets `s`.
- This is the frame of [A000394](../A000394/) (x² + y² + 7z²), with
  squares only, so no ranges of signed y and z are needed.

**Notes**

- Exact integers. The missing numbers 7, 10, 21, 35, 42, 70, 79, … are
  mostly multiples of 7 but not all (10, 79), so the program uses no
  congruence shortcut.
- `n+n-j-j-7*k` is the same length as `2*n-2*j-7*k`. Searching y and z
  over a signed range instead of squares is longer and slower.
- Term n looks at (n + 1)² pairs, so the program prints about 600 terms
  (up to n ≈ 640) in 60 s. The bar is 450 terms; the b-file has 1000
  (up to 1072).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000398), CC BY-SA 4.0.
