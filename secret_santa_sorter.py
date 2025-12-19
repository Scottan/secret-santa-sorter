#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:28:22 2018

@author: scottan
"""

import random
import copy
import os
import argparse
import json

MAX_CLASH = 10

def main(config_file, verbose=0):
    """
    Main function to run the secret santa sorter
    """
    config_dict = json.load(open(config_file))
    year = config_dict['year']
    outdir = config_dict['out_root'] + "/" + config_dict['folder_prefix'] + f"{year}/"
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    master_tuple = tuple(config_dict['people_unmatch'].keys())
    unmatch_dict = {}
    pos_match_dict = {}
    match_len_dict = {}

    for p in master_tuple:
        unmatch_dict[p] = _make_unmatched_list(config_dict['people_unmatch'][p], master_tuple, p)
        pos_match_dict[p] = [person for person in master_tuple if person not in unmatch_dict[p]]
        match_len_dict[p] = len(pos_match_dict[p])
        if match_len_dict[p] < 1:
            raise ValueError(f"No possible matches for {p}")

    # Sort master list by number of possible matches
    match_len_dict = dict(sorted(match_len_dict.items(), key=lambda item: item[1]))
    master_list =list(match_len_dict.keys())
    if verbose > 0:
        print(master_list)

    done = False
    iclash = 0

    # Keep repeating until it finds a valid match
    while not done:
        clash = False
        remaining = list(copy.deepcopy(master_tuple))
        matched = []
        matches = {}

        for i, getter in enumerate(master_list):
            if verbose > 0:
                print(f"{i}. Matching {getter}")

            unmatched = unmatch_dict[getter]

            pos_match = [person for person in remaining if person not in unmatched]
            if verbose > 1:
                print(pos_match)

            # Check we have someone to match with
            if len(pos_match) == 0:
                clash = True
                iclash += 1
                break
            else:
                receiver = random.choice(pos_match)
                remaining.remove(receiver)
                if verbose > 1:
                    print(f"{getter} has got {receiver}")

            # Add this to list of receiver
            matched.append(receiver)
            matches[getter] = receiver

        # End of family loop - check whether we have suceeded
        if clash and iclash < MAX_CLASH:
            if verbose > 0:
                print(f"Impossible combo {iclash} - starting again!")
            done = False
        elif clash and iclash >= MAX_CLASH:
            raise RuntimeError(f"Failed to sort after {MAX_CLASH} tries...")
        else:
            print("Sorted!")
            done = True

    # Write results to file
    for key, item in matches.items():
        # write to a text file
        filename = outdir + key + "_SecretSanta.txt"
        message = _write_message(key, item)
        with open(filename, 'w') as out:
            out.write(message)

def _make_unmatched_list(unmatch_list, master_tuple, getter):
    if unmatch_list is None:
        return [getter]
    elif isinstance(unmatch_list, list):
        if len(unmatch_list) == 0:
            return [getter]
        assert all([person in master_tuple for person in unmatch_list]), \
            f"Unknown name(s) {set(x for x in unmatch_list) - set(p for p in master_tuple)} in unmatch list for {getter}"
        assert len(unmatch_list) + 1 < len(master_tuple), f"Impossible to sort, too few options for {getter}"
        return unmatch_list + [getter]
    else:
        raise TypeError(f"people_unmatch paired with {getter} must be a list or None, is {type(unmatch_list)}")

def _write_message(getter, reciever):
    return f"""Dear {getter}, \n
This year, you need to get a present for...\n
    {reciever} !!!\n
Please keep the contents of this file secret
Merry Christmas! Xx
"""


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("config_file", type=str, help="Path to JSON config file")
    argparser.add_argument("--verbose", "-v", action="count", default=0,
                           help="Set the verbosity of the application")
    args = argparser.parse_args()
    main(args.config_file, verbose=args.verbose)
