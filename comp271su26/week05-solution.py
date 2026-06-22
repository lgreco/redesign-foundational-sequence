from dynamic_array_solution import DynamicArray

# Solution for Week 5 Assignment: Composing an App Class on Top of Dynamic Array
# Not for students -- posted after the deadline.
#
# FellowshipRoster does not inherit from DynamicArray -- it does not extend
# or override anything from it. Instead, its constructor creates a
# DynamicArray and stores it in self._members. This is composition:
# FellowshipRoster HAS A DynamicArray, rather than IS A DynamicArray.
#
# Every method below calls a method on self._members -- never reaches into
# self._members._underlying or any other private field directly. That
# boundary is exactly what contains, index_of, count, and remove exist to
# protect: FellowshipRoster only ever needs to know the array's public
# contract, never its internal array-and-resizing mechanics.


class FellowshipRoster:

    def __init__(self):
        """Create an empty roster backed by a DynamicArray."""
        self._members = DynamicArray()

    def add_member(self, name) -> None:
        """Add name to the roster.

        Parameters:
        -----------
        name : str
            The member's name. Repeated names are allowed -- a roster can
            list the same name more than once, just like the underlying
            array can store duplicate values.
        """
        self._members.add(name)

    def __str__(self) -> str:
        """String representation for the object.

        Returns:
        --------
        str : the roster's contents, delegating to DynamicArray's own
              __str__ rather than re-building the same formatting here.
        """
        return str(self._members)

    def has_member(self, name) -> bool:
        """Return whether name appears anywhere on the roster.

        Parameters:
        -----------
        name : str
            The name to look for.

        Returns:
        --------
        bool : True if name is on the roster, False otherwise.
        """
        # contains() already does exactly this search on self._members --
        # no need to write a second search loop here. One return statement,
        # at the very end, holds the delegated result.
        found = self._members.contains(name)
        return found

    def how_many(self, name) -> int:
        """Return how many times name appears on the roster.

        Parameters:
        -----------
        name : str
            The name to count.

        Returns:
        --------
        int : number of occurrences, or 0 if name is not on the roster.
        """
        # count() on DynamicArray already returns 0 when the value is
        # absent, so that sentinel case needs no special handling here.
        occurrences = self._members.count(name)
        return occurrences

    def remove_member(self, name):
        """Remove the first occurrence of name from the roster.

        Parameters:
        -----------
        name : str
            The name to remove.

        Returns:
        --------
        any : the removed value, or -1 if name is not on the roster.
        """
        # Two steps, because DynamicArray.remove() works by index, not by
        # value: first locate name with index_of (-1 if absent), then hand
        # that index to remove(). If name is absent, index_of already
        # returns -1, and remove(-1) also returns -1 by its own contract --
        # so the "not found" case falls out without an extra if-check.
        position = self._members.index_of(name)
        removed_value = self._members.remove(position)
        return removed_value


# Part 5: Reflection -- Comparing Week 4 Work with the Solutions
#
# 1. index_of_all -- single exit point
#    The solution scans every filled slot with one for loop and returns
#    "matches" exactly once, after the loop ends. It cannot stop early the
#    way index_of does, because index_of only needs the first match and can
#    return as soon as it sees one, but index_of_all is required to report
#    every match -- stopping early would silently drop later occurrences.
#
# 2. count -- delegation versus a second loop
#    The solution defines count as "return len(self.index_of_all(value))"
#    rather than re-scanning the array. Delegating means there is exactly
#    one place that defines what "match" means. If the definition of match
#    ever changed -- for example, to a case-insensitive comparison -- a
#    second, independent loop would require that change to be made and kept
#    in sync in two places instead of one, which is exactly the kind of
#    duplication the contract is meant to avoid.
#
# 3. Sentinels -- [] versus 0 versus -1
#    An empty list is already an unambiguous "not found" signal because a
#    list with zero elements cannot be confused with any real result --
#    there is no valid "index list" that looks like [] except "no matches."
#    Similarly, 0 is a value count can never produce except when nothing
#    matched, so it needs no separate sentinel. index_of and remove are
#    different: they return a single index, and 0 is a perfectly legitimate
#    index (the first slot), so 0 cannot mean "not found" -- only -1, which
#    is never a valid index, can serve that role unambiguously.
