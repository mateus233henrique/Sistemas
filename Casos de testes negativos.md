# Casos de Teste Negativos – Sistema Bancário

---

## CT005 – Criar Conta com Nome Vazio

**Objetivo:**  
Validar que o sistema não permite criar conta sem nome.

**Pré-condições:**  
- Sistema acessível

**Passos:**
1. Não informar nome do titular
2. Tentar criar conta

**Resultado Esperado:**  
- Exibir mensagem: "Nome é obrigatório"
- Conta não deve ser criada

---

## CT006 – Criar Conta Duplicada

**Objetivo:**  
Validar que o sistema não permite criar contas com o mesmo nome.

**Pré-condições:**  
- Conta já existente

**Passos:**
1. Informar nome já cadastrado
2. Tentar criar nova conta

**Resultado Esperado:**  
- Exibir mensagem: "Conta já existe"
- Nova conta não deve ser criada

---

## CT007 – Depositar Valor Negativo

**Objetivo:**  
Validar que o sistema rejeita depósitos com valor negativo.

**Pré-condições:**  
- Conta criada

**Passos:**
1. Informar nome do titular
2. Informar valor negativo (ex: -100)
3. Confirmar operação

**Resultado Esperado:**  
- Exibir mensagem: "Valor inválido"
- Saldo não deve ser alterado

---

## CT008 – Depositar em Conta Inexistente

**Objetivo:**  
Validar comportamento ao tentar depositar em conta não cadastrada.

**Pré-condições:**  
- Conta não existe

**Passos:**
1. Informar nome não cadastrado
2. Informar valor válido
3. Confirmar operação

**Resultado Esperado:**  
- Exibir mensagem: "Conta não encontrada"
- Operação não deve ser realizada

---

## CT009 – Sacar Valor Maior que o Saldo

**Objetivo:**  
Validar que o sistema impede saque sem saldo suficiente.

**Pré-condições:**  
- Conta com saldo menor que o valor solicitado

**Passos:**
1. Informar nome do titular
2. Informar valor maior que o saldo
3. Confirmar operação

**Resultado Esperado:**  
- Exibir mensagem: "Saldo insuficiente"
- Saldo não deve ser alterado

---

## CT010 – Sacar Valor Negativo

**Objetivo:**  
Validar que o sistema rejeita valores negativos no saque.

**Pré-condições:**  
- Conta criada

**Passos:**
1. Informar nome do titular
2. Informar valor negativo
3. Confirmar operação

**Resultado Esperado:**  
- Exibir mensagem: "Valor inválido"
- Operação não deve ser realizada

---

## CT011 – Consultar Saldo de Conta Inexistente

**Objetivo:**  
Validar comportamento ao consultar saldo de conta não cadastrada.

**Pré-condições:**  
- Conta não existe

**Passos:**
1. Informar nome não cadastrado

**Resultado Esperado:**  
- Exibir mensagem: "Conta não encontrada"

---

## CT012 – Inserir Caracteres Inválidos no Nome

**Objetivo:**  
Validar tratamento de entrada inválida no nome do titular.

**Pré-condições:**  
- Sistema acessível

**Passos:**
1. Informar nome com caracteres especiais (ex: @#$%)
2. Tentar criar conta

**Resultado Esperado:**  
- Exibir mensagem de erro para entrada inválida
- Conta não deve ser criada
