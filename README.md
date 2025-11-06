# E-Stay — Powered by LinkUp

**Hospedagem inteligente com tecnologia LinkUp — conforto, conectividade e gestão simplificada.**

Base operacional: Vila de Ponta Negra, Natal/RN  
Desenvolvido por: Akiles Simião

## Visão geral
E-Stay é um localizador de pousadas que encontra opções com os menores preços e filtra estabelecimentos que **não oferecem café da manhã**, exibindo resultados em lista e mapa.

## Estrutura do repositório
```
E-Stay/
├── backend/       # Django + DRF
├── frontend/      # ReactJS (CRA)
├── .github/       # Workflows e templates
├── README.md
└── LICENSE
```

## Como rodar localmente

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

> **Importante:** Não inclua sua chave do Google Maps em repositórios públicos. Coloque a chave em `backend/.env` (não versionado).

### Frontend
```bash
cd frontend
npm install
# para desenvolvimento (com proxy para backend em localhost:8000)
npm start
```

## Contribuindo
1. Fork este repositório
2. Crie uma branch: `git checkout -b feature/nome-da-feature`
3. Abra um pull request

