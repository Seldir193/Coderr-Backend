# Coderr Backend

Das Backend des Coderr-Projekts ist eine RESTful API, die mit **Django** und **Django REST Framework** entwickelt wurde. Es dient als Server, der das Frontend unterstützt, und bietet Funktionen wie Benutzerregistrierung, Login, Verwaltung von Angeboten, Bestellungen und Bewertungen.

## Inhaltsverzeichnis
1. [Überblick](#überblick)
2. [Features](#features)
3. [Technologien](#technologien)
4. [Installation](#installation)
5. [API-Endpunkte](#api-endpunkte)
6. [Hilfsfunktionen](#hilfsfunktionen)
7. [Contributing](#contributing)
8. [Lizenz](#lizenz)

---

## Überblick

Das Coderr-Backend stellt eine Reihe von REST-APIs bereit, die vom Frontend konsumiert werden. Es verwaltet Benutzerprofile, Angebote, Bestellungen und Bewertungen und stellt Daten sowie geschäftsspezifische Logik zur Verfügung.

---

## Features

- **Benutzerregistrierung und Authentifizierung**:
  - Registrieren und Anmelden von Benutzern.
  - Unterschiedliche Rollen: Kunde und Anbieter.
- **Angebotsmanagement**:
  - Erstellen, Aktualisieren und Löschen von Angeboten.
  - Filter- und Suchfunktionalität.
- **Bestellmanagement**:
  - Aufgeben und Verwalten von Bestellungen.
  - Statusverwaltung von Bestellungen.
- **Bewertungen**:
  - Bewertungen erstellen, bearbeiten und löschen.
- **Statistiken**:
  - Statistiken zu abgeschlossenen Bestellungen und Bewertungen.
- **Pagination**:
  - Paginierte Endpunkte für eine bessere Benutzererfahrung.

---

## Technologien

- **Programmiersprache**: Python
- **Framework**: Django, Django REST Framework
- **Datenbank**: SQLite
- **Abhängigkeiten**: 
  - `django-cors-headers`
  - `django-filter`
  - `pillow`
  - Weitere Details in der Datei `requirements.txt`.

---

## Installation

### Voraussetzungen
- Python 3.10+
- Git

### Schritte

1. **Repository klonen**:
   ```bash
   git clone https://github.com/Seldir193/coderr-backend.git
   cd coderr-backend
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**:
   ```bash
   python -m venv env
   source env/bin/activate  # Für Linux/macOS
   env\Scripts\activate     # Für Windows
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Datenbank migrieren**:
   ```bash
   python manage.py migrate
   ```

5. **Entwicklungsserver starten**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The following endpoints are available in the Coderr backend:

### Authentication
- **POST** `/registration/`  
  Registers a new user.
- **POST** `/login/`  
  Logs in a user.

### Profiles
- **GET** `/profile/<int:user_id>/`  
  Retrieves the profile of a specific user.
- **GET** `/profiles/business/<int:user_id>/`  
  Retrieves a specific business profile.
- **GET** `/profiles/business/`  
  Retrieves all business profiles.
- **GET** `/profiles/customer/<int:user_id>/`  
  Retrieves a specific customer profile.
- **GET** `/profiles/customer/`  
  Retrieves all customer profiles.

### Reviews
- **GET** `/reviews/`  
  Retrieves all reviews.
- **GET** `/reviews/<int:pk>/`  
  Retrieves a specific review.
- **POST** `/reviews/`  
  Creates a new review.
- **PUT** `/reviews/<int:pk>/`  
  Updates a specific review.
- **DELETE** `/reviews/<int:pk>/`  
  Deletes a specific review.

### Orders
- **GET** `/orders/`  
  Retrieves all orders.
- **GET** `/orders/<int:order_id>/`  
  Retrieves the details of a specific order.
- **POST** `/orders/`  
  Creates a new order.
- **GET** `/order-count/<int:offer_id>/`  
  Retrieves the count of in-progress orders for a specific offer.
- **GET** `/completed-order-count/<int:user_id>/`  
  Retrieves the count of completed orders for a specific user.
- **GET** `/user/orders/`  
  Retrieves all orders placed by the logged-in user.

### Offers
- **GET** `/offers/`  
  Retrieves all offers.
- **GET** `/offers/<int:id>/`  
  Retrieves the details of a specific offer.
- **POST** `/offers/`  
  Creates a new offer.

### Base Information
- **GET** `/base-info/`  
  Retrieves base information about the system.


## Hilfsfunktionen

Das Backend enthält verschiedene Hilfsfunktionen für unterschiedliche Zwecke:

- **`profile_helpers.py`**: Validierung und Verarbeitung von Benutzerdaten.
- **`utils.py`**: Gemeinsame Funktionen wie String-Formatierung.
- **`functions.py`**: Geschäftsspezifische Logik.

---

## Contributing

Beiträge sind willkommen! Erstelle einen Fork des Projekts, führe Änderungen durch und sende einen Pull-Request.

---

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der Datei [LICENSE](LICENSE).
