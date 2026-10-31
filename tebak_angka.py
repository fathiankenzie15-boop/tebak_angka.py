

def main():
    print("=" * 40)
    print("  PERMAINAN TEBAK ANGKA")
    print("=" * 40)
    print("Aturan: Tebak angka antara 1 sampai 50.")
    print("Kamu hanya punya 5 kesempatan!")
    print("=" * 40)

    while True:
        angka_rahasia = random.randint(1, 50)
        max_percobaan = 5
        percobaan = 0
        menang = False

        print("\n--- Permainan Dimulai ---")

        while percobaan < max_percobaan:
            try:
                tebakan = int(input(f"Percobaan ke-{percobaan + 1}/{max_percobaan}. Tebakanmu: "))
            except ValueError:
                print("Input harus berupa angka! Coba lagi.")
                continue

            percobaan += 1

            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"\nSelamat! Angka {angka_rahasia} berhasil ditebak dalam {percobaan} percobaan.")
                menang = True
                break

        if not menang:
            print(f"\nYah, kesempatan habis. Angkanya adalah {angka_rahasia}.")

        main_lagi = input("\nMau main lagi? (y/n): ").lower()
        if main_lagi != 'y':
            print("Terima kasih sudah bermain!")
            break

if __name__ == "__main__":
    main()