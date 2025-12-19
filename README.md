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

The keys on the left are all of the people who will be sorted.
The lists of names associated with each person are the people they *cannot* be match with. They also cannot be matched with themselves.
An empty list or `null` means that person can be matched with anyone.
The app will randomly match each person with someone else they can be matched with.

Once everyone has been matched, a message will be written into a text file exaplaining who each person should get a present for.

As long as the person who runs this app doesn't read those text files, nobody will know who everyone else got. I usually just attached the files to emails and send out in the runup to Christmas.

There's probably some clever way of saving those text files so they can only be viewed by the person theyre addressed to. I can't be bothered.
I know that's based on trust, but this is just a silly script I wrote for doing secret santa with my family, so if you cheat and look you're only cheating yourself!

:)

scottan
