# A001041

> a(0)=12; thereafter a(n) = 12 times the product of the first n primes.
> — [OEIS A001041](https://oeis.org/A001041)

Offset 0: 12, 24, 72, 360, 2520, 27720, 360360, 6126120, 116396280, 2677114440, …

### Python 3 — 54 bytes

```python
a=12;P=k=1
while 1:
 if P%k:print(a);a*=k
 P*=k*k;k+=1
```

**How it works**

- a(n) = 12·p₁p₂⋯pₙ, so the program walks k = 1, 2, 3, … and multiplies
  a, which starts at a(0) = 12, by every prime k it meets.
- Primes come from Wilson's theorem in its squared form: with
  P = ((k − 1)!)², P mod k is 1 when k is prime and 0 when k is composite
  (and 0 for k = 1). `P*=k*k;k+=1` keeps P = ((k − 1)!)².
- At a prime k the current a is 12 times the primes below k, which is the
  next term: it is printed, then `a*=k`. The first prime, 2, prints
  a(0) = 12.

**Notes**

- Exact integer arithmetic; the only theorem used is Wilson's.
- The whole b-file (101 terms) prints at once. The program stops after
  a(1229), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001041), CC BY-SA 4.0.
