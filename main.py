import datetime
import operation
import counter

account = counter.Counter()
account.load_from_file("database.txt")
account.add_operation(operation.Operation(datetime.datetime.today(), "work", 228))

for k in account.get_operations():
    k.print_operation()
