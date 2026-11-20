# A001947

> a(n) = Lucas(5*n+2).
> — [OEIS A001947](https://oeis.org/A001947)

Offset 0: 3, 29, 322, 3571, 39603, 439204, 4870847, 54018521, 599074578, 6643838879, …

### Python 3 — 37 bytes

```python
a,b=3,29
while[print(a)]:a,b=b,a+11*b
```

**How it works**

- **The recurrence.** For any sequence with x(m + 1) = x(m) + x(m − 1),
  x(m + k) + (−1)ᵏx(m − k) = L(k)x(m) (true for x = φᵐ and x = ψᵐ because
  φᵏ + ψᵏ = L(k) and φψ = −1, hence for every combination). With k = 5,
  L(5) = 11: a(n + 1) = L(5n + 7) = 11L(5n + 2) + L(5n − 3) =
  11a(n) + a(n − 1), the entry's recurrence, from a(0) = L(2) = 3 and
  a(1) = L(7) = 29.
- **Program.** The plain pair update: `a`, `b` hold a(n), a(n + 1) and step
  to a(n + 1), a(n) + 11a(n + 1).
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The same program as [A001946](../A001946/) (Lucas(5n)) with the start
  3, 29.
- Python's 4300-digit int-to-str limit stops the program at about n = 4110.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001947), CC BY-SA 4.0.
