# A000472

> a(n) = a(n-1)^2 + (a(n-2) + 1)*(a(n-1) - a(n-2)^2).
> — [OEIS A000472](https://oeis.org/A000472)

Offset 1: 2, 5, 28, 802, 643726, 414383582242, 171713753231982206218246, 29485613049014079571725771288849499850026859242, 869401376876189366008603664962520703088459987798626788985159595026678611496977754082506135886, 755858754114213857656603113420675810884838006478829986130891722713470138443059286330596770611262539256240920756092672154727041680815771409333728105993616009678903886154302740105437684242, …

### Python 3 — 41 bytes

```python
a=2;d=1
while[print(a)]:a,d=a*a+d,d*(a+1)
```

**How it works**

- Write A_n for a sequence term and put d_n=A_(n+1)−A_n².
  The defining recurrence says
  d_n=(A_(n−1)+1)·d_(n−1), or equivalently
  d_(n+1)=(A_n+1)·d_n.
- At a print, a=A_n and d=d_n. The simultaneous update
  `a,d=a*a+d,d*(a+1)` therefore supplies A_(n+1) and d_(n+1)
  using only the two old values.
- The seeds A_1=2 and A_2=5 give d_1=5−2²=1. The first
  states are (2,1), (5,3), (28,18), (802,522), explaining
  the first four outputs without storing two preceding terms.
- `[print(a)]` stays true after printing, so the update runs
  indefinitely as long as the interpreter can handle the integers.

**Notes**

- Exact integer arithmetic. The difference state is always positive:
  it starts at 1 and is multiplied by a+1>0. Consequently every
  later term exceeds the square of the preceding one.
- Storing the difference reduces the longer defining expression to
  one squaring, one addition and one product, without a separate
  counter or a copy of the previous term.
- Digit counts roughly double each step. The first 14 terms fit
  the default 4300-digit conversion limit of Python 3.11+; the next
  term exceeds it. That interpreter limit is not a correctness failure.
- The b-file has 14 terms (indices 1 through 14). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000472), CC BY-SA 4.0.
