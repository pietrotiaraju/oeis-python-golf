# A000496

> Restricted permutations.
> — [OEIS A000496](https://oeis.org/A000496)

Offset 0: 1, 1, 2, 6, 24, 44, 80, 144, 260, 476, …

### Python 3 — 70 bytes

```python
a=[1,1,2,6,24,44,80,144,260]
while[print(a.pop(0))]:a+=[2*a[-1]-a[-4]]
```

**How it works**

The rational generating function recorded by Plouffe describes
the tail beginning at n=4:
sum(a(n+4)*x^n,n>=0)=(24-4x-8x²-16x³-4x⁴)/(1-2x+x⁴).
Its first five coefficients are 24,44,80,144,260, and the
remaining coefficients satisfy a(n)=2a(n-1)-a(n-4).
For n=0..3 the unrestricted counts are n!=1,1,2,6.
The queue holds those initial coefficients and then extends
the rational-series recurrence indefinitely.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1001 terms in 60 s; the official b-file contains 1001 terms.
- Correctness beyond the verified terms depends on Plouffe's rational generating function, explicitly labeled conjectural in the OEIS entry. The program does not embed the b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000496), CC BY-SA 4.0.
