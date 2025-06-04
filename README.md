# 🎬 YouTube Downloader com Flask

Este projeto é uma aplicação web simples para baixar vídeos, áudios ou playlists do YouTube utilizando a biblioteca [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), com uma interface moderna em Flask + HTML + CSS puro. Também exibe um histórico local de downloads usando `localStorage`.

---

## 🔧 Funcionalidades

- 📥 Download de:
  - Vídeos em alta qualidade
  - Áudios em MP3
  - Playlists completas
- 🕒 Histórico de downloads salvos localmente (via browser `localStorage`)
- 🧭 Paginação automática quando houver mais de 10 itens no histórico
- 🎨 Interface moderna e responsiva com CSS personalizado
- 🧩 Verificação automática da presença do `ffmpeg`
- 🔒 Proteção contra interações durante o download com loading overlay

---

## 📦 Tecnologias Utilizadas

### Backend

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- `ffmpeg` (para conversão de áudio)

### Frontend

- HTML5
- CSS3
- JavaScript puro (sem dependências externas)
- `localStorage` para manter histórico

---

## 📁 Estrutura do Projeto
<!-- TREEVIEW START -->
```
youtube-downloader-flask/
├── app.py                 # App principal Flask
├── test_app.py            # Testes com pytest
├── downloads/             # Pasta onde os vídeos/áudios são salvos
├── static/                # Arquivos estáticos (CSS, imagens, etc.)
│   └── css/               # Estilos customizados
│   │   └── styles.css     # Arquivo referente ao estilo do projeto
│   └── js/                # Funções customizadas
│   │   └── script.js      # Arquivo referente as funções JS do projeto
│   └── img/
│       └── favicon.ico    # Ícone da aba (adicione o seu aqui)
├── templates/
│   └── index.html         # Página principal da aplicação
├── README.md              # Este arquivo
└── LICENSE                # Licença de uso (MIT)
```
<!-- TREEVIEW END -->
---

## ▶️ Como Executar

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/youtube-downloader-flask.git
cd youtube-downloader-flask
```

2. **Crie um ambiente virtual**

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**

```
pip install -r requirements.txt
```

4. **Execute o app**

```
python app.py
```

5. **Acesse no navegador**

```
http://127.0.0.1:5000/
```

## 🧪 Rodando os Testes

```
pytest test_app.py
```

## 📝 Observações

- O histórico de downloads é salvo no navegador do usuário, não no servidor.

- A conversão de áudio exige o ffmpeg instalado e disponível no PATH.

- Não são armazenados arquivos no servidor além da pasta downloads/.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

## 🙋‍♂️ Autor
Moisés Tedeschi de Melo [MOA]