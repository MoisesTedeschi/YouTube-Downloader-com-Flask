
# 📘 Guia de Comandos Git

Este arquivo contém uma lista organizada e comentada dos comandos mais utilizados no Git. Ideal para quem está aprendendo Git ou deseja revisar conceitos importantes.

- [GitHub Gist](https://gist.github.com/MoisesTedeschi/96a5cba54c83fd59013f96015ce6ef7b)
---

## 📦 Commit e Histórico

| Comando | Descrição |
|--------|-----------|
| `git commit -m "mensagem"` | Salva as alterações no repositório com uma mensagem de commit. A flag `-m` significa "message". |
| `git commit -am "mensagem"` | Adiciona e commita as alterações rastreadas em um único comando. |
| `git log` | Exibe o histórico completo de commits. |
| `git log -n 3` | Mostra os **3 commits mais recentes**. |
| `git log --oneline` | Exibe um **resumo dos commits** em uma única linha. |
| `git log --stat` | Mostra **detalhes de arquivos modificados**, linhas adicionadas/removidas. |

---

## 📂 Adicionando e Ignorando Arquivos

| Comando | Descrição |
|--------|-----------|
| `git add nomedoarquivo` | Adiciona o arquivo ao stage. |
| `git add .gitignore` | Adiciona o arquivo `.gitignore` ao stage. |
| `touch .gitignore` | Cria o arquivo `.gitignore`. |
| `echo "arquivo.txt" >> .gitignore` | Ignora um arquivo específico. |
| `echo "*.log" >> .gitignore` | Ignora todos os arquivos com extensão `.log`. |
| `echo "pasta/" >> .gitignore` | Ignora uma pasta inteira. |

---

## 🔄 Controle de Versões e Alterações

| Comando | Descrição |
|--------|-----------|
| `git checkout -- nomedoarquivo` | Desfaz as alterações locais em um arquivo (antes do `git add`). |
| `git reset --hard` | Desfaz **todas as modificações** feitas no projeto. |

---

## 🚮 Remoção e Renomeação

| Comando | Descrição |
|--------|-----------|
| `git rm nomedoarquivo` | Remove um arquivo do repositório. Lembre-se de commitar após isso. |
| `git mv antigo.txt novo.txt` | Renomeia um arquivo. |

---

## 🌿 Trabalhando com Branches

| Comando | Descrição |
|--------|-----------|
| `git branch` | Lista todas as branches. |
| `git branch nome_branch` | Cria uma nova branch. |
| `git checkout nome_branch` | Troca para a branch informada. |
| `git checkout -b nova_branch` | Cria e já troca para a nova branch. |
| `git branch -d nome_branch` | Deleta uma branch (sem commits pendentes). |
| `git branch -D nome_branch` | Força a deleção de uma branch (mesmo com commits). |
| `git branch --no-merged` | Lista branches que **ainda não foram mescladas**. |

---

## 🔗 Conectando ao GitHub

| Comando | Descrição |
|--------|-----------|
| `git remote add origin https://github.com/usuario/repositorio.git` | Liga seu repositório local a um repositório remoto no GitHub. |
| `git clone https://github.com/usuario/repositorio.git` | Clona um repositório existente do GitHub. |

---

## 🔀 Merge (Mesclagem)

| Comando | Descrição |
|--------|-----------|
| `git merge nome_branch -m "mensagem"` | Mescla a `nome_branch` à branch atual com uma mensagem explicativa. |

---

## 🚚 Enviando e Recebendo Alterações

| Comando | Descrição |
|--------|-----------|
| `git push origin nome_branch` | Envia os commits locais para o repositório remoto. |
| `git push -u origin nome_branch` | Envia e define o upstream (vínculo entre branch local e remota). |
| `git pull` | Baixa e mescla alterações do repositório remoto. |
| `git fetch` | Baixa alterações remotas **sem mesclar automaticamente**. |

---

## 👀 Status e Diagnóstico

| Comando | Descrição |
|--------|-----------|
| `git status` | Mostra o estado atual do repositório. |
| `git diff` | Mostra as diferenças entre os arquivos modificados e o último commit. |
| `git diff --staged` | Mostra as diferenças dos arquivos **já adicionados** ao stage. |

---

## 🔄 Revertendo Commits

| Comando | Descrição |
|--------|-----------|
| `git revert <id-do-commit>` | Cria um novo commit que **desfaz** um commit anterior. |
| `git reset --soft HEAD~1` | Remove o último commit, mantendo as alterações no stage. |
| `git reset --mixed HEAD~1` | Remove o commit e tira as alterações do stage. |
| `git reset --hard HEAD~1` | Apaga o commit e as alterações locais (⚠️ irreversível). |

---

## 🛠️ Repositórios e Configuração

| Comando | Descrição |
|--------|-----------|
| `git init` | Cria um novo repositório Git local. |
| `git config --global user.name "Seu Nome"` | Define o nome do usuário global para commits. |
| `git config --global user.email "seu@email.com"` | Define o e-mail do usuário global para commits. |

---

## 💡 Dicas Extras

| Comando | Descrição |
|--------|-----------|
| `git stash` | Salva alterações temporariamente (sem commitar). |
| `git stash pop` | Recupera as alterações salvas com `stash`. |
| `git tag v1.0` | Cria uma tag (ex: versão). |

---

## 🧼 Outros Comandos Úteis

| Comando | Descrição |
|--------|-----------|
| `Ctrl + L` | Limpa a tela do terminal. |

---

## 📝 Observações Importantes

- Uma branch só pode ser deletada se você **não estiver nela**.
- Use `git pull` com cuidado em projetos colaborativos para evitar conflitos inesperados.
- Prefira `git revert` a `git reset` em repositórios compartilhados para manter o histórico limpo e seguro.

---

## 🙋‍♂️ Autor
Moisés Tedeschi de Melo [MOA]

---

📁 Este material pode ser atualizado com novos comandos com o tempo. Contribuições são bem-vindas!