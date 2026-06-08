import math

# Solutions for Week 3 Assignment: DynamicArray Accessors
# Not for students -- posted after the deadline.
#
# The class below is complete except for five methods marked with pass.
# Your task: implement those methods according to the spec in their comments.
# Do not modify any other method.
# Run this file to check your work against the expected output shown below.


class DynamicArray:

    # Class-level constants: shared by every instance, not stored per object.
    # The underscore signals "internal detail -- not part of the public interface."
    _DEFAULT_RESIZE_BY: float = 2
    _DEFAULT_CAPACITY: int = 4

    def __init__(self, capacity: int = _DEFAULT_CAPACITY, resize_by: float = _DEFAULT_RESIZE_BY) -> None:
        self._underlying: list[int] = list()
        self._capacity: int = capacity
        self._resize_by: float = resize_by
        # Pre-fill every slot with -1 as a sentinel value that marks "nothing stored here."
        # This keeps _underlying at a fixed length equal to _capacity at all times.
        for i in range(self._capacity):
            self._underlying.append(-1)
        # _size tracks stored values; _capacity tracks total slots (including sentinel slots).
        # They start equal to 0 and _DEFAULT_CAPACITY and diverge as elements are added.
        self._size: int = 0

    def __str__(self) -> str:
        if self._size == 0:
            return "nothing to show"
        output = "["
        # Loop up to _size, not _capacity -- sentinel slots are internal and never displayed.
        for i in range(self._size):
            output = output + str(self._underlying[i])
            if i < self._size - 1:
                output = output + ", "
        output = output + "]"
        return output

    def resize(self) -> None:
        # math.ceil guarantees the new capacity is always larger than the old one.
        # int() would round down: int(3 * 1.1) == 3, so the array would never grow.
        temp_capacity = math.ceil(self._resize_by * self._capacity)
        temp = list()
        for i in range(temp_capacity):
            temp.append(-1)
        # Copy only the old _capacity elements -- temp already has sentinels beyond that.
        for i in range(self._capacity):
            temp[i] = self._underlying[i]
        self._underlying = temp
        self._capacity = temp_capacity

    def add(self, value: int) -> None:
        # Resize before writing; after resize there is guaranteed room at index _size.
        if self._size >= self._capacity:
            self.resize()
        # _size is always the index of the next empty slot.
        self._underlying[self._size] = value
        self._size = self._size + 1

    def __len__(self) -> int:
        # Return the number of values stored in this array.
        # Enables: len(da) and truthiness checks like "if da:"
        #
        # Python calls __len__ automatically whenever you write len(da). This is
        # part of the "dunder" (double-underscore) protocol -- a set of special
        # method names Python reserves for built-in operations. Implementing
        # __len__ makes DynamicArray behave like a native Python collection:
        # len(da), "if da:", and "if not da:" all work without any extra effort.
        #
        # The value to return is _size, not _capacity. _size is the guest count
        # (how many values have been stored); _capacity is the room count (how
        # many slots the underlying list has allocated). len() by convention
        # always means "how many items are in this collection."
        return self._size

    def get_size(self) -> int:
        # Return the number of values stored in this array.
        # Same value as __len__; explicit name for readers unfamiliar with dunder methods.
        #
        # __len__ and get_size() return the same number, so why have both?
        # __len__ hooks into Python's built-in protocol (len(), truthiness).
        # get_size() is self-documenting: a reader who has not memorized dunder
        # names understands da.get_size() immediately. Providing both keeps the
        # class easy to use for callers coming from either direction.
        return self._size

    def get_capacity(self) -> int:
        # Return the total number of slots in the underlying array,
        # including empty sentinel slots. This is the hotel room count, not the guest count.
        #
        # _capacity grows each time resize() is called, always ahead of _size.
        # Exposing it through a method (rather than letting callers read _capacity
        # directly) preserves encapsulation: the internal name can change without
        # breaking any caller. A caller who needs this value has a clear, stable
        # name to use -- get_capacity() -- instead of reaching into the object.
        return self._capacity

    def get(self, index: int) -> int:
        # Return the value at position index.
        # Valid positions are 0 through _size - 1 (filled slots only).
        # Return -1 for any index outside that range -- including negative indices.
        # Caution: Python lists accept negative indices natively; you must check for them
        # explicitly, or get(-1) will silently return the last element instead of -1.
        #
        # The bounds check has two parts and both matter:
        #
        #   index < 0
        #       Python lists treat negative indices as counting from the end
        #       (-1 is the last element, -2 is second-to-last, etc.). That
        #       behavior is useful in everyday code, but it is wrong here.
        #       DynamicArray only counts from 0; there is no meaningful position
        #       "-1". Without this check, get(-1) would silently return the last
        #       sentinel slot's value instead of signaling out-of-range.
        #
        #   index >= self._size
        #       _underlying has _capacity slots, but only _size of them hold real
        #       data. Slots from _size to _capacity - 1 are sentinel -1 values.
        #       Allowing access up to _capacity would let callers read sentinel
        #       slots as if they were stored values -- a silent data corruption.
        #       The upper bound is _size, not _capacity and not len(_underlying).
        #
        # If either condition is true, return -1 as the out-of-range signal. The
        # caller asked for something that does not exist; -1 communicates that
        # without raising an exception.
        if index < 0 or index >= self._size:
            return -1
        return self._underlying[index]

    def index_of(self, value: int) -> int:
        # Return the position of the first occurrence of value.
        # Search only filled slots: positions 0 through _size - 1.
        # Do not search sentinel slots -- they all hold -1 and would give false matches.
        # Return -1 if value is not found.
        #
        # range(self._size) produces exactly the filled-slot indices: 0, 1, ...,
        # _size - 1. Using range(self._capacity) or range(len(self._underlying))
        # would include sentinel slots, which all hold -1. If the caller searched
        # for -1, those sentinel slots would incorrectly show up as matches.
        #
        # The loop stops at the first match and returns immediately. That is the
        # correct behavior for "first occurrence": once found, there is no reason
        # to keep scanning. If the loop finishes without finding the value, the
        # function falls through to return -1 -- the agreed-upon signal for
        # "not found."
        #
        # This is a linear search: in the worst case (value absent or at the end)
        # it examines every filled slot. That is unavoidable when the array is
        # unsorted; there is no faster strategy without additional structure.
        for i in range(self._size):
            if self._underlying[i] == value:
                return i
        return -1


if __name__ == "__main__":
    da = DynamicArray()
    da.add(10001)
    da.add(60626)
    da.add(90210)
    print(da)                    # expected: [10001, 60626, 90210]

    print()
    print("__len__ and size/capacity getters")
    print(len(da))               # expected: 3
    print(da.get_size())         # expected: 3
    print(da.get_capacity())     # expected: 4

    print()
    print("get() tests")
    print(da.get(0))             # expected: 10001
    print(da.get(1))             # expected: 60626
    print(da.get(2))             # expected: 90210
    print(da.get(-1))            # expected: -1  (below valid range)
    print(da.get(3))             # expected: -1  (at size, no data there)
    print(da.get(100))           # expected: -1  (well beyond size)

    print()
    print("index_of() tests")
    print(da.index_of(10001))    # expected: 0
    print(da.index_of(60626))    # expected: 1
    print(da.index_of(90210))    # expected: 2
    print(da.index_of(99999))    # expected: -1  (not in array)

    da.add(11111)
    da.add(22222)
    print()
    print("after 2 more adds (triggers resize)")
    print(da)                    # expected: [10001, 60626, 90210, 11111, 22222]
    print(len(da))               # expected: 5
    print(da.get_capacity())     # expected: 8
