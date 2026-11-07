# A000970

> Fermat coefficients.
> — [OEIS A000970](https://oeis.org/A000970)

Offset 5: 1, 7, 25, 66, 143, 273, 476, 775, 1197, 1771, 2530, 3510, 4750, 6293, 8184, 10472, 13209, 16450, 20254, 24682, …

### Python 3 — 39 bytes

```python
s=7
while[print((s*s-5)**2//1920)]:s+=4
```

**How it works**

- This is the Fermat coefficient (n:5) = C(2n−5, 4)/5 rounded to the
  nearest integer (the column T(n, n−5) of [A258708](https://oeis.org/A258708),
  round(C(2n−5, 5)/(2n−9)), is the same number).
- With N = 2n−5, Lucas' theorem gives C(N, 4) ≡ C(N mod 5, 4) ∈ {0, 1}
  (mod 5), so the fractional part is 0 or 1/5 and rounding is the floor.
- C(N, 4) = x(x+2)/24 with x = N(N−3), so (n:5) = ((x+1)² − 1)/120. N is
  odd, so x+1 is odd and (x+1)² is not a multiple of 120: the floor is
  ⌊(x+1)²/120⌋.
- Completing the square, 4(x+1) = s² − 5 with s = 2N − 3 = 4n − 13, so
  a(n) = ⌊(s² − 5)²/1920⌋ for s = 7, 11, 15, … No import, no product of
  four factors.

**Notes**

- Exact integer arithmetic; the steps above are identities plus Lucas'
  theorem.
- The b-file has 996 terms (n = 5..1000) and all of them print in under
  0.1 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000970), CC BY-SA 4.0.
