# A001910

> a(n) = n*a(n-1) + (n-5)*a(n-2).
> — [OEIS A001910](https://oeis.org/A001910)

Offset 3: 0, 1, 5, 31, 227, 1909, 18089, 190435, 2203319, 27772873, 378673901, …

### Python 3 — 48 bytes

```python
a=x=0;b=1
while[print(a)]:a,b=b,x*(a+b)+5*b;x+=1
```

**How it works**

- **The recurrence itself.** a(n) = n·a(n − 1) + (n − 5)·a(n − 2) from
  a(3) = 0, a(4) = 1. `a`, `b` are a(n − 2), a(n − 1) and `x` is n − 5 for
  the term being made, so n·a(n − 1) + (n − 5)·a(n − 2) = `x*(a+b)+5*b`.
  Starting with x = 0 at n = 5 saves the initial values: one statement sets
  a(n − 2) = 0 and x = 0.
- **Generating function.** exp(−x)/(1 − x)^6 = Σ a(m + 4)·xᵐ/m!, which gives
  (1 − x)·f′ = (5 + x)·f and so this recurrence (with n = m + 5).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 98 terms (n = 3 to 100); the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001910), CC BY-SA 4.0.
