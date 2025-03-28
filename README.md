# Gerador de Resposta para GLPI

## Descrição
Este projeto foi desenvolvido para auxiliar na geração de padrões de resposta de chamados para criação de usuário e senha para novos funcionários. O programa recebe o nome completo do usuário, formata a exibição do nome e gera automaticamente uma saudação, um nome de usuário ou e-mail, além de criar uma senha baseada em suas iniciais e na data atual.

## Funcionalidades
- **Formata o nome do usuário** com as iniciais em maiúsculo.
- **Remove acentos** para a geração do nome de usuário e e-mail.
- **Permite escolher** entre gerar um **usuário do Active Directory (AD)** ou um **e-mail institucional**.
- **Gera uma senha** no formato `Iniciais#DDMM`.
- **Exibe uma mensagem de saudação** baseada no horário atual.

## Estrutura do Projeto
```
/
├── gerador_de_resposta.py
├── utilidades.py
├── README.md
```

## 📂 Arquivos
### `gerador_de_resposta.py`
Arquivo principal que gerencia a entrada do usuário e exibe os resultados formatados.

### `utilidades.py`
Módulo com funções auxiliares:
- `descobrir_data()`: Retorna a data atual.
- `formatar_data(data)`: Retorna a data no formato `DDMM`.
- `apresentar(data)`: Exibe uma mensagem de saudação baseada no horário atual.
- `exibir_linha()`: Exibe uma linha separadora.
- `remover_acentos(texto)`: Remove os acentos de uma string.
- `criar_usuario(primeiro_nome, ultimo_nome)`: Cria o usuário no formato `primeiro_nome.ultimo_nome`.
- `criar_senha(iniciais, data)`: Cria a senha no formato `Iniciais#DDMM`.

## 🚀 Exemplo de Uso
### 📥 Entrada:
```
Nome completo: João Silva José
```
### 📤 Saída:
```
Nome formatado: João Silva José
Usuário: joao.jose
Senha: Jsj#2803
```

## 🛠 Como Executar
1. Certifique-se de ter o Python instalado.
2. Clone ou baixe este repositório.
3. Execute o arquivo principal:
   ```sh
   python gerador_de_resposta.py
   ```
4. Escolha a opção desejada e insira o nome completo.

## 🔥 Melhorias Futuras
- Criar uma interface gráfica para facilitar o uso.
- Permitir customização do padrão de senha.

---
Desenvolvido por **Carlos André Resende Belo**.

