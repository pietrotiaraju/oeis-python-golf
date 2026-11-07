# A000971

> Fermat coefficients.
> — [OEIS A000971](https://oeis.org/A000971)

Offset 6: 1, 9, 42, 132, 334, 728, 1428, 2584, 4389, 7084, 10963, 16380, 23751, 33563, 46376, 62832, 83657, 109668, 141778, 181001, …

### Python 3 — 47 bytes

```python
d=2
while[print((d**5*4-d**3*5+d+45)//90)]:d+=1
```

**How it works**

- This is the Fermat coefficient (n:6) = C(2n−6, 5)/6 rounded to the
  nearest integer. It really is rounded, not truncated: a(10) = 334 while
  (10:6) = 2002/6 = 333.67 (the name of [A258708](https://oeis.org/A258708)
  says "integer part", but its data, like this sequence's, is rounded).
- With d = n − 4, N = 2n−6 = 2d+2 and the five factors of C(N, 5) are the
  numbers around 2d: C(N, 5) = d(d²−1)(4d²−1)/15, so (n:6) = P/90 with
  P = 4d⁵ − 5d³ + d.
- N is even, so C(N, 5) is even (Lucas' theorem mod 2, 5 = 101₂), and
  P mod 90 = 15·(C(N, 5) mod 6) ∈ {0, 30, 60}: never a tie, and
  round(P/90) = ⌊(P + 45)/90⌋, `(d**5*4-d**3*5+d+45)//90`.

**Notes**

- Exact integer arithmetic; the steps above are identities plus Lucas'
  theorem.
- `(math.comb(n,5)+3)//6` stepping n by 2 is 9 bytes longer with its
  import.
- The b-file has 995 terms (n = 6..1000) and all of them print in under
  0.1 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000971), CC BY-SA 4.0.
