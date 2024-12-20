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

The frontend communicates with the following backend API endpoints to provide core functionality.

### Authentication
- **POST** `/registration/`  
  Register a new user.

- **POST** `/login/`  
  Log in a user.

---

### Profiles
- **GET** `/profile/<int:user_id>/`  
  Retrieve a user profile.

- **GET** `/profiles/business/`  
  Retrieve all business profiles.

- **GET** `/profiles/business/<int:user_id>/`  
  Retrieve a specific business profile.

- **GET** `/profiles/customer/`  
  Retrieve all customer profiles.

- **GET** `/profiles/customer/<int:user_id>/`  
  Retrieve a specific customer profile.

---

### Offers
- **GET** `/offers/`  
  Retrieve all offers.

- **POST** `/offers/`  
  Create a new offer.

- **GET** `/offers/<int:id>/`  
  Retrieve details of an offer.

---

### Orders
- **GET** `/orders/`  
  Retrieve all orders.

- **POST** `/orders/`  
  Create a new order.

- **GET** `/orders/<int:order_id>/`  
  Retrieve details of an order.

- **GET** `/order-count/<int:offer_id>/`  
  Count of orders in progress for an offer.

- **GET** `/completed-order-count/<int:user_id>/`  
  Retrieve completed orders of a user.

---

### Reviews
- **GET** `/reviews/`  
  Retrieve all reviews.

- **POST** `/reviews/`  
  Create a new review.

- **GET** `/reviews/<int:pk>/`  
  Retrieve details of a review.

- **PUT** `/reviews/<int:pk>/`  
  Edit a review.

- **DELETE** `/reviews/<int:pk>/`  
  Delete a review.

---

### Base Information
- **GET** `/base-info/`  
  Retrieve base information of the application.

---

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
