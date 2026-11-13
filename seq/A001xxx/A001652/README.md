# A001652

> a(n) = 6*a(n-1) - a(n-2) + 2 with a(0) = 0, a(1) = 3.
> — [OEIS A001652](https://oeis.org/A001652)

Offset 0: 0, 3, 20, 119, 696, 4059, 23660, 137903, 803760, 4684659, 27304196, …

### Python 3 — 37 bytes

```python
a=0;b=3
while[print(a)]:a,b=b,6*b-a+2
```

**How it works**

- The recurrence of the name, run directly: `a`, `b` hold a(n), a(n+1),
  starting from a(0) = 0, a(1) = 3, and each pass prints a(n) and moves the
  window by a(n+2) = 6a(n+1) − a(n) + 2.

**Notes**

- The entry is marked "changed"; its data and b-file follow the recurrence
  of the name, which is what the program does. (These are the legs a with
  a² + (a+1)² a square: 2a + 1 runs through 1, 7, 41, … but printing
  `b//2` of that homogeneous sequence costs 2 bytes more.)
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001652), CC BY-SA 4.0.
