# TP DevSecOps avec Docker

![Build and Scan](https://github.com/maksoumotm/DevSecOps-TP1/actions/workflows/deploy.yml/badge.svg)
![CodeQL](https://github.com/maksoumotm/DevSecOps-TP1/actions/workflows/codeql-analysis.yml/badge.svg)

## Pipeline DevSecOps

Ce projet implémente un pipeline CI/CD sécurisé pour Docker avec :
- Analyse statique du code (CodeQL)
- Lint du Dockerfile (Hadolint)
- Scan de l'image Docker (Trivy)
- Scan des dépendances (Dependabot)
- Secret Scanning
- Security Gates (blocage sur vulnérabilités critiques)
- SBOM (Software Bill of Materials)

## Sécurité de l'Image

- Image de base : nginx:alpine (version spécifique)
- Utilisateur non-root
- Headers de sécurité renforcés
- Health checks
- Pas de secrets dans l'image

## Exécution Locale

```bash
docker pull ghcr.io/maksoumotm/devops-tp-docker:main
docker run -p 8080:8080 ghcr.io/maksoumotm/devops-tp-docker:main
```
