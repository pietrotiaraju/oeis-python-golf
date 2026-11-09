# A001161

> Numbers containing an even number of letters.
> — [OEIS A001161](https://oeis.org/A001161)

Offset 1: 0, 4, 5, 9, 11, 12, 13, 14, 18, 19, 20, 24, 25, 29, 30, 34, 35, 39, 41, 42, …

### Python 3 — 171 bytes

```python
M=239585418511822
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+(M>>28+e//3)+f(n%10**e)or n>19and(M>>n//10+18)+f(n%10)or M>>n
n=0
while 1:f(n)%2or print(n);n+=1
```

**Which names**

- US English, as in [A005589](https://oeis.org/A005589), the letter count
  this entry refers to: no "and" ("one hundred one"), short scale (a billion
  is 10⁹), letters only (spaces and hyphens do not count). The OEIS data stop
  at 99, where all conventions agree; from 101 on the British "and" would add
  3 letters and flip the parity.
- Scale words: thousand, million, …, vigintillion (10⁶³), with the spellings
  sexdecillion and novemdecillion, as in [A000052](../../A000xxx/A000052/).

**How it works**

- Only the parity of the count matters, and the parity of a sum is the sum
  of the parities. So the program keeps one bit per word in M: bit i is the
  parity of the length of word i, with i = 0–19 for zero (set to 0, never
  spoken inside a name), one, …, nineteen; 20–27 for twenty … ninety, reached
  by `n//10+18`; 28–49 for hundred, thousand, million, …, vigintillion,
  reached by `28+e//3`.
- `M>>i` has bit i as its lowest bit, so f adds up the shifted numbers
  instead of the bits and takes `%2` once at the end. The sums are huge but
  always positive, which keeps the `and`/`or` chain safe.
- f follows the name: for n ≥ 100, e is the exponent of the largest word
  that fits (`~-len(str(n))//3*3` is the digit count minus one rounded down to
  a multiple of 3, and `or 2` gives "hundred" for three digits), and
  f(n) = f(n // 10ᵉ) + word + f(n mod 10ᵉ); 20–99 is the tens word plus the
  units; below 20 a single word.
- `f(n)%2or print(n)` prints n when the count is even. f(0) is the empty name, 0 letters, and "zero" has 4: both even, so 0 comes out right.

**Notes**

- Exact for every n below 10⁶⁶, where the names stop; the scan would need
  10⁶⁶ steps to get there. Past it, `M>>50` and beyond read as an even word.
- The b-file has the 50 terms below 100 from the OEIS data, printed at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 171 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001161), CC BY-SA 4.0.
