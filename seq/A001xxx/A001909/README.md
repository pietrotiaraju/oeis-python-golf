# A001909

> a(n) = n*a(n-1) + (n-4)*a(n-2), a(2) = 0, a(3) = 1.
> — [OEIS A001909](https://oeis.org/A001909)

Offset 2: 0, 1, 4, 21, 134, 1001, 8544, 81901, 870274, 10146321, 128718044, …

### Python 3 — 48 bytes

```python
a=x=0;b=1
while[print(a)]:a,b=b,x*(a+b)+4*b;x+=1
```

**How it works**

- **The recurrence itself.** a(n) = n·a(n − 1) + (n − 4)·a(n − 2) from
  a(2) = 0, a(3) = 1. `a`, `b` are a(n − 2), a(n − 1) and `x` is n − 4 for
  the term being made, so n·a(n − 1) + (n − 4)·a(n − 2) = `x*(a+b)+4*b`.
  Starting with x = 0 at n = 4 saves the initial values: one statement sets
  a(n − 2) = 0 and x = 0.
- **Generating function.** exp(−x)/(1 − x)^5 = Σ a(m + 3)·xᵐ/m!, which gives
  (1 − x)·f′ = (4 + x)·f and so this recurrence (with n = m + 4).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 99 terms (n = 2 to 100); the bar is the whole b-file in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001909), CC BY-SA 4.0.
