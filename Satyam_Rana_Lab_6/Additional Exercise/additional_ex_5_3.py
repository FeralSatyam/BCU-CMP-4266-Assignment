def report(q1, q2, q3, *args):
    rev_london = q1 * args[0]
    rev_birmingham = q2 * args[1]
    rev_notingham = q3 * args[2]
    mean_rev = (rev_london + rev_birmingham + rev_notingham) / 3
    mean_qty = (q1 + q2 + q3)/ 3
    print("{:<12}{:<10}{:<10}".format("Store", "Quantity", "Revenue"))
    print("{:<12}{:<10}{:<10}".format("London", q1, rev_london))
    print("{:<12}{:<10}{:<10}".format("Birmingham", q2, rev_birmingham))
    print("{:<12}{:<10}{:<10}".format("Notingham", q3, rev_notingham))
    print("{:<12}{:<10.2f}{:<10.2f}".format("MEAN", mean_qty, mean_rev))

report(299, 100, 100, 65, 65, 54)
    