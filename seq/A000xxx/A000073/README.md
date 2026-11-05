# A000073

> Tribonacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) for n >= 3 with a(0) = a(1) = 0 and a(2) = 1.
> — [OEIS A000073](https://oeis.org/A000073)

Offset 0: 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, …

### Python 3 — 41 bytes

```python
a=b=0;c=1
while[print(a)]:a,b,c=b,c,a+b+c
```

**How it works**

- `a`, `b` and `c` hold three consecutive terms, a(n), a(n+1) and a(n+2),
  starting from a(0) = a(1) = 0 and a(2) = 1. The chained `a=b=0` sets both
  zeros at once, so `a=b=0;c=1` is two bytes shorter than `a,b,c=0,0,1`.
- `print(a)` runs in the loop condition, as in [A000032](../A000032/): it
  returns `None`, and `[None]` is a non-empty list, so the loop never ends.
- `a,b,c=b,c,a+b+c` moves one step along the recurrence: the new triple is
  a(n+1), a(n+2), a(n) + a(n+1) + a(n+2) = a(n+3). Integers are exact, so
  every term is right.

**Notes**

- Starting one step earlier, from a(-1) = 1, is a tie: `a=1;b=c=0` +
  `while[print(b)]:a,b,c=b,c,a+b+c` is also 41 bytes.
- `while 1:print(a);…` is one byte longer than `while[print(a)]:…`.
- Starting from three equal values, `a=b=c=1`, saves two bytes but gives
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

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000073), CC BY-SA 4.0.
