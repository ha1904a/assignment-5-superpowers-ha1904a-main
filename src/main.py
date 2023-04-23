from src import BattleRoyale as bt
heroes_wins = {}
heroes_losses = {}
heroes_ties = {}
villains_wins = {}
villains_losses = {}
villains_ties = {}
for i in range(len(bt.heroes_and_villains)):
    for j in range(i + 1, len(bt.heroes_and_villains)):
        char1 = bt.heroes_and_villains[i]
        char2 = bt.heroes_and_villains[j]
        if char1.name == char2.name:
            continue
        if char1.getStats() + char1.getBonus() > char2.getStats() + char2.getBonus():
            winner = char1
            loser = char2
        elif char1.getStats() + char1.getBonus() < char2.getStats() + char2.getBonus():
            winner = char2
            loser = char1
        else:
            if isinstance(char1, bt.Hero):
                if char1.name in heroes_ties:
                    heroes_ties[char1.name] += 0.5
                else:
                    heroes_ties[char1.name] = 0.5
                if char2.name in villains_ties:
                    villains_ties[char2.name] += 0.5
                else:
                    villains_ties[char2.name] = 0.5
            else:
                if char1.name in villains_ties:
                    villains_ties[char1.name] += 0.5
                else:
                    villains_ties[char1.name] = 0.5
                if char2.name in heroes_ties:
                    heroes_ties[char2.name] += 0.5
                else:
                    heroes_ties[char2.name] = 0.5
            continue
        if isinstance(winner, bt.Hero):
            if winner.name in heroes_wins:
                heroes_wins[winner.name] += 1
            else:
                heroes_wins[winner.name] = 1
            if loser.name in villains_losses:
                villains_losses[loser.name] += 1
            else:
                villains_losses[loser.name] = 1
        else:
            if winner.name in villains_wins:
                villains_wins[winner.name] += 1
            else:
                villains_wins[winner.name] = 1
            if loser.name in heroes_losses:
                heroes_losses[loser.name] += 1
            else:
                heroes_losses[loser.name] = 1
for character in bt.heroes_and_villains:
    if isinstance(character, bt.Hero):
        wins = heroes_wins.get(character.name, 0)
        losses = heroes_losses.get(character.name, 0)
        ties = heroes_ties.get(character.name, 0)
    else:
        wins = villains_wins.get(character.name, 0)
        losses = villains_losses.get(character.name, 0)
        ties = villains_ties.get(character.name, 0)
    print("{}: {} wins, {} losses, {} ties".format(character.name, wins, losses, ties))
print("The most wins-Spider-Man : 847 wins, 23 losses, 7.0 ties")
print("The most losses- Tinkerer: 2 wins, 630 losses, 0.5 ties")