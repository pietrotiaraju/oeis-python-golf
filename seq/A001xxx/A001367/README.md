# A001367

> Solution to f(2) = 1, f(n) = sqrt(n) f(sqrt(n)) + n at values n = 2^2^i.
> — [OEIS A001367](https://oeis.org/A001367)

Offset 0: 1, 6, 40, 896, 294912, 23622320128, 119903836479112085504, …

### Python 3 — 35 bytes

```python
m=K=1
while[print(m*K)]:K*=2*K;m+=2
```

**How it works**

- At n = 2^(2^i) the functional equation reads
  a(i+1) = f(2^(2^(i+1))) = 2^(2^i)·a(i) + 2^(2^(i+1)), with a(0) = f(2) = 1.
  By induction a(i) = (2i+1)·2^(2^i − 1): substituting gives
  2^(2^(i+1) − 1)·(2i+1) + 2^(2^(i+1)) = (2i+3)·2^(2^(i+1) − 1).
  (This closed form is also in the entry, by Christian Krause.)
- `m` is the odd factor 2i+1 and `K` the power K(i) = 2^(2^i − 1), which
  obeys K(i+1) = 2·K(i)², so `K*=2*K` updates it with no exponent and no
  counter; the program prints `m*K`.

**Notes**

- The direct closed form `n=0` / `while[print(2*n+1<<2**n-1)]:n+=1` is
  36 bytes, and the entry's recurrence with P = 2^(2^i),
  `a=1;P=2` / `while[print(a)]:a=P*a+P*P;P*=P`, is 38.
- a(i) has about 0.3·2^i digits, so Python's 4300-digit int-to-str limit
  stops the program at a(14) (4933 digits), after printing a(0) to a(13).
- The b-file has 12 terms (a(0) to a(11)); the bar is the whole b-file in
  60 s, which takes no time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001367), CC BY-SA 4.0.
