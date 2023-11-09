import random
import time

# Kullanıcı adı girişi
username = input("Lütfen kullanıcı adınızı girin: ")
print(f"Hoş geldin, {username}! Oyuna başlayalım.")

# Kart veritabanı oluşturma
cards = [
    {
        "name": "Kılıç Darbesi",
        "class": "Saldırı",
        "rarity": "Sıradan",
        "attack": 5,
        "life_steal": 1,
        "defense_reduction": 1
    },
    {
        "name": "Son Şans",
        "class": "Saldırı",
        "rarity": "Sıradan",
        "attack": 6,
        "life_steal": 3,
        "defense_reduction": 3
    },
    {
        "name": "Kılıç Çevirme",
        "class": "Saldırı",
        "rarity": "Sıradan",
        "attack": 8,
        "life_steal": 1,
        "defense_reduction": 1
    },
    {
        "name": "Sarsıcı Çığlık",
        "class": "Saldırı",
        "rarity": "Nadir",
        "attack": 10,
        "life_steal": 5,
        "defense_reduction": 2
    },
    {
        "name": "Kritik Dokunuş",
        "class": "Saldırı",
        "rarity": "Nadir",
        "attack": 10,
        "life_steal": 5,
        "defense_reduction": 2
    },
    {
        "name": "Ejderha Ateşi",
        "class": "Saldırı",
        "rarity": "Eşsiz",
        "attack": 15,
        "life_steal": 8,
        "defense_reduction": 3
    },
    {
        "name": "Ejderha Kükremesi",
        "class": "Saldırı",
        "rarity": "Eşsiz",
        "attack": 15,
        "life_steal": 8,
        "defense_reduction": 3
    },
    # Diğer kartlar burada listelenebilir
    # ...
]

# Rastgele kart seçimi
def select_random_card(cards):
    rand = random.randint(1, 10)
    if rand <= 7:
        return random.choice([card for card in cards if card['rarity'] == "Sıradan"])
    elif rand <= 9:
        return random.choice([card for card in cards if card['rarity'] == "Nadir"])
    else:
        return random.choice([card for card in cards if card['rarity'] == "Eşsiz"])

# Kullanıcı seçimini isteme
def get_player_choice(cards):
    print("Lütfen aşağıdaki kartlardan birini seçin:")
    for i, card in enumerate(cards, start=1):
        print(f"{i}. Kart İsmi: {card['name']}")

    while True:
        try:
            choice = int(input("Seçiminizi yapın (1, 2, 3, ...): "))
            if 1 <= choice <= len(cards):
                return cards[choice - 1]
            else:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        except ValueError:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

# Oyuncu ve bilgisayarın can puanları
player_health = 100
computer_health = 100

# Oyuncunun kart eli
player_hand = []
max_hand_size = 3

# Başlangıçta oyuncunun kart elini doldurma
for _ in range(max_hand_size):
    player_hand.append(select_random_card(cards))

# Oyun döngüsü
while player_health > 0 and computer_health > 0:
    # Sıranın rastgele belirlenmesi
    turn = random.choice(["player", "computer"])

    # Rastgele olarak belirlenen oyuncunun hamle süresi
    max_time = 30
    current_time = 0

    while current_time < max_time:
        if turn == "player":
            print("Başlama sırası senin, ilk hamleni iyi düşün")
            if not player_hand:
                for _ in range(max_hand_size):
                    player_hand.append(select_random_card(cards))
            player_choice = get_player_choice(player_hand)
            player_hand.remove(player_choice)
            print(f"Rakibin seçtiği kart: {player_choice['name']}")
            computer_health = max(0, computer_health - player_choice['attack'])
            print(f"Kalan canın: {player_health}")
            print(f"BRakibinin kalan canı: {computer_health}")
            print("----------------------------------")
            current_time += 1
            turn = "computer"
            if player_health <= 0 or computer_health <= 0:
                break
        else:
            print("Rakibin sırası")
            time.sleep(1)  # Saniyelik bir bekleme süresi eklenmiştir, istenilen süre ayarlanabilir.
            if not player_hand:
                for _ in range(max_hand_size):
                    player_hand.append(select_random_card(cards))
            computer_choice = select_random_card(cards)
            print(f"Rakibinin seçtiği kart: {computer_choice['name']}")
            player_health = max(0, player_health - computer_choice['attack'])
            print(f"Kalan canın: {player_health}")
            print(f"Rakibinin kalan canı: {computer_health}")
            print("----------------------------------")
            current_time += 1
            turn = "player"
            if player_health <= 0 or computer_health <= 0:
                break

    if player_health <= 0 or computer_health <= 0:
        break

# Oyuncu ve bilgisayarın can puanlarının kontrol edilmesi
if player_health <= 0:
    print("Rakinin sana acımadı!")
else:
    print("Bir böcek gibi ezdin!")
