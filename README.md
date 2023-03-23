# battleRoyale

This program is a simple text-based game called "Battle Royale" where the user inputs two characters with names and designations (e.g. Wizard, Orc, Human, etc.) that will battle each other until one of them dies.

The program generates the characters' initial health and strength points using the health() and strength() functions, which both involve dice rolls. The characters take turns attacking each other, with the difference between their strength points determining how much damage is done to the other character's health points.

The game continues until one of the characters' health points drop to zero or below, at which point the other character is declared the winner. The program outputs the winner's name and the number of rounds it took for the battle to finish.

The program also uses some simple animation by clearing the console screen between each round to create a sense of progress and flow.
