import time
import random
from database import professions, hobbies, biology, packages, phobias, situations
import game


players = []
game_start = False

MIN_PLAYERS = 4
MAX_PLAYERS = 12
LOBBY_TIME = 60


class Player:
    def __init__(self, name):
        self.name = name
        self.profession = random.choice(professions)
        self.health = random.choice(biology)
        self.hobby = random.choice(hobbies)
        self.phobia = random.choice(phobias)
        self.package = random.choice(packages)

    def short_info(self):
        return f"{self.name} | Профессия: {self.profession}"

    def full_info(self):
        return (
            f"{self.name}\n"
            f"Профессия: {self.profession}\n"
            f"Здоровье: {self.health}\n"
            f"Хобби: {self.hobby}\n"
            f"Фобия: {self.phobia}\n"
            f"Багаж: {self.package}\n"
        )


def lobby_wait():
    global game_start
    print("🟢 ЛОББІ ГРИ «БУНКЕР»")
    print(f"⏳ Час очікування: {LOBBY_TIME} секунд")
    print(f"👥 Мінімум гравців: {MIN_PLAYERS}\n")

    start_time = time.time()

    while True:
        remaining = LOBBY_TIME - int(time.time() - start_time)
        if remaining <= 0:
            print("\n⏰ Час вийшов")
            break

        print(f"\n⏳ Залишилось {remaining} сек")
        print(f"👥 Гравців: {len(players)}")

        name = input("Ім'я гравця (Enter — чекати): ").strip()
        if name:
            players.append(Player(name))
            print(f"✅ {name} доданий")

        if len(players) >= MIN_PLAYERS:
            print("✅ Мінімум гравців набрано")
            print("▶️ Натисни Y щоб стартувати АБО Enter щоб чекати таймер")
            if input().lower() == "y":
                game_start = True
                print("🚀 Ранній старт")
                break

    if len(players) >= MIN_PLAYERS:
        game_start = True
        print("🚀 Старт після таймера")
    else:
        print("❌ Недостатньо гравців")

def start_game():
    scenario = random.choice(situations)
    bunker_capacity = len(players) // 2

    print("\n🔴 ГРА ПОЧИНАЄТЬСЯ")
    print(f"☢️ Сценарій: {scenario}")
    print(f"🏠 Місць у бункері: {bunker_capacity}\n")

    print("📢 Усі гравці знають ТІЛЬКИ свої професії:\n")
    for idx, p in enumerate(players, 1):
        print(f"{idx} | {p.short_info()}")


    game.run_game(players)


if __name__ == "__main__":
    lobby_wait()
    if game_start:
        start_game()
    else:
        print("❌ Гра не була запущена")
