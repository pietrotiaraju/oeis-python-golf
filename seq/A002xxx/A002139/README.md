# A002139

> Shuffling 2n cards.
> — [OEIS A002139](https://oeis.org/A002139)

Offset 1: 2, 3, 5, 12, 14, 11, 13, 20, 72, 19, 42, 132, …

The entry's title is only "Shuffling 2n cards"; its reference is S. W.
Golomb, *Permutations by cutting and shuffling* (SIAM Review, 1961). The
data are the order of a perfect out-shuffle of 2n cards followed by moving
the top card to the bottom: this reading reproduces all 5000 terms of the
b-file, and the entry's formula (Sean A. Irvine), which goes through the
multiplicative order of 2 mod 2n − 1, describes the same permutation.

### Python 3 — 144 bytes

```python
from math import*
N=0
while 1:
 N+=2;L=1;s=set()
 for x in range(N):
  k=0
  while{x}-s:s|={x};x=(2*x-(2*x<N))%N;k+=1
  L=lcm(L,k)or L
 print(L)
```

**How it works**

- **The permutation.** Number the positions 0, …, 2n−1 from the top. The
  out-shuffle interleaves the two halves with the top card staying on
  top: the card at position c < n goes to 2c and the card at c ≥ n to
  2c − 2n + 1. Moving the top card to the bottom then lowers every
  position by 1 mod 2n. Together: c ↦ 2c − 1 for c < n (0 ↦ 2n − 1) and
  c ↦ 2c − 2n for c ≥ n, which is `(2*x-(2*x<N))%N` with N = 2n.
- **Its order.** a(n) is the least number of repetitions that restores
  the deck, the lcm of the cycle lengths. For every start x the loop
  follows the map, marking positions in `s` and counting the steps in k,
  so each cycle is walked once; a start that is already marked gives
  k = 0, and `lcm(L,k)or L` then keeps L (math.lcm with 0 is 0).

**Notes**

- Integer arithmetic only, so it is correct for every n; a term costs
  about 2n steps.
- Moving the bottom card to the top instead gives the same orders.
- The b-file has 5000 terms; the bar is 3500 terms in 60 s, about 22 s
  here.

## First 450 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only the first 450 terms have to arrive in time.

### Python 3, 450 terms — 128 bytes

```python
from math import*
N=0
while 1:
 N+=2;L=1
 for x in range(N):
  y=x;k=1
  while(y:=(2*y-(2*y<N))%N)-x:k+=1
  L=lcm(L,k)
 print(L)
```

**How it works**

- Same permutation, but no marks: from every start x it follows the map
  until it is back at x, and takes the lcm of all these cycle lengths
  (each cycle is walked once per element). Every k is at least 1, so
  `lcm(L,k)` needs no guard.

**Limits**

- A term costs about 2n times the cycle length, up to about 4n² steps:
  here the 450th term arrives after about 19 s, far short of the main
  bar of 3500.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 144 | first entry |

**Python 3, 450 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-20 | 128 | first entry: walk the cycle of every element, no marks |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002139), CC BY-SA 4.0.
