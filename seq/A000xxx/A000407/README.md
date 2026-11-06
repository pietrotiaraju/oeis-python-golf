# A000407

> a(n) = (2*n+1)! / n!.
> — [OEIS A000407](https://oeis.org/A000407)

Offset 0: 1, 6, 60, 840, 15120, 332640, 8648640, 259459200, 8821612800, 335221286400, …

### Python 3 — 33 bytes

```python
a=1;k=6
while[print(a)]:a*=k;k+=4
```

**How it works**

- The ratio of consecutive terms cancels almost completely:
  a(n+1)/a(n)=(2n+3)(2n+2)/(n+1)=4n+6.
  With a(0)=1, the sequence is obtained by multiplying successively
  by 6, 10, 14, … .
- At each print, a is the current term and k is the multiplier for
  the next term. `a*=k;k+=4` advances both values without computing
  a factorial or keeping a separate sequence index.
- `print(a)` returns `None`, but `[None]` is nonempty, so the list
  in the condition keeps the loop going. The initial value is printed
  before any multiplication, giving the required offset zero.

**Notes**

- Exact integer multiplication proves the invariant at every step.
  The factorial expression needs no division in this form.
- Equivalently a(n)=2ⁿ(2n+1)!!, so the ratio loop combines the
  powers of two and odd-factor product into a single state.
- Only a and the next multiplier are stored; their integer sizes grow
  with n. Python 3.11+ eventually stops at the default 4300-digit
  output conversion limit, an interpreter limit rather than a wrong term.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000407), CC BY-SA 4.0.
