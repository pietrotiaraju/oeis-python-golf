# A000253

> a(n) = 2*a(n-1) - a(n-2) + a(n-3) + 2^(n-1).
> — [OEIS A000253](https://oeis.org/A000253)

Offset 0: 0, 1, 4, 11, 27, 63, 142, 312, 673, 1432, …

### Python 3 — 49 bytes

```python
a=1;b=c=d=0
while[print(d)]:a+=b;b,c=a-c,b;d+=d+b
```

**How it works**

- Split off the doubling: t(n) = a(n+1) − 2a(n) has generating function
  A(x)(1 − 2x)/x = 1/(1 − 2x + x² − x³), so t = 1, 2, 3, 5, 9, 16, 28, …
  obeys t(n) = 2t(n−1) − t(n−2) + t(n−3) with t(−1) = t(−2) = 0. The
  program keeps d = a(n) and updates it with `d+=d+b`, where b = t(n).
- t needs three numbers of state, and the companion form
  `b,c,e=2*b-c+e,b,c` is 17 bytes. Instead `a` holds the running total
  1 + t(0) + … + t(n−1) and `c` holds t(n−1); then
  t(n) = a − t(n−2), which is `a+=b;b,c=a-c,b` (14 bytes). This identity
  is the summed recurrence: u(n) = 1 + Σ_{k<n} t(k) − t(n−2) − t(n) has
  u(0) = 0 and u(n+1) − u(n) = 2t(n) − t(n−1) + t(n−2) − t(n+1) = 0.
- In loop pass n the state goes in as (a, b, c, d) = (1 + Σ_{k<n−1} t(k),
  t(n−1), t(n−2), a(n)); at n = 0 that is (1, 0, 0, 0), which needs
  only two groups in the first line.
- `print(…)` sits in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never stops. All arithmetic is on Python
  integers, so every term is exact.

**Notes**

- The direct recurrence with a power of two, `a=b=c=0;p=1` +
  `while[print(a)]:a,b,c=2*a-b+c+p,a,b;p*=2`, is 52 bytes; with `2**n` and
  a counter it is 53.
- A000253(n) counts binary strings of length n + 2 containing 010
  (Holger Petersen, in the OEIS entry). The automaton for 010 gives
  `e=o=1;z=2;d=0` + `while[print(d)]:d+=d+o;e,z,o=e+o,e+z,z`, also 52
  bytes: same update length, but its start state (1, 2, 1, 0) needs three
  groups.
- The 49-byte form came out of a brute-force search over in-place
  updates (`x+=y`, `x-=y`, `x=y-x`, …), two- and three-target tuple
  assignments with short right-hand sides, and one `d+=d±…` doubling
  step, with the start state solved exactly from the first terms. No
  in-place-only program with at most 22 bytes of updates exists in that
  space, and nothing under 49 bytes turned up. Printing a walrus instead,
  `while[print(d:=d+d+b)]:a+=b;b,c=a-c,b`, is also 49.
- Python 3.12 refuses to convert integers of more than 4300 digits to
  text, so `print` raises near n = 14280 (a limit of the interpreter, not
  of the method). The b-file has 1001 terms (n = 0 to 1000) and the whole
  of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000253), CC BY-SA 4.0.
