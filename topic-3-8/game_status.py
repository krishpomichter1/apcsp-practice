"""Game Status: refactor render_status without changing its behavior."""

def clamp(value, minimum, maximum):
    if value < minimum:
        value = minimum
    elif value > maximum:
        value = maximum
    return value

def render_status(name, health, energy, elapsed_seconds, best_seconds, scores):
    # Keep this function's name, parameters, and returned report.
    # Add your own helper functions above it.

    # Bound the two meters.
    shown_health = clamp(health, 0, 100)
    shown_energy = clamp(energy, 0, 60)


    # Build two bars. // keeps the whole-number part of the division.
    health_filled = shown_health * 10 // 100
    health_bar = "["
    for position in range(10):
        if position < health_filled:
            health_bar = health_bar + "#"
        else:
            health_bar = health_bar + "-"
    health_bar = health_bar + "]"

    energy_filled = shown_energy * 10 // 60
    energy_bar = "["
    for position in range(10):
        if position < energy_filled:
            energy_bar = energy_bar + "#"
        else:
            energy_bar = energy_bar + "-"
    energy_bar = energy_bar + "]"

    # Format two durations.

    elapsed_text = format_duration(elapsed_seconds)
    best_text = format_duration(best_seconds)


    # Summarize the recent scores.
    total = add_all(scores)
    highest = find_highest(scores)
    strong_threshold = 80
    strong_count = count_at_least(scores, strong_threshold)

    # Choose a level from the total.
    if total < 100:
        level = "Rookie"
    elif total < 250:
        level = "Skilled"
    else:
        level = "Expert"

    # Return one report. \n separates its lines; there is no final \n.
    report = "PLAYER: " + name
    report = report + "\nHealth  " + health_bar + " " + str(shown_health) + "/100"
    report = report + "\nEnergy  " + energy_bar + " " + str(shown_energy) + "/60"
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
