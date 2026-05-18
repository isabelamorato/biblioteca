---

name: resumo-whatsapp

description: Resume uma conversa exportada de grupo de WhatsApp (colada como texto ou passada como caminho de arquivo .txt) destacando decisões tomadas, pendências e temas em debate. Use sempre que o usuário mencionar conversa, chat ou grupo de WhatsApp — disser "me resume essa conversa", "resume esse chat", "resume esse grupo", "perdi o grupo", "voltei de férias e tem 500 mensagens", "me atualiza sobre essa conversa", ou passar um caminho de arquivo .txt de export do WhatsApp.

---



# /resumo-whatsapp



Transforma uma conversa longa de grupo de WhatsApp em um resumo

curto que diz o que foi decidido, o que ficou pendente e quais

temas estão em debate. Útil quando você sumiu do grupo por uns

dias e não quer ler 500 mensagens pra se atualizar.



## Instruções



### Passo 1: Receber a conversa



O usuário cola o conteúdo do export do grupo de WhatsApp, ou

passa o caminho de um arquivo .txt. Se ele chamar a skill sem

fornecer o conteúdo, peça gentilmente antes de prosseguir.



### Passo 2: Classificar cada item



Leia a conversa inteira e separe cada item relevante em uma de

três categorias:



- Decisões tomadas: o grupo fechou o assunto e não volta mais

- Pendências: alguém precisa fazer algo, ficou em aberto

- Temas em debate: discussão ainda sem conclusão



### Passo 3: Devolver no formato fixo



SEMPRE no formato abaixo, sem preâmbulo:



**Decisões tomadas**

- [decisão 1]



**Pendências**

- [quem] — [o que precisa fazer]



**Temas em debate**

- [tema 1]



Se alguma seção não tiver conteúdo, escreva "(nada)" abaixo do

título. Não invente.



## Exemplo



### Cenário: volta de férias



Usuário diz: "me atualiza sobre esse grupo: [conteúdo do export colado]"



Ações:

1. Ler a conversa inteira

2. Classificar cada item em decisão, pendência ou debate

3. Devolver no formato fixo da seção Instruções



Resultado:



**Decisões tomadas**

- Aula remarcada pra quarta às 19h

- Stack oficial: Claude Code + skill /pesquisa + Perplexity



**Pendências**

- Thales — documentar fix do Perplexity no Windows

- Hugo — enviar app de controle de cartões até sexta



**Temas em debate**

- Cowork vs Code vs app desktop

- Melhor rota pra automação WhatsApp sem API oficial
