# The reduced energy
def reducedEnergy(energy, ionization_potential):
    return [x / ionization_potential for x in energy]

# the f(E/J), or the ionization reduced cross-section for atoms or molecules
def funcEJ(cross_section, ionization_potential, n_valence): # using joules instead of eV
    return [x * 10**-20 * (ionization_potential * elec_charge)**2 / (n_valence * np.pi * elec_charge**4 * ke**2) for x in cross_section]

# my guessed functions for the data
def funcGuess_1(x, a, b, d):
    return [(a * (y + b)) / (np.pi * y * (y + d)) for y in x]

def funcGuess_2(x, a, b, d, e):
    return [(a * (y + b)) / (np.pi * (y + e) * (y + d)) for y in x]
