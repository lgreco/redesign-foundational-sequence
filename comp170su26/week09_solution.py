# COMP 170 — Week 9 Assignment: Solutions
# ========================================
# This file contains annotated solutions for Problems 1 and 2 (the
# ATM.py program: withdraw() and deposit(), each wrapped in a retry
# loop with try/except and a limited number of tries) and Problem 3
# (reflection on the Week 8 solutions). Read the comments carefully —
# they explain not just WHAT the code does, but WHY each piece is
# written the way it is.


# =============================================================================
# PROBLEM 1 — Withdrawals with Limited Retries
# =============================================================================
#
# withdraw(amount, balance) keeps the same two guard clauses as the
# Week 8 solutions, in the same order: check the multiple-of-$20 rule
# first, since it doesn't depend on balance at all, then check against
# balance. The one thing that changes from Week 8 is *how* an invalid
# case is reported — each guard clause here raises a ValueError
# instead of printing a message and returning the balance unchanged.
# That's what lets the retry loop around it use try/except: raising
# hands the failure to the caller through the exact mechanism a
# try/except is built to catch, instead of leaving the caller to
# notice (or forget to notice) that the returned balance didn't change.

print("=" * 60)
print("PROBLEM 1 — Withdrawals with Limited Retries")
print("=" * 60)


def withdraw(amount, balance):
    # guard clause: ATMs only dispense $20 bills, so anything that
    # isn't a multiple of $20 is invalid before we even look at balance
    if amount % 20 != 0:
        raise ValueError("amount must be a multiple of $20")
    # guard clause: can't withdraw money that isn't there
    if amount > balance:
        raise ValueError("withdrawal amount exceeds balance")
    return balance - amount


def attempt_withdrawal(balance, max_tries=5):
    """Ask for a withdrawal amount, retrying on bad input.

    Every attempt is wrapped in one try/except that catches two
    different problems at once: int() failing on non-numeric text,
    and withdraw() raising a ValueError because the amount itself is
    invalid — the same except line covers both, since Python doesn't
    care which line inside try raised, only that something did. If
    every try fails, print a gentle message instead of crashing or
    looping forever.
    """
    tries = 0
    while tries < max_tries:
        tries = tries + 1
        try:
            amount = int(input("How much would you like to withdraw? "))
            balance = withdraw(amount, balance)
            print(f"Success! New balance: {balance}")
            return balance
        except ValueError as error:
            print(f"Something's wrong: {error}")
            print("Try again.")
    print("Sorry, you're out of tries. Please visit a teller.")
    return balance


# =============================================================================
# PROBLEM 2 — Cash vs. Cheque Deposits
# =============================================================================
#
# deposit() takes one more piece of information than Week 8's version:
# method, which must be "cash" or "cheque". The two forms are validated
# differently because they're physically different kinds of deposit:
# cash is bills and coins handed to the machine, so a fractional cent
# can't physically exist in that form — a cash deposit must be a whole
# number of dollars. A cheque is just a written amount, and can
# legitimately be for $42.50.
#
# Order of checks follows the same principle as withdraw(): whatever
# doesn't depend on anything else runs first (amount > 0, then method
# is one of the two known forms), then the method-dependent rules, and
# the IRS-threshold warning runs last, since it only matters once the
# deposit is already known to be valid.

print()
print("=" * 60)
print("PROBLEM 2 — Cash vs. Cheque Deposits")
print("=" * 60)


def deposit(amount, balance, method):
    # guard clause: can't deposit nothing or a negative amount
    if amount <= 0:
        raise ValueError("deposit amount must be greater than $0")
    # guard clause: method must be one of the two forms this ATM knows
    if method not in ("cash", "cheque"):
        raise ValueError('method must be "cash" or "cheque"')
    # guard clause: cash can't include cents -- there's no such thing
    # as physically handing an ATM a fraction of a dollar in cash
    if method == "cash" and amount != int(amount):
        raise ValueError("cash deposits cannot include cents")
    # guard clause: even a cheque amount must be valid dollars and
    # cents. Multiplying by 100 turns a valid amount into a whole
    # number of cents; round() undoes tiny floating-point error, and
    # comparing against the un-rounded value catches anything finer
    # than a cent, like 42.503
    if round(amount * 100) != amount * 100:
        raise ValueError("deposit amount must be valid dollars and cents")
    # not an error -- the deposit still happens, just with a warning
    if amount >= 10000:
        print("Warning: deposits of $10,000 or more are reported to the IRS")
    return balance + amount


