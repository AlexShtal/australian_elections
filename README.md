
# Australian Elections

Small project of processing ballots


## Description/Examples
### Description
Australian ballots require voters to rank all candidates in order of preference. Initially, only the first candidate on the resulting list is considered, and if one candidate receives more than 50% of the votes, that candidate is considered elected. However, if no candidate receives more than 50% of the votes, all candidates with the lowest number of votes are eliminated. Ballots counted in favor of these candidates are counted in favor of the candidate not eliminated, who is next in order of preference. This process of eliminating the weakest candidates and recounting their ballots in favor of the next candidate in the order of preference who has not been eliminated continues until one candidate has more than 50% of the votes or until all candidates have the same number of votes.

### Example input
Information about ballots stores in txt file in following format.

```
2

3
John Doe
Jane Smith
Jane Austen
1 2 3
2 1 3
2 3 1
1 2 3
3 1 2

4
John Doe
Jane Austen
Jane Smith
Josh Bush
4 1 2 2
4 3 1 3
2 4 3 1
2 1 3 4
1 2 4 3

```

### Example output
```
John Doe
Jane Austen
```
