# streamlitbot
## Membre du projet
Virasidh KIM

## Instructions pour lancer le projet Streamlit depuis GitHub

1. Récupérer le projet depuis GitHub

1.1 Copiez l’URL du dépôt GitHub.

1.2 Clonez le projet en utilisant la commande suivante dans un terminal :

    git clone <URL_DU_DEPOT>
    
Exemple :

    git clone https://github.com/virakim/streamlitbot.git

1.3 Entrez dans le dossier cloné :

    cd streamlitbot

2. Créer un environnement virtuel Python

2.1 Créez un environnement virtuel nommé stenv :

    python -m venv stenv

2.2 Activez l’environnement virtuel :
    
    - Sous Windows :
        stenv\Scripts\activate
    - Sous Mac/Linux :
        source stenv/bin/activate

3. Installer les dépendances

3.1 Installez les modules nécessaires à l’aide du fichier requirements.txt :

    pip install -r requirements.txt

4. Configurer les clés API

4.1 Créez un dossier .streamlit dans le répertoire du projet :

    - Sous Windows :
        mkdir .streamlit
    - Sous Mac/Linux :
        mkdir -p .streamlit

4.2 Dans ce dossier, créez le fichier secrets.toml :

    - Sous Windows :
        echo > .streamlit\secrets.toml
    - Sous Mac/Linux :
        touch .streamlit/secrets.toml

4.3 Ajoutez votre clé API OpenAI dans le fichier secrets.toml :

    [OPENAI]
    API_KEY = "votre_clé_api_openai"

5. Lancer l’application Streamlit, pour cela :

5.1 Exécutez la commande suivante pour démarrer l’application :

    streamlit run chatbotgpt.py

5.2 Une fenêtre de navigateur s’ouvrira avec l’interface utilisateur du chatbot.
