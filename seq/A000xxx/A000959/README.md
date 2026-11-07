# A000959

> Lucky numbers.
> — [OEIS A000959](https://oeis.org/A000959)

Offset 1: 1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, …

### Python 3 — 83 bytes

```python
L=[];m=0
while 1:
 m+=1;q=m
 if all(q%k*(q:=q-q//k)for k in L):print(m);L+=[m+1//m]
```

**How it works**

- Each m is tested by following its position through the sieve. q is the
  position of m (counted from 1) in the list left so far. A step with k
  removes the positions divisible by k, and a survivor at position q moves
  to q − ⌊q/k⌋.
- The steps are k = 2 (every second number), then 3, 7, 9, 13, …, the lucky
  numbers after 1. `L` holds exactly these: 1 goes in as `m+1//m` = 2 and
  every later lucky number as itself. All the steps that can still remove m
  use lucky numbers < m, so `L` is complete when m is tested.
- `q%k*(q:=q-q//k)` is 0 exactly when the step removes m (the new q is
  always ≥ 1), so `all(...)` says whether m survives. Steps with k > q
  remove nothing and only cost time.

**Notes**

- No list is sieved: L grows by one entry per term. Each lucky number goes
  through all of L, so n terms cost about n² steps: 18800 terms in 60 s.
- The b-file has 200000 terms; the bar is 14000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000959), CC BY-SA 4.0.
