# NCAIC 2022 Template

Template for NCAIC 2022 Contest Competitors.

## Add Team Information

Checkout [`team.json`](./team.json)

```json
{
    "register": false,
    "name": "Team Name",
    "org": "Team Organization",
    "members": [
        {
            "name": "Member 1's Name",
            "email": "Member 1's Email",
            "github": "Member 1's Github Username"
        },
        {
            "name": "Member 2's Name",
            "email": "Member 2's Email",
            "github": "Member 2's Github Username"
        }
    ],
    "program": "path/to/your/agent/source"
}
```

The first member of the team is the team leader.

For every member, the only required field is `name`, and the other fields are optional.

## Write Your Agent Code

Your code can be anywere in the repository, but you must set the `program` field to the path of your agent source code file.


## Register for the contest

Set the `register` field to `true` in `team.json` to register for the contest.
