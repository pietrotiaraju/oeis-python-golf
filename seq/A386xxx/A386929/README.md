# A386929

> a(n) is the least base b in {2,...,10} such that the base-b expansion of n,
> when read as a decimal integer, is prime; a(n) = 0 if no such base exists.
> — [OEIS A386929](https://oeis.org/A386929)

Offset 1: 0, 3, 2, 3, 2, 5, 4, 5, 6, 3, 4, 9, 4, 0, 6, 5, 4, 0, 4, 0, …

### Python 3 — 131 bytes

```python
n=1
while[print(next((b for b in range(2,11)if(m:=sum(n//b**i%b*10**i for i in range(n)))*all(m%d for d in range(2,m))>1),0))]:n+=1
```

**How it works**

- `n//b**i%b` is the i-th base-b digit of n, and multiplying by 10ⁱ puts it
  in the i-th decimal place, so the sum is n written in base b and read in
  decimal. n has at most n digits in any base, so `range(n)` covers them all
  (the extra digits are 0).
- The prime test is trial division by every d from 2 to m − 1. Multiplying
  by m and asking for more than 1 also rejects m = 1, the reading of n = 1.
- The walrus in the condition assigns m before `all` builds its `range(2,m)`.
- `next(…,0)` returns the first base that works, or 0 when none does.

**Notes**

- Trial division up to m is exact but slow when m is prime: base 2 turns
  n ≈ 250 into an 8-digit number. The program prints about 300 terms a minute;
  the bar is 200 terms in 60 s.
- Stopping the trial division at `math.isqrt(m)` and reading the digits with
  the recursion `f=lambda n,b:n and n%b+10*f(n//b,b)` takes 162 bytes and
  about 10 000 terms a minute. The recursion alone, with the slow test, is 135.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A386929), CC BY-SA 4.0.
