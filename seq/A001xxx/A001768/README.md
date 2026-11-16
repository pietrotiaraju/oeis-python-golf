# A001768

> Sorting numbers: number of comparisons for merge insertion sort of n
> elements.
> — [OEIS A001768](https://oeis.org/A001768)

Offset 1: 0, 1, 3, 5, 7, 10, 13, 16, 19, 22, 26, 30, 34, 38, 42, 46, 50, 54, …

### Python 3 — 44 bytes

```python
s=k=0
while 1:k+=3;s+=len(bin(k))-4;print(s)
```

**How it works**

- Knuth (TAOCP 5.3.1) gives a(n) = Σ_{j=1..n} ⌈log₂(3j/4)⌉: merge
  insertion spends ⌈log₂(3j/4)⌉ comparisons on the j-th element.
- 3j/4 is never a power of 2 (3 does not divide 2ᵐ), so the ceiling is the
  floor plus 1: ⌈log₂(3j/4)⌉ = ⌊log₂ 3j⌋ − 1, which is the bit length of 3j
  minus 2. `len(bin(k))` is the bit length plus 2 for the `0b`, hence `-4`.
- k runs through 3j directly (`k+=3`), and s is the running sum, printed
  after each step: j = 1 adds 0, so the first line is a(1) = 0.

**Notes**

- Printing first, `while[print(s)]:` with `s=0;k=3`, is 45 bytes. The
  closed form n(z − 1) − ⌊(2^(z+2) − 3z)/6⌋ with z = ⌊log₂(3n + 3)⌋ needs a
  formula per term and is 65 bytes.
- Exact integer arithmetic, so the program is right for every n. The
  b-file (10000 terms) prints in 0.2 s; the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001768), CC BY-SA 4.0.
