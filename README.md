# Sales KPI

## Description

Sales KPI est un module personnalisé développé sous Odoo 18 pour suivre les performances mensuelles des commerciaux.

Le module est totalement indépendant des modules CRM et Sales d'Odoo.
Toutes les données sont saisies manuellement.

## Fonctionnalités

- Gestion des commerciaux
- Enregistrement des KPI mensuels
- Calcul automatique des indicateurs de performance
- Vue liste
- Vue formulaire
- Vue recherche
- Menu dédié "Sales KPI"
- API REST avec les méthodes GET et POST

## Modèles de données

### Commercial

Le modèle Commercial contient :

- Nom
- Email
- Téléphone

### KPI mensuel

Le modèle KPI mensuel contient :

- Commercial
- Mois
- Année
- Nombre de prospects contactés
- Nombre de rendez-vous obtenus
- Nombre de devis envoyés
- Nombre de ventes réalisées
- Chiffre d'affaires généré

## Indicateurs calculés

### Taux de transformation

Nombre de ventes / Nombre de prospects contactés × 100

### Taux de conversion Prospect → Rendez-vous

Nombre de rendez-vous / Nombre de prospects contactés × 100

### Valeur moyenne d'une vente

Chiffre d'affaires / Nombre de ventes

Les indicateurs sont calculés automatiquement par Odoo.

## Installation

1. Copier le dossier `sales_kpi` dans le répertoire `addons` d'Odoo.
2. Redémarrer le serveur Odoo.
3. Activer le mode développeur.
4. Aller dans **Applications**.
5. Cliquer sur **Mettre à jour la liste des applications**.
6. Rechercher **Sales KPI**.
7. Cliquer sur **Activer**.

## Utilisation

Le module ajoute un menu dédié dans Odoo :

Sales KPI

├── Commercials

└── Monthly KPIs

### Ajouter un commercial

Créer un commercial et renseigner :

- Nom
- Email
- Téléphone

### Ajouter un KPI mensuel

Sélectionner le commercial puis renseigner :

- Mois
- Année
- Prospects contactés
- Rendez-vous obtenus
- Devis envoyés
- Ventes réalisées
- Chiffre d'affaires généré

Les indicateurs calculés sont automatiquement mis à jour.

## API REST

### GET - Récupérer les KPIs

Endpoint :

GET /api/sales-kpi

Exemple :

```bash
curl.exe -i "http://localhost:8069/api/sales-kpi"
```

### POST - Créer un KPI


Endpoint :

POST /api/sales-kpi

Exemple avec PowerShell :
```bash
$body = @{
    commercial_id = 1
    month = 9
    year = 2026
    prospects_contacted = 30
    appointments = 12
    quotations = 8
    sales = 3
    revenue = 300000
} | ConvertTo-Json -Compress

Invoke-RestMethod -Uri "http://localhost:8069/api/sales-kpi" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```