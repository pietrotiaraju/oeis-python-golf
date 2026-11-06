# A000422

> Concatenation of numbers from n down to 1.
> — [OEIS A000422](https://oeis.org/A000422)

Offset 1: 1, 21, 321, 4321, 54321, 654321, 7654321, 87654321, 987654321, 10987654321, …

### Python 3 — 40 bytes

```python
s='';n=0
while 1:print(s:=str(n:=n+1)+s)
```

**How it works**

- s holds the decimal text of the previous term. Increment n first,
  convert it to text, and prepend it: sₙ=str(n)+s_(n−1), with
  s₀ the empty string. This gives “1”, “21”, “321”, … .
- The inner walrus `n:=n+1` advances the counter before `str` reads
  it. The outer `s:=...` retains the new concatenation while passing
  that same string to `print`.
- Every component is positive, so there is no leading zero. The
  printed string is exactly the decimal representation of the required
  integer; there is no need to construct that integer internally.
- Crossing a digit boundary needs no special case: from s₉=987654321,
  prepend “10” to obtain s₁₀=10987654321.

**Notes**

- The new n is prepended as an entire block, preserving the order of
  its own digits. Reversing the decimal text of “123…n” would give
  a different result once n has more than one digit.
- The output length is Σₖ₌₁ⁿ digits(k), of order n·log n. Each
  concatenation allocates the full new string, and printing also takes
  time proportional to that output length.
- The assembled output is never converted to an integer, so Python's
  4300-digit integer conversion limit does not apply to that string.
  Compare [A000461](../A000461/) for repeated, rather than descending,
  concatenation blocks.
- The b-file has 150 terms (indices 1 through 150). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000422), CC BY-SA 4.0.
