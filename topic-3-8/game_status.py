"""Game Status: refactor render_status without changing its behavior."""

def clamp(value, minimum, maximum):
    if value < minimum:
        value = minimum
    elif value > maximum:
        value = maximum
    return value

def make_bar(current, maximum, width):
    filled = current * width // maximum
    bar = "["
    for position in range(width):
        if position < filled:
            bar = bar + "#"
        else:
            bar = bar + "-"
    bar = bar + "]"
    return bar

def meter_line(label, value, maximum):
    shown = clamp(value, 0, maximum)
    bar = make_bar(shown, maximum, 10)
    return label + bar + " " + str(shown) + "/" + str(maximum)

def format_time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    text = str(minutes) + ":"
    if remainder < 10:
        text = text + "0"
    text = text + str(remainder)
    return text

def add_all(scores):
    total = 0
    for score in scores:
        total = total + score
    return total

def find_highest(scores):
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def count_at_least(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count = count + 1
    return count

def choose_level(total):
    if total < 100:
        level = "Rookie"
    elif total < 250:
        level = "Skilled"
    else:
        level = "Expert"
    return level

def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.

    # Bound the two meters.
    # Build two bars. // keeps the whole-number part of the division.
    health_line = meter_line("Health  ", health, 100)
    energy_line = meter_line("Energy  ", energy, 60)

    # Format two durations.
    elapsed_text = format_time(elapsed_seconds)
    best_text = format_time(best_seconds)


    # Summarize the recent scores.
    total = add_all(scores)
    highest = find_highest(scores)
    strong_threshold = 80
    strong_count = count_at_least(scores, strong_threshold)

    # Choose a level from the total.
    level = choose_level(total)

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\n" + health_line
    report = report + "\n" + energy_line
    report = report + "\nLevel:  " + level
    report = report + "\nTime:   " + elapsed_text
    report = report + "\nBest:   " + best_text
    report = report + "\nRecent: total=" + str(total)
    report = report + ", best=" + str(highest) + ", 80+=" + str(strong_count)
    return report


# Supplied demo. This guard keeps the demo from running when tests import the file.
if __name__ == "__main__":
    print(render_status("Nova", 75, 18, 125, 119, [40, 50, 90]))
    print()
    print(render_status("Orion", 110, -4, 61, 60, [80, 80, 90]))
