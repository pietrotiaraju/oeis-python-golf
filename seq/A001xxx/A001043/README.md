# A001043

> Numbers that are the sum of 2 successive primes.
> — [OEIS A001043](https://oeis.org/A001043)

Offset 1: 5, 8, 12, 18, 24, 30, 36, 42, 52, 60, 68, 78, 84, 90, 100, 112, 120, 128, …

### Python 3 — 49 bytes

```python
P=k=q=2
while k:=k+1:~P%k or print(q+(q:=k));P*=k
```

**How it works**

- Primes by Wilson's theorem, as in [A000040](../../A000xxx/A000040/):
  k starts at 3 with P = 2! and `~P%k` is 0 exactly when k divides
  (k−1)! + 1.
- `q` is the previous prime, 2 at the start. `print(q+(q:=k))` reads the
  old q before the walrus sets it to k.

**Notes**

- Exact integer arithmetic.
- About 13 000 terms in 60 s; the whole b-file (10 000 terms) prints in
  about 33 s, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001043), CC BY-SA 4.0.
