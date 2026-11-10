# A001557

> a(n) = 1^n + 2^n + ... + 10^n.
> — [OEIS A001557](https://oeis.org/A001557)

Offset 0: 10, 55, 385, 3025, 25333, 220825, 1978405, 18080425, 167731333, …

### Python 3 — 53 bytes

```python
n=0
while[print(sum(i**n for i in range(1,11)))]:n+=1
```

**How it works**

- The definition: `sum(i**n for i in range(1,11))` is 1ⁿ + 2ⁿ + … + 10ⁿ,
  for n = 0, 1, 2, ….
- The range starts at 1, not 0: 0⁰ = 1 in Python, so `range(11)` would
  give a(0) = 11. Written out, `1+2**n+…+10**n` would be 47 characters
  against 30 here: the generator is shorter from seven terms on.

**Notes**

- The same family, sums up to 3ⁿ … 10ⁿ: [A001550](../A001550/), [A001551](../A001551/), [A001552](../A001552/), [A001553](../A001553/), [A001554](../A001554/), [A001555](../A001555/), [A001556](../A001556/).
- Exact integer arithmetic, so the program is right for every n; a(n) has n + 1 digits, so Python's 4300-digit int-to-str limit
  stops it after a(4299).
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001557), CC BY-SA 4.0.
