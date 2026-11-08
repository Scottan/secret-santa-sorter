# secret-santa-sorter

Command line app for matching people up for secret santa

Run with:
```
python secret_santa_sorter.py <config_file>.json [-v]
```

Where higher verbosity can be set with `-v`. For example:

```
python secret_santa_sorter.py example_family_2025.json -v
```

Matching is controlled in the `do_not_match` object in the config json file
(see `example_family_2025.json` for an example):
```
    "do_not_match": {
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

Then a message will be written into a text file explaining who each person should get a present for. The text for the message is contained line-by-line in the `message` object
in the config json file. The key words `getter` will be replaced with the name of
the person who is getting the present, and `reciever` will be replaced with the name
of the person will be recieving a present from `getter`. For example, from
`example_family_2025.json`:

```
    "message": [
        "Dear {getter}, \n",
        "This year, you need to get a present for...\n",
        "{reciever} !!!\n",
        "Please keep the contents of this file secret.\n\n",
        "Merry Christmas!",
        "Secret Santa Xx"
    ]
```

As long as the person who runs this app doesn't read hte generated text files, nobody will know who everyone else got. I usually just attach the text files to emails without opening and send out in the runup to Christmas.

There's probably some clever way of saving those text files so they can only be viewed by the person theyre addressed to. I can't be bothered.
I know it's based on trust, but this is just a silly script I wrote for doing secret santa with my family. 

If you cheat and look you're only cheating yourself!

:)

scottan
