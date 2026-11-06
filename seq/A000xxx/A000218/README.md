# A000218

> Take sum of squares of digits of previous term; start with 3.
> — [OEIS A000218](https://oeis.org/A000218)

Offset 1: 3, 9, 81, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …

### Python 3 — 49 bytes

```python
n=3
while[print(n)]:n=sum(d*d%96for d in b'%d'%n)
```

**How it works**

- The program applies the definition: each new `n` is the sum of the squares
  of the digits of the old one. It does not rely on the orbit being
  periodic, so it is right for every n.
- `b'%d'%n` is the decimal expansion of `n` as a `bytes` object, and
  iterating over it gives the ASCII codes c = 48 + d of the digits d.
- c² − d² = (c − d)(c + d) = 48(2c − 48) = 96(c − 24), so c² ≡ d² (mod 96).
  Since d² ≤ 81 < 96, `d*d%96` (here `d` is the code c) is exactly the square
  of the digit. 96 is the only modulus that works: it has to divide every
  96(c − 24) for c = 48, …, 57, that is divide 96, and be larger than 81.
- `96for` makes CPython 3.12 print a `SyntaxWarning` (invalid decimal
  literal) on stderr; the program runs normally.
- `while[print(n)]:` prints in the loop test: `[None]` is a non-empty list,
  so the loop never ends.

**Notes**

- From 3 the orbit is 3 → 9 → 81 → 65 → 61 → 37 → 58 → 89 → 145 → 42 → 20
  → 4 → 16 → 37, so after five terms it runs round the 8-cycle
  37, 58, 89, 145, 42, 20, 4, 16 (Porges 1945).
- The usual form, `n=sum(int(d)**2for d in str(n))`, is 51 bytes: `d*d%96`
  saves 3 bytes on `int(d)**2` and `b'%d'%n` costs 1 more than `str(n)`.
- The byte table of [A000216](../A000216/) (store S on the orbit, index it
  with something like `n%53%9`) does not pay here. The 13 orbit points have
  12 different successors (only 61 and 16 share one, 37), and 145 has to be
  written `\x91`, so the table is at least 15 bytes; to beat 49 bytes, index
  and table together would have to fit in 21 bytes, which means a 6-byte
  index that sends the 13 points into exactly 12 slots. A search over
  one- and two-operator indices (`n%a%b`, `~n%a%b`, `-n%a%b`, `a%n%b`,
  `a//n%b`, `n*a%b`, `n*n%a%b`, `(n^a)%b`, … with a < 2000, b < 60) found
  nothing close: the best, `772//n%17` with a 15-slot table, gives 54 bytes.
- The b-file has 100 terms and the program prints them at once; the bar is
  the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000218), CC BY-SA 4.0.
