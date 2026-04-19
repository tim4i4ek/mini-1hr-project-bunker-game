import random
from time import sleep


INFO_ORDER = ["profession", "health", "hobby", "phobia", "package"]

def run_game(players):
    print("\n🎮 Розпочинаємо раунди гри!")
    round_num = 1
    revealed_info_count = 1

    while len(players) > 2 and revealed_info_count <= len(INFO_ORDER):
        print(f"\n🔁 Раунд {round_num}")
        print(f"🗣 Обговорення (3 сек на гравця для теста)")

        for player in players:
            info = f"{player.name} | "
            parts = []
            if revealed_info_count >= 1:
                parts.append(f"Профессия: {player.profession}")
            if revealed_info_count >= 2:
                parts.append(f"Здоровье: {player.health}")
            if revealed_info_count >= 3:
                parts.append(f"Хобби: {player.hobby}")
            if revealed_info_count >= 4:
                parts.append(f"Фобия: {player.phobia}")
            if revealed_info_count >= 5:
                parts.append(f"Багаж: {player.package}")

            info += " | ".join(parts)
            print(info)
            sleep(1)

        print("🗳 Голосування...")
        sleep(2)


        votes = []
        for player in players:
            vote = random.choice([p for p in players if p != player])
            votes.append(vote)

        expelled = max(votes, key=votes.count)
        players.remove(expelled)
        print(f"❌ Гравець {expelled.name} вигнаний")

        round_num += 1
        revealed_info_count += 1

    print("\n🏆 У БУНКЕРІ залишилися:")
    for p in players:
        print(f"{p.name} | Профессия: {p.profession} | Здоровье: {p.health} | "
              f"Хобби: {p.hobby} | Фобия: {p.phobia} | Багаж: {p.package}")
