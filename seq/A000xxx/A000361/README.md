# A000361

> Binary encodings of the successive columns of the Gosper-Lafitte triangle.
> — [OEIS A000361](https://oeis.org/A000361)

Offset 0: 1, 0, 2, 1, 1, 2, 5, 0, 10, 6, 3, 2, 19, 2, 10, 1, 5, 10, 89, 1, 170, 28, 7, 2, 71, 12, 170, 5, …

### Python 3 — 81 bytes

```python
a,b=0,1
while[print(sum(((~k*a-1)%b-~a)%2<<k for k in range(b)))]:a,b=b,a+b-a%b*2
```

**The formula**

Column n of the Gosper–Lafitte triangle (see [A000360](../A000360/)) is a
binary word of length q = s(n+1), 1 for a filled triangle and 0 for an
empty one, where s is Stern's diatomic sequence
[A002487](https://oeis.org/A002487); a(n) reads it as a binary number,
bottom digit last. Lafitte's formula on the OEIS page reads the word off a
rotation modulo q: with p = s(n) and the digits v_0 … v_(q−1) from the top,

v_j = (((j·p − 1) mod q) + 1 − p) mod 2,  a(n) = Σ_j v_j·2^(q−1−j).

**How it works**

- `a,b` is the Stern pair (s(n), s(n+1)) = (p, q), advanced by Newman's
  recurrence s(n+1) = s(n−1) + s(n) − 2·(s(n−1) mod s(n)), as in
  [A000360](../A000360/).
- The sum runs over the bit positions k = q−1−j instead of j, so no
  `b-1-j` is needed: j·p − 1 = (q−1−k)·p − 1 ≡ −(k+1)·p − 1 = `~k*a-1`
  (mod q).
- `-~a` adds p + 1, which has the parity of 1 − p, and `%2<<k` puts the
  digit at weight 2^k.

**Notes**

- Integers only, exact for every n. The b-file has 10000 terms (n = 0 to
  9999, the longest about 400 digits) and they all print in about a second;
  the bar is the whole b-file.
- The formula is checked against the recursive construction on the OEIS
  page (each column word is a lift of one or two earlier words, the PARI
  `w(n)`): both agree on all 10000 b-file terms, and the popcount of a(n)
  reproduces [A000360](../A000360/) there.
- `((~k*a-1)%b-~a&1)<<k` is the same length as `((~k*a-1)%b-~a)%2<<k`;
  `~(k*a+a)%b` is the same length as `(~k*a-1)%b`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000361), CC BY-SA 4.0.
