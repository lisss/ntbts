```sh
begin;
declare c cursor for select id from grades where g between 90 and 100;
fetch c; -- fetches the first row
fetch c; -- fetches the second row
fetch last c;
```

### pros
- saves memory
- streaming
- can be cancelled
- paging (but not that easy)

### cons
- stateful (you cannot share cursor, you can share a pointer to transaction but it's extremely difficult)
- long transactions