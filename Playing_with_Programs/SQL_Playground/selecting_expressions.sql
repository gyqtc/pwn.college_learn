WITH RECURSIVE seq(i) AS ( SELECT 1 UNION ALL SELECT i+5 FROM seq WHERE i+5 <= (SELECT length(content) FROM flags)) SELECT substr(content, i, 5) AS part FROM flags, seq;
