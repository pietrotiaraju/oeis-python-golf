# A001592

> Hexanacci numbers: a(n+1) = a(n)+...+a(n-5) with a(0)=...=a(4)=0, a(5)=1.
> — [OEIS A001592](https://oeis.org/A001592)

Offset 0: 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 63, 125, 248, 492, 976, 1936, …

### Python 3 — 43 bytes

```python
l=[0]*5+[1]
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` is a window of six consecutive terms, starting with
  a(0), …, a(5) = 0, 0, 0, 0, 0, 1 (`[0]*5+[1]` is two bytes under
  `0,0,0,0,0,1`). `a,*l=*l,sum(l)` drops the oldest term into `a`, which
  is printed, and appends the sum of the six, the next term (the template
  of [A000078](../../A000xxx/A000078/)).

**Notes**

- The name's indexing, a(n+1) = a(n) + … + a(n−5), is the same recurrence
  shifted by one.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 3362 terms (a(0) to a(3361)); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001592), CC BY-SA 4.0.
