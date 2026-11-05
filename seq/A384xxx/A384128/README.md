# A384128

> Number of iterations for the circular absolute first-difference on decimal
> digits to reach a repdigit.
> — [OEIS A384128](https://oeis.org/A384128)

Offset 1: 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, …

The map replaces each digit by its distance to the next one, the last digit
wrapping round to the first, and drops leading zeros:
109 → 198 → 817 → 761 → 156 → 415 → 341 → 132 → 211 → 101 → 110 → 11,
so a(109) = 11.

### Python 3 — 118 bytes

```python
f=lambda n:len({*(s:=b'%d'%n)})>1and-~f(int(bytes(48+abs(a-b)for a,b in zip(s,s[1:]+s))))
n=1
while[print(+f(n))]:n+=1
```

**How it works**

- `b'%d'%n` writes n as bytes, so iterating over it gives the ASCII codes of
  the digits, and `a-b` of two codes is the difference of the digits.
- `zip(s,s[1:]+s)` pairs each digit with the next one, and the last with the
  first (`zip` stops at the shorter argument).
- `bytes(48+abs(a-b)…)` writes the new digits as text again, and `int(…)`
  reads them, dropping the leading zeros.
- `len({*s})>1` is false for a repdigit, so the recursion stops there and
  returns `False`; one step up, `-~False` is 1. The `+` in `print(+f(n))`
  turns the `False` of a repdigit n into 0.
- `>1and` raises a `SyntaxWarning` on stderr, which the rules allow.

**Notes**

- The program follows the worked example and the listed terms. The formula
  F(n) in the OEIS comments puts each difference one place to the right of
  where the example does; it gives the same terms up to 100, but a(101) = 1
  instead of the listed 2.
- The definition assumes every n reaches a repdigit. For n < 10⁴ it takes at
  most 11 steps, as the OEIS comment says.
- The b-file has only the 106 terms of the entry, so the bar is all of them.
- The same steps as two nested `while` loops are 122 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A384128), CC BY-SA 4.0.
