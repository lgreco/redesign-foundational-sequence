# A further refactor of the word-frequency counter from
# better_file_processing.py. That version separated file-reading
# (process()) from searching (search()), but the "did we already see
# this word" if/else still lived directly inside process(), sitting
# next to the file-reading loop. This version pulls that if/else out
# into its own function, record(), so process() does nothing but read
# the file and hand each word off. Still two synchronized lists, still
# a linear search, still no dictionary -- that's next.
#
# Why bother, if the lists and the search are still here? Because
# record() is now the *entire* job of "remember this word," isolated
# in one place. Tomorrow, when dictionaries are introduced, this exact
# function collapses into a single line:
#     word_counts[word] = word_counts.get(word, 0) + 1
# Seeing record() clearly first -- as its own named step -- makes it
# obvious what that one line is doing: find-or-default, then add one.

def search(list, target):
    # idx doubles as both "have we found it" and "where." -1 means
    # "not found," anything else is the exact position of the match.
    idx = -1
    # Guard clause: an empty list has nothing to search, and an empty
    # (falsy) target isn't a real word to search for, so skip the loop
    # entirely instead of running it and finding nothing.
    if list and target:
        i = 0
        while i < len(list) and idx < 0:
            if list[i] == target:
                idx = i
            i += 1
    return idx

def record(contents, frequency, word):
    # Everything process() used to do after calling search() now lives
    # here: decide whether word is new, and either add it or bump its
    # existing count. contents and frequency are passed in rather than
    # being globals, so record() only ever changes the two lists it's
    # handed -- same reasoning as passing filename into process().
    idx = search(contents, word)
    if idx == -1:
        # New word, not previously encountered.
        contents.append(word)
        frequency.append(1)
    else:
        # idx already points straight at the match, so no i-1
        # bookkeeping is needed here.
        frequency[idx] += 1

def process(filename):
    # contents and frequency are local variables here, not
    # module-level globals. That means process() can be called again,
    # on a different file, without one call's leftover word counts
    # bleeding into the next.
    contents = []
    frequency = []
    # Guard clause: skip straight to returning empty results instead
    # of letting open() blow up on a missing/empty filename.
    if filename:
        with open(filename, 'r') as book:
            line = book.readline()
            while len(line) > 0:
                words = line.split()
                for word in words:
                    # One call to record() replaces the whole
                    # search-then-if/else block that used to sit here.
                    # process() no longer needs to know how "have we
                    # seen this word before" gets answered -- only
                    # that record() answers it.
                    record(contents, frequency, word)
                line = book.readline()
    return contents, frequency
