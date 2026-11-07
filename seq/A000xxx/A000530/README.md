# A000530

> Let p(n, s, x) be predicate that number of occurrences of s's in x >= 2*n - the length of the longest sequence of s's in x. Then a(n)=#{x in {0,1}* | x ends in 0 and p(n,0,x) and (there is no prefix y of x such that p(n,0,y) or p(n,1,y))}.
> — [OEIS A000530](https://oeis.org/A000530)

Offset 1: 1, 5, 28, 226, 2077, 20770, 222884, 2529541, …

Write binary words one letter at a time and stop as soon as some letter s
has (number of s's) + (longest run of s's) ≥ 2n. a(n) counts the stopping
words whose last letter is 0 (the prefixes in the name are the proper
ones; the word itself is the first to satisfy the predicate).

### Python 3 — 103 bytes

```python
f=lambda a,r,b,s,t:a+r>m or f(a+1,r+(t==r),b,s,t+1)+f(b+1,s,a,r,1)
m=1
while[print(+f(1,1,0,1,1))]:m+=2
```

**How it works**

- **The state.** For the letter c that the word ends with, `a` is its
  count, `r` its longest run and `t` the length of the final run; `b` and
  `s` are the count and longest run of the other letter. Appending c gives
  a + 1 and t + 1, and the longest run grows to t + 1 exactly when t = r
  (always t ≤ r), so `r+(t==r)` is max(r, t+1). Appending the other letter
  makes it the current one, with count b + 1, final run 1 and longest run
  max(s, 1).
- **No 0/1 bookkeeping.** Complementing every letter maps stopping words
  to stopping words, so as many of them end in 0 as in 1, and as many
  start with 0 as with 1. a(n) is therefore the number of stopping words
  that start with a given letter, and the program never records which
  letter is 0: `f(1,1,0,1,1)` is the one-letter word.
- **The stop test.** `m` is 2n − 1 (`m+=2`), so `a+r>m` is a + r ≥ 2n.
  Only the letter just appended can newly pass it, since the other
  letter's numbers did not change. A stopping word returns `True`, which
  counts as 1 in the sums. Before stopping both counts are below 2n, so
  every word has fewer than 4n letters and the recursion ends.
- **The start value s = 1.** The second letter has not appeared yet, but
  storing its longest run as 1 makes max(s, 1) just `s` when it first
  appears; `s` is never tested before that, because the test only looks
  at the current letter.
- **`+f`.** For n = 1 the one-letter word already stops and `f` returns
  `True`; unary `+` turns it into 1.

**Notes**

- Other versions that print the same terms: with
  `from functools import*` and a fresh cache for every n,
  `while[print(+(f:=cache(lambda a,r,b,s,t:…))(1,1,0,1,1))]:m+=2`:
  134 bytes, and 31 terms in 60 s here (the cache must not outlive `m`);
  the previous program, a memoized walk over both letters with an explicit
  0/1 flag: 240 bytes.
- A brute force over all binary words straight from the definition
  agrees for n ≤ 4. Exact integer arithmetic, so the program is right for
  every n.
- The calls form a full binary tree whose leaves are the a(n) stopping
  words, so a(n) costs 2a(n) − 1 calls: the whole b-file prints in about
  2 s here, and a(9) = 29995812 follows after about 25 s. That value
  matches the lower bound "a(9) ≥ 29995812 (probably equal to this value)"
  in the entry's comment; the memoized version agrees.
- The b-file has 8 terms (up to a(8)); the bar is the whole b-file in 60 s.
- The recursion depth is the word length, under 4n, far below Python's
  limit for any n that finishes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 240 | first entry |
| 2026-11-07 | Python 3 | 103 | complement symmetry: no 0/1 flag, no memo |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000530), CC BY-SA 4.0.
