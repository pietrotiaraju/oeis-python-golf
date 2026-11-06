# A000433

> n written in base where place values are positive cubes.
> — [OEIS A000433](https://oeis.org/A000433)

Offset 0: 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, …

### Python 3 — 114 bytes

```python
n=0
while 1:
 r=n;s='';k=1
 while k**3<=n:k+=1
 while k>1:
  k-=1;d,r=divmod(r,k**3);s+=str(d)
 print(s or 0);n+=1
```

**How it works**

Use greedy division by the cube place values in descending order.
First locate the largest cube at most n, then divmod supplies each
digit and the remainder for the lower places. The largest possible
digit is 7, at the units place, so ordinary decimal digit strings
encode every quotient. The empty representation of zero prints as 0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10001 terms in 60 s; the official b-file contains 10001 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000433), CC BY-SA 4.0.
