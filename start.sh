#!/bin/bash

# Démarrer l'application Django
python manage.py runserver 0.0.0.0:8000 &

# Attendre que l'application soit démarrée
sleep 5

# Afficher un message personnalisé
echo "Django app is running on http://localhost:8000"

# Maintenir le script en cours d'exécution
tail -f /dev/null
