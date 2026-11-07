# A000774

> a(n) = n!*(1 + Sum_{i=1..n} 1/i).
> — [OEIS A000774](https://oeis.org/A000774)

Offset 0: 1, 2, 5, 17, 74, 394, 2484, 18108, 149904, 1389456, 14257440, 160460640, …

### Python 3 — 41 bytes

```python
a=f=n=1
while[print(a)]:a=a*n+f;f*=n;n+=1
```

**How it works**

- With H_n = 1 + 1/2 + ··· + 1/n, a(n) = n!·(1 + H_n), and
  H_n = H_{n−1} + 1/n gives a(n) = n·a(n−1) + (n−1)! (the recurrence in
  the OEIS entry).
- At the top of each round `a` = a(n−1) and `f` = (n−1)!, so `a=a*n+f`
  gives a(n), `f*=n` gives n!, and `n+=1` moves on.
- This is the loop of [A000254](../A000254/) (n!·H_n), which has the same
  recurrence: a(n) is A000254(n) + n!, and adding any multiple of n! keeps
  the recurrence. Here the start a(0) = 1 matches the other two variables,
  so `a=f=n=1` is 2 bytes under A000254's `a=0;f=n=1`.

**Notes**

- The second-order recurrence a(n) = (2n−1)·a(n−1) − (n−1)²·a(n−2) needs
  two terms and the counter and has a longer update.
- Exact integer arithmetic, correct for every n.
- The b-file has 251 terms (up to a(250)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 1558, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000774), CC BY-SA 4.0.
