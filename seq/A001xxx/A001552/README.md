# A001552

> a(n) = 1^n + 2^n + ... + 5^n.
> — [OEIS A001552](https://oeis.org/A001552)

Offset 0: 5, 15, 55, 225, 979, 4425, 20515, 96825, 462979, 2235465, 10874275, …

### Python 3 — 44 bytes

```python
n=0
while[print(1+2**n+3**n+4**n+5**n)]:n+=1
```

**How it works**

- The definition, written out: `1+2**n+…+5**n` is 1ⁿ + 2ⁿ + … + 5ⁿ
  (1ⁿ = 1), for n = 0, 1, 2, ….
- Written out, each term costs 5 bytes; the generator
  `sum(i**n for i in range(1,6))` costs 29, so writing the sum out is
  shorter up to six terms, and the generator from seven on.

**Notes**

- The same family, sums up to 3ⁿ … 10ⁿ: [A001550](../A001550/), [A001551](../A001551/), [A001553](../A001553/), [A001554](../A001554/), [A001555](../A001555/), [A001556](../A001556/), [A001557](../A001557/).
- Exact integer arithmetic, so the program is right for every n; a(n) has about n·log₁₀5 digits, so Python's 4300-digit
  int-to-str limit stops it at about n = 6200.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001552), CC BY-SA 4.0.
