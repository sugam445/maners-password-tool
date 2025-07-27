import time

def banner():
    print("\033[1;32m")  # Yeşil renk
    print("="*40)
    print("      Maners Password Tool      ")
    print("="*40)
    print("\033[0m")  # Renk sıfırla

def analyze_password_strength(pw):
    length = len(pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>/?\\|" for c in pw)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "ZAYIF ❌"
    elif score == 3:
        return "ORTA 🟡"
    elif score >= 4:
        return "GÜÇLÜ ✅"

def main():
    banner()
    
    example_pw = "Maners123!"  # Ortalama üstü güçlü bir örnek şifre
    print(f"\nÖrnek Şifre: {example_pw}")
    print("Bu şifrenin gücü kontrol ediliyor...\n")
    time.sleep(1)
    strength = analyze_password_strength(example_pw)
    print(f"[+] Örnek Şifre Gücü: {strength}")
    
    print("\n--- Kendi Şifreni Denemek İster misin? ---")
    user_pw = input("Parolanı gir: ")
    print("Analiz yapılıyor...")
    time.sleep(1)
    result = analyze_password_strength(user_pw)
    print(f"[+] Senin Parola Gücün: {result}")

if __name__ == "__main__":
    main()