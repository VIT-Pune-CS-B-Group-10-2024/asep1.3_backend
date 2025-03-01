def simulate_radiation_effect(metal, radiation, temperature, intensity):
    # Dummy logic for simulation
    if metal == 'aluminium' and radiation == 'gamma':
        return f"{metal.capitalize()} on {radiation} radiation at {temperature}K and {intensity}W/m² has minimal effect and is suitable for building spacecraft."
    elif metal == 'tin' and radiation == 'alpha':
        return f"{metal.capitalize()} on {radiation} radiation at {temperature}K and {intensity}W/m² has moderate effect and may not be suitable for building spacecraft."
    else:
        return f"{metal.capitalize()} on {radiation} radiation at {temperature}K and {intensity}W/m² has significant effect and is not suitable for building spacecraft."