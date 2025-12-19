# secret-santa-sorter
Command line app for matching people up for secret santa

Matching is controlled in the people_unmatch object in the config json file
(see `example_family_2025.json` for an example):
```
    "people_unmatch": {
        "Alice": ["Bob", "Carol", "Frank"],
        "Bob": ["Alice", "Erin", "Dave"],
        "Carol": ["Bob", "Dave"],
        "Dave": [],
        "Erin": ["Carol", "Alice", "Bob", "Dave"],
        "Frank": null
    }
```

The keys on the left are all of the people who need to get presents for each other.
The lists of names associated with each person are the people they *cannot* be matched with. They also cannot be matched with themselves.
An empty list or `null` means that person can be matched with anyone (except themselves).

The app will randomly match each person with someone else they can be matched with, until everyone has someone they should get a present for.
Then a message will be written into a text file exaplaining who each person should get a present for.

As long as the person who runs this app doesn't read those text files, nobody will know who everyone else got. I usually just attach the text files to emails without opening and send out in the runup to Christmas.

There's probably some clever way of saving those text files so they can only be viewed by the person theyre addressed to. I can't be bothered.
I know it's based on trust, but this is just a silly script I wrote for doing secret santa with my family. 

If you cheat and look you're only cheating yourself!

:)

scottan
