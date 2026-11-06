# A000360

> Distribution of nonempty triangles inside a fractal rep-4-tile.
> — [OEIS A000360](https://oeis.org/A000360)

Offset 0: 1, 0, 1, 1, 1, 1, 2, 0, 2, 2, 2, 1, 3, 1, 2, 1, 2, 2, 4, 1, 4, 3, 3, 1, 4, 2, 4, 2, 3, 2, 3, 0, …

### Python 3 — 47 bytes

```python
a,b=0,1
while[print(b+~a%2>>1)]:a,b=b,a+b-a%b*2
```

**The formula**

a(n) counts the filled triangles in column n of the Gosper–Lafitte
triangle. The OEIS page gives Lafitte's 1995 result in terms of Stern's
diatomic sequence s = [A002487](https://oeis.org/A002487):

a(n) = (s(n+1) + χ₃(n+1)) / 2,

with χ₃(m) = 1, −1, 0 for m ≡ 1, 2, 0 (mod 3); that is, a(3m) =
(s(3m+1)+1)/2, a(3m+1) = (s(3m+2)−1)/2 and a(3m+2) = s(3m+3)/2. Karttunen's
mutual recurrence for the filled and empty counts, on the same page, gives
the same numbers.

**How it works**

- `a,b` runs through consecutive Stern values (s(n), s(n+1)), starting from
  (s(0), s(1)) = (0, 1). The step `a,b=b,a+b-a%b*2` is Newman's recurrence
  s(n+1) = s(n−1) + s(n) − 2·(s(n−1) mod s(n)); b = s(n+1) ≥ 1, so `a%b` is
  always defined.
- s(m) is even exactly when 3 divides m (from s(2m) = s(m) and
  s(2m+1) = s(m) + s(m+1), by induction). So a = s(n) is even exactly when
  n ≡ 0 (mod 3), and `~a%2` = (a+1) mod 2 is 1 there and 0 otherwise.
- When n ≡ 0, s(n+1) is odd and a(n) = (s(n+1)+1)/2; when n ≡ 1, s(n+1) is
  odd and a(n) = (s(n+1)−1)/2 = ⌊s(n+1)/2⌋; when n ≡ 2, s(n+1) is even and
  a(n) = s(n+1)/2. All three are `b+~a%2>>1`.

**Notes**

- Integers only, exact for every n. The b-file has 10001 terms (n = 0 to
  10000), all printed in well under a second; the bar is the whole b-file.
- Computing s(n+1) from its binary digits for each n, or the filled/empty
  mutual recursion as a lambda, is longer than carrying the Stern pair.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000360), CC BY-SA 4.0.
