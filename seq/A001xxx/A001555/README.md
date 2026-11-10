# A001555

> a(n) = 1^n + 2^n + ... + 8^n.
> — [OEIS A001555](https://oeis.org/A001555)

Offset 0: 8, 36, 204, 1296, 8772, 61776, 446964, 3297456, 24684612, 186884496, …

### Python 3 — 52 bytes

```python
n=0
while[print(sum(i**n for i in range(1,9)))]:n+=1
```

**How it works**

- The definition: `sum(i**n for i in range(1,9))` is 1ⁿ + 2ⁿ + … + 8ⁿ,
  for n = 0, 1, 2, ….
- The range starts at 1, not 0: 0⁰ = 1 in Python, so `range(9)` would
  give a(0) = 9. Written out, `1+2**n+…+8**n` would be 36 characters
  against 29 here: the generator is shorter from seven terms on.

**Notes**

- The same family, sums up to 3ⁿ … 10ⁿ: [A001550](../A001550/), [A001551](../A001551/), [A001552](../A001552/), [A001553](../A001553/), [A001554](../A001554/), [A001556](../A001556/), [A001557](../A001557/).
- Exact integer arithmetic, so the program is right for every n; a(n) has about n·log₁₀8 digits, so Python's 4300-digit
  int-to-str limit stops it at about n = 4800.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001555), CC BY-SA 4.0.
