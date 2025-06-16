# CONTROLE FINANCEIRO
Projeto para controle de despesas/créditos em finanças particulares.

## Melhorias
- Inserir end point para cadastro de usuários com retorno do token de acesso
- Adicionado tag de balanço no retorno -> Indica qual é o balanço do usuário pode ser exibido por: total, por mes, por dia
- Adicionado query param no end point para consulta filtrando por total, por mes, por dia
- Inserir end point para incluir montante inicial (Incluir no banco de usuários)

## Documentação da API

#### Retorna todas as transações do usuário + balanço geral

```http
  /api/transacoes/
```

#### Retorna todas as transações do usuário + balanço para o dia-mes-ano informado

```http
  /api/transacoes/?data=yyyy-mm-dd
```

#### Retorna todas as transações do usuário + balanço para o mes-ano informado

```http
  /api/transacoes/?mes=m&ano=yyyy
```

#### Retorna todas as transações do usuário + balanço para o ano informado

```http
  /api/transacoes/?ano=2024
```

