# Bit Academy: Escola Inteligente

Bit Academy é uma plataforma web para gestão escolar modular e interativa, promovendo a integração entre professores e alunos, além de oferecer ferramentas inteligentes e gamificadas para otimizar o ensino-aprendizagem.

## 🚀 Funcionalidades Principais
- **Bit Main**: Regras de negócio e modelos centrais do sistema.
- **Bit School**: Gestão escolar, administração de alunos, professores e relatórios.
- **Bit Class**: Ambiente de ensino interativo, semelhante ao Google Classroom.
- **Bit Notes**: Plataforma de anotações inteligentes, com flashcards e revisões espaçadas.

## 📂 Estrutura do Projeto  
```bash
bit-academy-back/
│── bit_academy/          # Configuração principal do projeto Django
│   ├── settings.py       # Configurações do Django
│   ├── urls.py           # Rotas principais
│   ├── wsgi.py           # Interface WSGI para servidores
│   ├── asgi.py           # Interface ASGI para WebSockets
│── bit_main/             # App principal com regras de negócio e modelos compartilhados
│── bit_school/           # Funcionalidades para gestão escolar
│── bit_class/            # Ambiente de ensino semelhante ao Google Classroom
│── bit_notes/            # Plataforma de anotações inteligentes e flashcards
│── compose.yml           # Docker Compose para o banco de dados PostgreSQL
│── .env.development      # Variáveis de ambiente para desenvolvimento
│── manage.py             # CLI do Django para gerenciar o projeto
│── requirements.txt      # Dependências do Python
│── README.md             # Documentação do projeto
│── LICENSE               # Licença de uso do projeto
```

## ⚙️ Como Rodar o Projeto  

### 📌 Pré-requisitos  
Antes de começar, certifique-se de ter instalado:
- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) *(para rodar o banco de dados)*
- [Python 3.x](https://www.python.org/) *(para rodar o backend)*
- [Node.js](https://nodejs.org/) e npm/yarn *(para rodar o frontend)*

### 📥 Clone o Repositório  
```bash
git clone https://github.com/lexmoraes/bit-academy.git
cd bit-academy-back
```

### 🐳 Iniciando o Banco de Dados com Docker  
Seu banco de dados PostgreSQL pode ser iniciado com o seguinte comando:  
```bash
docker-compose -f compose.yml up
```
Isso irá:
✅ Criar um container chamado **postgres-dev**
✅ Carregar a imagem **PostgreSQL 16.7 Alpine**
✅ Aplicar variáveis de ambiente definidas em `.env.development`
✅ Expor a porta **5432**

Para parar o banco de dados, use:
```bash
docker compose down
```

### 🚀 Rodando o Backend  
Após iniciar o banco de dados, rode a API com Django:  
```bash
cd bit-academy-back
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📄 Licença  
Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---  
Backend desenvolvido por:
[Alexsandro Moraes](https://github.com/lexmoraes); 🚀
[Antônio Pereira](https://github.com/antonio-pss/); 🚀

Frontend desenvolvido por:
[Alef Monteiro](https://github.com/alef-monteiro); 🚀
[Ithauana Silva](https://github.com/ithauana); 🚀

Repositório do Frontend do projeto:
[Bit Academy frontend](https://github.com/antonio-pss/bit-academy-frontend)