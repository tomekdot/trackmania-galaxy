# Jak wspomóc projekt (Contributing)

Dziękujemy za zainteresowanie rozwojem ManiaPlanet Wiki! Ten projekt jest otwarty i tworzony przez społeczność.

## Jak zacząć

1. Zaloguj się na swoje konto GitHub.
2. Wejdź do wybranego artykułu lub strony, którą chcesz edytować.
3. W prawym górnym rogu podglądu dokumentu znajdziesz ikonę **ołówka** lub przycisk **"Edit on GitHub"**. Otworzy to wbudowany edytor GitHuba.
4. Wpisz swoje zmiany w formacie pliku Markdown (`.md`).
5. U dołu strony pojawi się formularz, w którym możesz zaproponować **Commit** z krótkim opisem tego, co i dlaczego zmieniałeś.
6. Zatwierdź swoje zmiany klikając **"Propose changes"**, co utworzy tzw. `Pull Request`. Twoje zgłoszenie zostanie sprawdzone i po akceptacji (Merge) pojawi się niezwłocznie na oficjalnej stronie Wiki!

## Formatowanie
- Projekt oparty jest o narzędzie Just The Docs z użyciem plików `.md` (Markdown).
- Zachowaj ogólny styl i pisz jak najbardziej czytelnie, unikaj wulgaryzmów.
- Na początku nowych plików pamiętaj o dodaniu odpowiedniego nagłówka (tzw. "Front Matter"). Np:

```yml
---
layout: default
title: Mój nowy artykuł
nav_order: 10
---
```

## Automatyczne budowanie
Przy każdym wprowadzonym Pull Requestcie lub bezpośredniej zmianie na gałęzi `main`, GitHub Actions zadba o to, by przebudować i pokazać nową wersję strony. Strona aktualizuje się zazwyczaj do około 2 minut na: `https://[TwojaNazwa].github.io/[Repozytorium]` (zmieni się zgodnie z aktualnie ustawionym `baseurl` dla adresu repozytorium GitHub.io).

Dziękujemy za twój wkład!
