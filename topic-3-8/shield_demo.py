from game_status import make_bar

# Check empty, partial, and full shield values.
print("Shield  " + make_bar(0, 40, 10) + " 0/40")
print("Shield  " + make_bar(20, 40, 10) + " 20/40")
print("Shield  " + make_bar(40, 40, 10) + " 40/40")