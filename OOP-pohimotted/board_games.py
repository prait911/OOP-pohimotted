import csv
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional, Callable

class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.games_played: Counter[str] = Counter()
        self.games_won: int = 0

    def add_game(self, game_name: str) -> None:
        self.games_played[game_name] += 1

    def add_win(self) -> None:
        self.games_won += 1

class Game:
    def __init__(self, name: str):
        self.name: str = name
        self.play_counts: int = 0
        self.player_counts: Counter[int] = Counter()
        self.wins: Counter[str] = Counter()
        self.losses: Counter[str] = Counter()
        self.best_scores: Dict[str, int] = {}

    def record_play(self, players: List[str]) -> None:
        self.play_counts += 1
        self.player_counts[len(players)] += 1

    def record_winner(self, winner: str) -> None:
        self.wins[winner] += 1

    def record_loser(self, loser: str) -> None:
        self.losses[loser] += 1

    def record_score(self, player: str, score: int) -> None:
        if player not in self.best_scores or score > self.best_scores[player]:
            self.best_scores[player] = score

class Statistics:
    def __init__(self, filename: str):
        self.players: Dict[str, Player] = defaultdict(lambda: Player(""))
        self.games: Dict[str, Game] = defaultdict(lambda: Game(""))
        self.total_games: int = 0
        self.game_types: Counter[str] = Counter()
        
        self._load_data(filename)
    
    def _load_data(self, filename: str) -> None:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                game_name, player_names, result_type, results = row
                players = player_names.split(',')
                self.total_games += 1
                self.game_types[result_type] += 1
                
                for player in players:
                    self.players[player].add_game(game_name)
                
                self.games[game_name].record_play(players)
                
                if result_type == 'points':
                    scores = list(map(int, results.split(',')))
                    sorted_players = sorted(zip(players, scores), key=lambda x: x[1], reverse=True)
                    self.players[sorted_players[0][0]].add_win()
                    self.games[game_name].record_winner(sorted_players[0][0])
                    self.games[game_name].record_loser(sorted_players[-1][0])
                    for player, score in sorted_players:
                        self.games[game_name].record_score(player, score)
                elif result_type == 'places':
                    ranked_players = results.split(',')
                    self.players[ranked_players[0]].add_win()
                    self.games[game_name].record_winner(ranked_players[0])
                    self.games[game_name].record_loser(ranked_players[-1])
                elif result_type == 'winner':
                    self.players[results].add_win()
                    self.games[game_name].record_winner(results)
    
    def get(self, path: str):
        parts = path.strip('/').split('/')
        if path == '/players':
            return list(self.players.keys())
        elif path == '/games':
            return list(self.games.keys())
        elif path == '/total':
            return self.total_games
        elif parts[0] == 'total' and len(parts) == 2:
            return self.game_types.get(parts[1], 0)
        elif parts[0] == 'player' and len(parts) >= 2:
            player_name = parts[1]
            if player_name not in self.players:
                return None
            if parts[2] == 'amount':
                return sum(self.players[player_name].games_played.values())
            elif parts[2] == 'favourite':
                return self.players[player_name].games_played.most_common(1)[0][0]
            elif parts[2] == 'won':
                return self.players[player_name].games_won
        elif parts[0] == 'game' and len(parts) >= 2:
            game_name = parts[1]
            if game_name not in self.games:
                return None
            if parts[2] == 'amount':
                return self.games[game_name].play_counts
            elif parts[2] == 'player-amount':
                return self.games[game_name].player_counts.most_common(1)[0][0]
            elif parts[2] == 'most-wins':
                return self.games[game_name].wins.most_common(1)[0][0]
            elif parts[2] == 'most-frequent-winner':
                total_wins = self.games[game_name].wins
                if not total_wins:
                    return None
                return max(total_wins.keys(), key=lambda p: total_wins[p] / self.players[p].games_played[game_name])
            elif parts[2] == 'most-losses':
                return self.games[game_name].losses.most_common(1)[0][0]
            elif parts[2] == 'most-frequent-loser':
                total_losses = self.games[game_name].losses
                if not total_losses:
                    return None
                return max(total_losses.keys(), key=lambda p: total_losses[p] / self.players[p].games_played[game_name])
            elif parts[2] == 'record-holder':
                return max(self.games[game_name].best_scores, key=self.games[game_name].best_scores.get, default=None)
        return None
