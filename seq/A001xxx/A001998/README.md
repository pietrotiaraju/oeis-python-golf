# A001998

> Bending a piece of wire of length n+1; walks of length n+1 on a tetrahedron; also non-branched catafusenes with n+2 condensed hexagons.
> — [OEIS A001998](https://oeis.org/A001998)

Offset 0: 1, 2, 4, 10, 25, 70, 196, 574, 1681, 5002, 14884, 44530, 133225, 399310, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a*b)]:a,b=b,3*a-1
```

**How it works**

- A wire of length n + 1 has n bends, each to the left, to the right or
  none (O), so it is a word over {L, R, O} of length n. Turning the wire
  over swaps L and R; reading it from the other end reverses the word and
  also swaps L and R. These generate a group of four maps: the identity,
  the swap, the reversal and the reversed swap. a(n) is the number of
  orbits (the entry's comment: n-tuples of 0, 1, 2 up to reversal and
  x ↦ 2 − x).
- Burnside's lemma: the identity fixes 3^n words, the swap only OO…O, the
  reversal the palindromes, 3^⌈n/2⌉, and the reversed swap the words with
  w_i = swap(w_(n+1−i)), 3^⌊n/2⌋ (an odd n forces an O in the middle). So
  a(n) = (3^n + 3^⌈n/2⌉ + 3^⌊n/2⌋ + 1)/4
  = x(⌊n/2⌋)·x(⌈n/2⌉) with x(k) = (3^k + 1)/2 ([A007051](https://oeis.org/A007051)),
  which is the entry's a(2n) = A007051(n)², a(2n+1) = A007051(n)·A007051(n+1),
  and agrees with its generating function.
- The program keeps a = x(⌊n/2⌋) and b = x(⌈n/2⌉). From n to n + 1 the
  ceiling becomes the floor and the floor grows by one, and
  x(k+1) = 3x(k) − 1, so the pair steps as `a,b=b,3*a-1`. `a=b=1` is
  n = 0, the offset.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The direct `n=0` / `while[print((3**(n//2)+1)*(3**(n-n//2)+1)//4)]:n+=1`
  is 55 bytes. The same swap does [A001444](../A001444/), where the
  turned-over wire counts as new.
- a(n) has about 0.48·n digits, so the 4300-digit limit on printing an int
  stops the program near n = 9000. The b-file has 2093 terms (n = 0 to
  2092); the bar is the whole b-file in 60 s, which takes a fraction of a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001998), CC BY-SA 4.0.
