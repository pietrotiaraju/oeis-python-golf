# A000073

> Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with a(0) = a(1) = 0 and a(2) = 1.
> — [OEIS A000073](https://oeis.org/A000073)

Offset 0: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, …

### Python 3 — 39 bytes

```python
l=0,0,1
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- l begins as the triple (0,0,1). Before iteration n, it holds
  a(n),a(n+1),a(n+2), where the next tribonacci term is their sum.
- Python evaluates the whole right side `*l,sum(l)` before assigning
  the left side. It is the old triple followed by a(n+3).
  The unpacking `a,*l` takes a(n) into a and keeps the remaining
  three values as the next window.
- Print a after advancing the window. This emits exactly the oldest
  term, beginning with 0,0,1, and retains only three future terms.
  It is the same window update used by [A000078](../A000078/),
  with three entries instead of four.
- All additions use exact integers; there is no input or stored
  sequence table beyond the three defining initial values.

**Notes**

- An earlier scalar form starts one step before a(0), from a(-1)=1: `a=1;b=c=0` +
  `while[print(b)]:a,b,c=b,c,a+b+c` is also 41 bytes.
- The initial tuple becomes a three-element list after the first
  unpacking. Its length stays three throughout the loop.
- In the earlier scalar form, `a=b=c=1` saves two bytes but gives
  A000213 (1, 1, 1, 3, 5, 9, …), and a(n) = (A000213(n+1) - A000213(n))/2
  costs `print((b-a)//2)`, seven bytes more than `print(a)`.
- The closed form a(n) = floor(2^(n^2+n)/(2^(3n) - 2^(2n) - 2^n - 1)) mod
  2^n (Prunescu and Sauras Altuzarra) is exact but needs 58 bytes:
  `n=0` + `while[print(2**(n*n+n)//(8**n-4**n-2**n-1)%2**n)]:n+=1`.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(16251), the first term with 4301 digits, after printing a(0) to
  a(16250). The limit is not counted as a failure.
- The b-file has 3001 terms (n = 0 to 3000, the last one has 794 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |
| 2026-11-06 | Python 3 | 39 | advance a three-term window with extended unpacking |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000073), CC BY-SA 4.0.
