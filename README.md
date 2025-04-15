# Gerador de Resposta para GLPI

## Descrição
Este projeto foi desenvolvido para auxiliar na geração de padrões de resposta de chamados para criação de usuário e senha para novos funcionários.

O programa recebe o nome completo do usuário, formata a exibição do nome e gera automaticamente uma saudação, um nome de usuário ou e-mail, além de criar uma senha baseada em suas iniciais e na data atual.

O projeto também possui uma interface gráfica interativa utilizando a biblioteca **Flet**, tornando o uso mais intuitivo e acessível.

## Funcionalidades
- **Formata o nome do usuário** com as iniciais em maiúsculo.
- **Remove acentos** para a geração do nome de usuário e e-mail.
- **Permite escolher** entre gerar um **usuário do Active Directory (AD)** ou um **e-mail institucional**.
- **Gera uma senha** no formato `Iniciais#DDMM`.
- **Exibe uma mensagem de saudação** baseada no horário atual.
- **Interface gráfica interativa** para facilitar o uso do sistema.

## Estrutura do Projeto
```
/
├── gerador_de_resposta.py
├── utilidades.py
├── interface_flet.py
├── README.md
```

## 📂 Arquivos
### `gerador_de_resposta.py`
Arquivo principal que gerencia a entrada do usuário e retorna os resultados formatados.

### `utilidades.py`
Módulo com funções auxiliares:
- `descobrir_data()`: Retorna a data atual.
- `formatar_data(data)`: Retorna a data no formato `DDMM`.
- `remover_acentos(texto)`: Remove os acentos de uma string.
- `apresentar(data)`: Exibe uma mensagem de saudação baseada no horário atual.
- `criar_usuario(primeiro_nome, ultimo_nome)`: Cria o usuário no formato `primeiro_nome.ultimo_nome`.
- `criar_senha(iniciais, data)`: Cria a senha no formato `Iniciais#DDMM`.
- `mostrar_saudacao_final`: Exibe uma mensagem de saudação final com orientações para nova senha.

### `interface_flet.py`
Arquivo que implementa a interface gráfica utilizando a biblioteca **Flet**, permitindo uma interação mais amigável com o usuário.

## 🚀 Exemplo de Uso
### 📥 Entrada:

Qual é o assunto do chamado?

Opção: AD | E-mail

Nome completo: joão SILVA JosÉ

### 📤 Saída:
Nome formatado: João Silva José

Boa tarde,

Usuário: joao.jose

Senha: Jsj#3103

Crie uma nova senha seguindo os critérios de segurança:

A senha deve conter pelo menos 8 caracteres.

Deve possuir, no mínimo, uma letra maiúscula.

Deve conter, no mínimo, uma letra minúscula.

Deve incluir, pelo menos, um número ou caracter especial (por exemplo, @, #, $, etc.). Após definir a nova senha, confirme a alteração.

Att...


## 🛠 Como Executar
### Via Interface Gráfica
1. Certifique-se de ter o Python instalado.
2. Clone ou baixe este repositório.
3. Execute o arquivo da interface gráfica:
   ```sh
   interface_flet.py
   ```
4. Preencha o formulário com as informações solicitadas (escolha entre AD ou E-mail e nome completo) e clique em Gerar resposta.

### Via Linha de Comando (sem interface gráfica)
1. Certifique-se de ter o Python instalado.
2. Clone ou baixe este repositório.
3. Execute o arquivo principal:
   ```sh
   gerador_de_resposta.py
   ```
4. Escolha a opção desejada e insira o nome completo.

## 🔥 Melhorias Futuras
- Melhorar a interface gráfica com mais recursos interativos.
- Permitir customização do padrão de senha.
- Implementar validação mais robusta de entradas.

## 🤝 Contribuições
Contribuições são bem-vindas! Se você deseja melhorar este projeto, por favor, siga os passos abaixo:
1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas alterações (git commit -m 'Adiciona nova feature').
4. Faça o push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

## 📜 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](https://github.com/CaseResende/Gerador-de-resposta/blob/main/LICENSE) mais detalhes.

Desenvolvido por **Carlos André Resende Belo**. 😎

