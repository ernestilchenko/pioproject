<div align="center">
<h1>🎓 PIO Project</h1>

[Light Theme](#) | [Dark Theme](#)

<style>
  /* Этот стиль будет работать только на GitHub Pages */
  :root[data-theme="light"] {
    --bg-color: #ffffff;
    --text-color: #24292e;
    --link-color: #0366d6;
    --border-color: #e1e4e8;
  }

  :root[data-theme="dark"] {
    --bg-color: #0d1117;
    --text-color: #c9d1d9;
    --link-color: #58a6ff;
    --border-color: #30363d;
  }

  body {
    background-color: var(--bg-color);
    color: var(--text-color);
  }

  a {
    color: var(--link-color);
  }

  .theme-switch {
    position: fixed;
    top: 20px;
    right: 20px;
    padding: 10px;
    border-radius: 50%;
    cursor: pointer;
    z-index: 1000;
  }
</style>

<button onclick="toggleTheme()" class="theme-switch" title="Toggle theme">
  🌓
</button>

<script>
  function toggleTheme() {
    const root = document.documentElement;
    const currentTheme = root.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
  }

  // Установка начальной темы
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
</script>

Platforma edukacyjna z możliwością zarządzania kursami, harmonogramem i profilami użytkowników.

![Platform Preview](images/img.png)
</div>

## 📋 Spis treści
- [Instalacja](#instalacja)
- [Uruchomienie](#uruchomienie)
- [Dostępne endpointy](#dostępne-endpointy)
- [Funkcjonalność](#funkcjonalność)
- [Screenshots](#screenshots)
- [Autorzy](#autorzy)

## 🚀 Instalacja

### Wymagania wstępne
- Python 3.12.0
- Git

### Kroki instalacji

1. **Pobierz i zainstaluj Python**
   - Odwiedź [oficjalną stronę Python](https://www.python.org/downloads/release/python-3120/)
   - Pobierz i zainstaluj odpowiednią wersję dla swojego systemu

2. **Przygotuj środowisko projektu**
   ```bash
   # Utwórz katalog projektu
   mkdir pioproject
   cd pioproject

   # Utwórz wirtualne środowisko
   python3.8 -m venv env

   # Aktywuj środowisko (Linux/MacOS)
   source env/bin/activate
   # LUB dla Windows
   .\env\Scripts\activate
   ```

3. **Sklonuj repozytorium**
   ```bash
   git clone https://github.com/ernestilchenko/pioproject.git
   ```

4. **Zainstaluj zależności**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Uruchomienie

Aby uruchomić serwer deweloperski:
```bash
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: `http://127.0.0.1:8000/`

## 🛣 Dostępne endpointy

| Endpoint | Opis |
|----------|------|
| `/register/` | Rejestracja nowego użytkownika |
| `/login/` | Logowanie do systemu |
| `/favorites/` | Lista ulubionych kursów |
| `/favorites/add/<course_id>/` | Dodawanie kursu do ulubionych |
| `/courses/` | Lista wszystkich kursów |
| `/courses/delete_course/<course_id>/` | Usuwanie kursu |
| `/harmonogram/` | Zarządzanie harmonogramem |
| `/course/<course_id>/` | Szczegóły kursu |
| `/admin/` | Panel administracyjny |

## 💡 Funkcjonalność

### Panel Administratora
- **URL**: `http://127.0.0.1:8000/pio/admin`
- Zarządzanie bazą danych
- Dodawanie i edycja kursów
- Zarządzanie użytkownikami

### Modele Danych
1. **Użytkownicy**
   - Login i hasło (szyfrowane)
   - Dane osobowe
   - Uprawnienia

2. **Profile użytkowników**
   - Customizacja avatara
   - Dane specyficzne dla typu użytkownika

3. **Harmonogram**
   - Powiązanie z kursami
   - Zarządzanie terminami
   - Przypisywanie do użytkowników/grup

4. **Kursy**
   - Materiały wideo
   - Opisy i dokumentacja
   - System ulubionych

## 📸 Screenshots

<div class="screenshot-container">

### Panel logowania
![Login Page](images/img_1.png)

### Strona rejestracji
![Register Page](images/img_2.png)

### Profil użytkownika
![User Profile](images/img_3.png)

### Lista kursów
![Courses List](images/img_4.png)

### Harmonogram
![Schedule](images/img_5.png)

</div>

## 👥 Autorzy

<div class="authors-container">

[![GitHub](https://img.shields.io/badge/GitHub-ernestilchenko-blue?style=for-the-badge&logo=github)](https://github.com/ernestilchenko)
[![GitHub](https://img.shields.io/badge/GitHub-Ajeszny-blue?style=for-the-badge&logo=github)](https://github.com/Ajeszny)
[![GitHub](https://img.shields.io/badge/GitHub-Andezio-blue?style=for-the-badge&logo=github)](https://github.com/Andezion)

</div>

<hr>

<div align="center">
  <small>Made with ❤️ by the PIO Team</small>
</div>
