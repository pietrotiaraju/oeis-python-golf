# A001556

> a(n) = 1^n + 2^n + ... + 9^n.
> — [OEIS A001556](https://oeis.org/A001556)

Offset 0: 9, 45, 285, 2025, 15333, 120825, 978405, 8080425, 67731333, …

### Python 3 — 53 bytes

```python
n=0
while[print(sum(i**n for i in range(1,10)))]:n+=1
```

**How it works**

- The definition: `sum(i**n for i in range(1,10))` is 1ⁿ + 2ⁿ + … + 9ⁿ,
  for n = 0, 1, 2, ….
- The range starts at 1, not 0: 0⁰ = 1 in Python, so `range(10)` would
  give a(0) = 10. Written out, `1+2**n+…+9**n` would be 41 characters
  against 29 here: the generator is shorter from seven terms on.

**Notes**

- The same family, sums up to 3ⁿ … 10ⁿ: [A001550](../A001550/), [A001551](../A001551/), [A001552](../A001552/), [A001553](../A001553/), [A001554](../A001554/), [A001555](../A001555/), [A001557](../A001557/).
- Exact integer arithmetic, so the program is right for every n; a(n) has about n·log₁₀9 digits, so Python's 4300-digit
  int-to-str limit stops it at about n = 4500.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001556), CC BY-SA 4.0.
