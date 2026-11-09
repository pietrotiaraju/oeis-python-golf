# A001206

> Number of self-dual monotone Boolean functions of n variables.
> — [OEIS A001206](https://oeis.org/A001206)

Offset 0: 0, 1, 2, 4, 12, 81, 2646, 1422564, 229809982112, 423295099074735261880

### Python 3 — 141 bytes

```python
print('0\n1');D={0:1,1:0}
while[print(sum(h&a&D[a]==h for a in D for h in D))]:D={a|b*-~D[0]:D[b]|D[a]*-~D[0]for a in D for b in D if a&~b<1}
```

**How it works**

- A Boolean function f of k variables is a 2ᵏ-bit integer: bit x is f(x),
  the point x read in binary. Its low half a is f with the last variable 0,
  its high half b is f with it 1, and f = a + b·2^(2ᵏ⁻¹). f is monotone
  exactly when a and b are monotone and a ≤ b, i.e. `a&~b<1`. So the
  monotone functions of k variables come in pairs from those of k − 1.
- The dual is f*(x) = ¬f(x̄), x̄ the complement of x. Complementing the last
  variable swaps the halves, so (a, b)* = (b*, a*). The keys of `D` are the
  monotone functions of k variables and `D[f]` is f*; a new level is built
  with `D[b]|D[a]*…` next to `a|b*…`. `D[0]` is the dual of the constant 0,
  the constant 1 = 2^(2ᵏ) − 1, so `-~D[0]` is the shift for the next level.
  The start {0: 1, 1: 0} is k = 0.
- f is self-dual (f* = f) and monotone exactly when f = (g, g*) with g
  monotone of n − 1 variables and g ≤ g*. Write g = (h, a) with h ≤ a, both
  of n − 2 variables. Then g* = (a*, h*), and g ≤ g* asks h ≤ a* and
  a ≤ h*, which are the same condition (no x with h(x) and a(x̄)). So
  a(n) = #{(h, a): h ≤ a ∧ a*}, the pairs counted by `h&a&D[a]==h` over the
  functions of n − 2 variables: the first `D` gives a(2) = 2.
- a(0) = 0 (a constant is never its own negation) and a(1) = 1 (f = x) are
  printed first. `while[print(…)]:` is a byte under `while 1:print(…);`.

**Notes**

- Exact integer arithmetic; nothing beyond the two halving facts above.
- The functions of n − 2 variables are the Dedekind numbers 2, 3, 6, 20,
  168, 7581, 7828354 of them, and the count costs their square. a(7) needs
  7581² pairs, about 20 s here. Then the program builds the 7828354
  functions of six variables, which takes about 1 GB of memory (under a
  300 MB cap it stops there with a MemoryError), and a(8) would need
  6·10¹³ pairs.
- The b-file has 10 terms (up to a(9)); the bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 141 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001206), CC BY-SA 4.0.
