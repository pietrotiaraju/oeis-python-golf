# A001908

> E.g.f. exp(-x)/(1-5*x).
> — [OEIS A001908](https://oeis.org/A001908)

Offset 0: 1, 4, 41, 614, 12281, 307024, 9210721, 322375234, 12895009361, …

### Python 3 — 33 bytes

```python
a=n=0
while[print(a:=a*n^1)]:n+=5
```

**How it works**

- **Recurrence.** exp(−x)/(1 − 5x) is exp(−x) times Σ 5ⁿxⁿ, so
  a(n) = n!·5ⁿ·Σⱼ₌₀ⁿ (−1/5)ʲ/j!, and the last term of that sum gives
  a(n) = 5n·a(n − 1) + (−1)ⁿ, a(0) = 1.
- **Parity.** a(n) is odd exactly when n is even: a(0) = 1; for even n,
  5n·a(n − 1) is even and a(n) adds 1; for odd n, a(n − 1) is odd, 5n·a(n − 1)
  is odd and a(n) subtracts 1. So 5n·a(n − 1) has the parity of n, and adding
  (−1)ⁿ is XOR with 1: `a:=a*n^1`, with `n` holding 5n, the trick of
  [A000180](../../A000xxx/A000180/).

**Notes**

- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+, first passed by a(1276).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001908), CC BY-SA 4.0.