def attempt_deposit(balance, max_tries=5):
    """Ask for a deposit method and amount, retrying on bad input.

    An invalid method answer counts as a failed try, exactly like an
    invalid amount does -- both are just different ways deposit() can
    raise, and the same try/except catches either one.
    """
    tries = 0
    while tries < max_tries:
        tries = tries + 1
        try:
            method = input("Deposit method (cash/cheque)? ").strip().lower()
            amount = float(input("How much would you like to deposit? "))
            balance = deposit(amount, balance, method)
            print(f"Success! New balance: {balance}")
            return balance
        except ValueError as error:
            print(f"Something's wrong: {error}")
            print("Try again.")
    print("Sorry, you're out of tries. Please visit a teller.")
    return balance


def main():
    balance = 1000
    balance = attempt_withdrawal(balance)
    balance = attempt_deposit(balance)
    print(f"Final balance: {balance}")


if __name__ == "__main__":
    main()


# =============================================================================
# PROBLEM 3 — Reflection on Week 8 Solutions
# =============================================================================
#
# Q1. Printing vs. raising
#
#     Print-and-return leaves it up to the caller to notice that
#     balance didn't change and guess why -- there's no structured
#     signal, just a printed line the caller has to trust was actually
#     about that call. raise stops the function immediately and hands
#     the failure up through the exact mechanism a try/except is built
#     to catch, so the retry loop can react specifically to it, report
#     it once, and immediately ask again. A caller that forgot to
#     check the returned balance against what it expected would sail
#     right past a print-and-return failure with a stale idea of what
#     happened; a raise doesn't allow that.
#
# Q2. Order of checks
#
#     Yes, the reasoning still applies -- it was never about how a
#     check reports failure, only about what the check depends on. The
#     multiple-of-$20 check still doesn't need to know balance at all,
#     so it still belongs first regardless of whether failure is
#     reported with print or raise. Switching to raise changes what
#     happens after a check fails, not which check should run first.
#
# Q3. Where the function stops
#
#     No -- "one return, at the end" assumed every path through the
#     function, valid or invalid, eventually reached the same return
#     statement, because an invalid case just left new_balance
#     unchanged rather than exiting early. Once a guard clause raises
#     instead, an invalid case never reaches any return at all; the
#     function stops immediately at the raise. What replaces "one
#     return, at the end" is closer to "one return on success, one
#     raise per invalid case" -- several exit points, but each one is
#     unambiguous about exactly which situation it represents.
#
# Q4. A warning that isn't an error
#
#     The IRS-notice case isn't invalid input at all -- $12,000 is a
#     perfectly good deposit amount, it just triggers an extra
#     reporting requirement once it clears. raise is reserved for
#     amounts the function refuses to accept; here the deposit is
#     supposed to still succeed, so raising would incorrectly stop a
#     transaction that should go through. print() communicates a side
#     fact about a successful case, not a rejection of it.
#
# Q5. Your choice
#
#     The single thing from the Week 8 solutions that most shaped this
#     week's ATM.py was withdraw()'s own comment admitting that having
#     a function both return a value and print is a "teaching
#     shortcut, not a pattern to copy in general." That's what pushed
#     me toward raise for every guard clause this time, and toward
#     keeping all the user-facing printing inside attempt_withdrawal()
#     and attempt_deposit() instead of inside withdraw() and deposit()
#     themselves -- so withdraw() and deposit() only ever compute a
#     result or raise, and the retry loop is the only place
#     responsible for talking to the user.
