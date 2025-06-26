# DevOps und Software Engineering Tutorial

Dieses Repository dient als Vorlage für Machine Learning Projekte. Es enthält Anleitungen zum Einrichten des Projekts, zum Trainieren und Vorhersagen mit einem Modell, zum Hochladen auf GitHub und zum Bereitstellen auf Heroku.

## Voraussetzungen:

Windows-Benutzer können dem offiziellen Microsoft-Tutorial folgen, um Python, Git und VSCode zu installieren:

* Englisch: https://docs.microsoft.com/en-us/windows/python/beginners
* Deutsch: https://docs.microsoft.com/de-de/windows/python/beginners

## Visual Studio Code

Dieses Repository ist für [Visual Studio Code](https://code.visualstudio.com/) optimiert. Das `.vscode`-Verzeichnis enthält Konfigurationen für nützliche Erweiterungen wie [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens0) und [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

## Entwicklungseinrichtung

1.  **Repository erstellen**: Erstellen Sie ein GitHub-Repository. Verwenden Sie als Grundlage das folgende Template-Repository: https://github.com/fullstack-ml-academy/python-template.
2.  **Virtuelle Umgebung einrichten**: Öffnen Sie das integrierte Terminal und führen Sie das Setup-Skript für Ihr Betriebssystem aus. Dadurch wird eine virtuelle Python-Umgebung mit allen in `requirements.txt` angegebenen Paketen installiert.

    * **Linux/Mac**:
        ```bash
        ./setup.sh
        source .venv/bin/activate
        ```
    * **Windows**:
        ```powershell
        .\setup.ps1
        .\.venv\Scripts\Activate.ps1
        ```
        * **Fehlerbehebung**: Wenn Ihr System das Ausführen von Powershell-Skripten nicht zulässt, versuchen Sie, die Ausführungsrichtlinie festzulegen: `Set-ExecutionPolicy RemoteSigned`.

3.  **Daten herunterladen**: Laden Sie die Trainingsdaten von https://gist.github.com/OFranke/9359880e40ba14afe795c1e1549839be herunter und legen Sie diese im Repository im Ordner `/data` ab.

## Modell trainieren und Vorhersagen treffen

1.  **Modell trainieren**: Erstellen Sie ein Skript `train.py`. Trainieren Sie das Modell (z.B. Sklearn Decision Tree) und speichern Sie es mit der "pickle"-Bibliothek unter `/data/models`.
2.  **Modellvorhersage**: Erstellen Sie ein Skript `predict.py`. Lesen Sie das zuvor erstellte Modell wieder ein und generieren Sie eine Vorhersage, die im Terminal ausgegeben wird.

## Flask API erstellen

Erstellen Sie eine Flask-API, um das Modell über HTTP-Anfragen verfügbar zu machen.

1.  **Abhängigkeiten installieren**: Installieren Sie `flask` und `flask-cors`.
2.  **API-Struktur**: Erstellen Sie eine `wsgi.py`-Datei und eine `src/api.py`-Datei.
3.  **Endpunkte implementieren**:
    * `GET /`: Gibt `{"hello": "world"}` als JSON zurück.
    * `GET /hello_world`: Gibt `<p>Hello, World!</p>` als HTML zurück.
    * `GET /training_data`: Gibt die Trainingsdaten als JSON zurück.
    * `GET /predict`: Nimmt die Parameter `zylinder`, `ps`, `gewicht`, `beschleunigung` und `baujahr` entgegen und gibt eine Vorhersage als JSON zurück (z.B. `{"result": 18.1}`).

## Auf GitHub hochladen

Verwenden Sie den JIRA + GitHub Workflow, um Ihre Änderungen zu verwalten.

1.  **Git-Repository initialisieren**:
    ```bash
    git init
    ```
2.  **Dateien hinzufügen und committen**:
    ```bash
    git add .
    git commit -m "Erster Commit"
    ```
3.  **Remote-Repository hinzufügen und pushen**:
    ```bash
    git remote add origin <REMOTE_REPOSITORY_URL>
    git push -u origin master
    ```

## Auf Heroku bereitstellen

1.  **Heroku-Konto erstellen**: Legen Sie einen neuen Heroku-Account an.
2.  **Heroku-App erstellen**: Erstellen Sie eine neue Heroku-App.
3.  **GitHub Action für automatisches Deployment einrichten**:
    * Erstellen Sie eine neue GitHub Action, die bei Änderungen im `main`-Branch automatisch auf Heroku deployed wird.
    * Setzen Sie die folgenden Environment Variables in Ihrem GitHub Repository unter `Settings > Secrets`: `HEROKU_API_KEY`, `HEROKU_APP_NAME`, `HEROKU_EMAIL`.
    * Verwenden Sie den Code für die Action von: https://gist.github.com/OFranke/e39c7629bfaa4538fbc616ba60be2d57.
4.  **Procfile erstellen**: Erstellen Sie eine `Procfile`-Datei im Stammverzeichnis Ihres Projekts mit dem folgenden Inhalt, um den API-Server mit `gunicorn` zu starten:
    ```
    web: gunicorn wsgi:app
    ```
5.  **Runtime definieren**: Erstellen Sie eine `runtime.txt`-Datei im Stammverzeichnis, um die Python-Version für Heroku festzulegen:
    ```
    python-3.9.0
    ```
