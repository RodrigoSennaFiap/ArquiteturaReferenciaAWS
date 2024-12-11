# Sistema de Registro e Consulta de Feedback de Usuários

Este projeto demonstra como implementar um sistema simples para registrar e consultar feedbacks de usuários utilizando serviços da AWS. Ele inclui um frontend em HTML, backend com AWS Lambda, e armazenamento em DynamoDB. A infraestrutura é gerenciada via CloudFormation para facilitar o provisionamento e a destruição dos recursos.

---

## **Arquitetura do Sistema**
- **Frontend**: Página web para submissão do feedback.
- **Backend**: Função Lambda para processar as solicitações.
- **Banco de Dados**: DynamoDB para armazenar feedbacks.
- **API Gateway**: Interface RESTful para comunicação entre frontend e backend.
- **Autenticação**: AWS Cognito para proteger as consultas administrativas.
- **Infraestrutura**: Provisionada com CloudFormation.

---

## **Pré-requisitos**
1. Conta AWS ativa com permissões para criar os recursos necessários.
2. AWS CLI configurado localmente.
3. Python 3.9 ou superior instalado.
4. Bucket S3 para armazenar o código Lambda.
5. Editor de texto (como VS Code).
6. Familiaridade com serviços da AWS e CloudFormation.

---

## **Passo a Passo**

### **1. Configurar Infraestrutura**
1. Clone este repositório:
   ```bash
   git clone <url-do-repo>
   cd <nome-do-repo>
