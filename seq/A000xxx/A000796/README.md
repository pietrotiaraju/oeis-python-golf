# A000796

> Decimal expansion of Pi (or digits of Pi).
> — [OEIS A000796](https://oeis.org/A000796)

Offset 1: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, …

### Python 3 — 85 bytes

```python
q=t=l=1;y=4
while y%t<q or[print(y//t),q:=q*10,y:=y%t*10]:l+=2;y=y*l-2*q;q*=l//2;t*=l
```

**How it works**

This is Jeremy Gibbons' unbounded spigot ("Unbounded Spigot Algorithms for
the Digits of Pi", *Amer. Math. Monthly* 113 (2006)), squeezed down to three
integers and a counter.

- The series is π = 2 + 1/3·(2 + 2/5·(2 + 3/7·(2 + …))), the Euler transform
  of Leibniz's series. Step k is the map x ↦ 2 + k·x/(2k + 1), with
  `l` = 2k + 1 and `l//2` = k.
- The state is an increasing map f(x) = (q·x + y − 4q)/t, chosen so that the
  digits still to be printed are those of f(x), where x is the value of the
  rest of the series. Every tail 2 + k/(2k+1)·(2 + …) lies between π and 4
  (each factor k/(2k+1) is below 1/2, and they grow with k), so x is in
  [3, 4]. At the start f is the identity: q = t = 1, y = 4.
- y/t is f(4) and (y − q)/t is f(3). When `y%t>=q`, subtracting q does not
  cross a multiple of t, so f(3) and f(4) have the same integer part
  n = `y//t`, and so does f(x): n is certainly the next digit. Printing it
  replaces f by 10·(f − n), which is `q*=10` and y = 10·(y − n·t) =
  `y%t*10`.
- Otherwise the next term goes in: f(x) becomes f(2 + k·x/l), that is
  q → q·k, t → t·l and y → y·l − 2q (the new y is (2q + y − 4q)·l + 4q·k,
  and 4k = 2l − 2). The interval f([3, 4]) then gets more than 2 times
  narrower.
- Both steps sit in one `while`: the condition prints a digit when it is
  safe (the list is non-empty, so the condition is always true, as in
  [A000045](../A000045/)) and the body always takes in one more term. A term
  is worth about log₁₀ 2 ≈ 0.3 digits, so one chance to print per term is
  enough to keep up.

**Notes**

- It is exact: every digit is printed only once f(3) and f(4) agree on it,
  and since π is irrational, f(x) is never a whole number, so the interval
  always ends up inside one digit and no digit is held back forever.
- Each printed value is a single digit, so the 4300-digit int-to-str limit of
  Python 3.11+ never applies. The integers grow by about log₁₀(2k + 1) digits
  per term: by digit 20 000 (about 66 000 terms) t has some 300 000 digits,
  and the program slows down roughly quadratically.
- The whole b-file (20 000 digits) prints in 15–20 s; the bar is the whole
  b-file in 60 s.
- Halving the tail, π = 2u with u = 1 + 1/3·(1 + 2/5·(1 + …)) and u in
  [1, 2], is also 85 bytes: `t=l=1;q=2;y=4` +
  `while y%t<q or[print(y//t),q:=q*10,y:=y%t*10]:l+=2;y=y*l-q;q*=l//2;t*=l`.
  The update loses `2*`, the start pays it back.
- With an `if` instead of the list, `q=t=l=1;y=4` + `while l:=l+2:` +
  ` if y%t>=q:print(y//t);q*=10;y=y%t*10` + ` y=y*l-2*q;q*=l//2;t*=l` is
  87 bytes. Gibbons' own version, with separate n and k and the test
  `4*q+r-t<n*t`, is about 165.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000796), CC BY-SA 4.0.
