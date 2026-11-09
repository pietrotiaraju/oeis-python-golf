# A001175

> Pisano periods (or Pisano numbers): period of Fibonacci numbers mod n.
> — [OEIS A001175](https://oeis.org/A001175)

Offset 1: 1, 3, 8, 6, 20, 24, 16, 12, 24, 60, 10, 24, 28, 48, 40, 24, 36, 24, 18, 60, …

### Python 3 — 68 bytes

```python
n=k=1
while[print(k)]:
 n+=1;a=b=k=1
 while a%n|~-b%n:a,b=b,a+b;k+=1
```

Siblings: the entry points [A001177](../A001177/), the number of zeros per
period [A001176](../A001176/), and the iterations of this map in
[A001178](../A001178/) and [A001179](../A001179/).

**How it works**

- Modulo n the step (F_k, F_{k+1}) ↦ (F_{k+1}, F_k + F_{k+1}) is a bijection
  of the n² residue pairs (it can be run backwards), so the orbit of
  (F_0, F_1) = (0, 1) is a cycle and comes back. The Pisano period is the
  first k ≥ 1 with F_k ≡ 0 and F_{k+1} ≡ 1 (mod n).
- The search starts at (F_1, F_2) = (1, 1) with k = 1 and steps until the
  pair is (0, 1) mod n. `a%n|~-b%n` is 0 exactly when n divides both F_k and
  F_{k+1} − 1 (`~-b` is b − 1); for n = 1 it is 0 at once, so a(1) = 1.
- The Fibonacci numbers are kept exact, not reduced: `a,b=b,a+b` is 2 bytes
  under `a,b=b%n,a+b`. The period is at most 6n, so F_k has at most about
  4.2n bits, which only costs speed.
- `while[print(k)]:` prints a(1) = 1 before the first pass; each pass sets up
  the next n.

**Notes**

- Exact for every n.
- About 5400 terms in 22 s on the PC it was written on. The b-file has 10000;
  the bar is 5000 terms in 60 s.
- Reducing (`a,b=b%n,a+b`, 70 bytes) keeps the numbers below 2n and prints
  the whole b-file in about 24 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001175), CC BY-SA 4.0.
