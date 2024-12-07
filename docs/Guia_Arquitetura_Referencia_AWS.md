
# Guia para Criar uma Arquitetura de Referência na AWS

Este guia passo a passo foi projetado para ajudar iniciantes a criar uma arquitetura de referência na AWS, cobrindo os principais tópicos das certificações **AWS Certified Cloud Practitioner**, **AWS Certified Solutions Architect – Associate**, e **AWS Certified Solutions Architect – Professional**. O foco é utilizar o Free Tier para minimizar custos.

## Passo 1: Planejamento Inicial

### 1. Entenda o que vamos criar:
- Um site simples ou uma API funcional.
- Armazenamento de arquivos em S3.
- Banco de dados relacional em RDS.
- Monitoramento de desempenho com CloudWatch.
- Automação para deploys com CodePipeline.

### 2. Configuração inicial:
- Crie uma conta AWS: [https://aws.amazon.com/free](https://aws.amazon.com/free).
- Habilite o Billing Alerts no console de CloudWatch para monitorar gastos.
- Configure o AWS Budgets para criar alertas caso algum limite de custo seja ultrapassado.

### 3. Ferramentas que você vai usar:
- Navegador web (para acessar o console AWS).
- Editor de texto (Visual Studio Code ou outro).
- Um terminal para testes CLI (AWS CLI).

## Passo 2: Estrutura Inicial da Arquitetura

### 1. Rede (VPC)
- Crie uma VPC com 2 sub-redes públicas e 2 sub-redes privadas.
- Configure tabelas de roteamento para suportar internet gateway e NAT Gateway.

### 2. Computação (EC2)
- Configure uma instância EC2 (t2.micro no Free Tier).
- Instale um servidor web (ex.: Apache) e configure um site simples.

### 3. Armazenamento (S3)
- Crie um bucket S3 para armazenar arquivos estáticos.
- Habilite a hospedagem de site estático.

### 4. Banco de Dados (RDS)
- Configure um banco de dados relacional (MySQL ou PostgreSQL).
- Habilite backups automáticos e Multi-AZ.

### 5. Monitoramento (CloudWatch)
- Configure métricas e alarmes para monitorar o uso de recursos (CPU, memória).

### 6. Automação (CodePipeline)
- Configure um pipeline para automatizar o deploy de aplicações no EC2.

## Passo 3: Configuração e Implementação

1. Configure o site hospedado no EC2, instale um servidor web (Apache ou Nginx) e faça upload de um arquivo `index.html` simples.
2. Configure o bucket S3 para armazenar arquivos estáticos e habilite a hospedagem de site estático.
3. Configure o banco RDS e crie tabelas simples para testes usando clientes SQL.

## Passo 4: Salve a Arquitetura como Código

Use **AWS CloudFormation** para salvar a infraestrutura como código. Aqui está um exemplo simplificado para criar uma VPC, sub-rede e uma instância EC2:

```yaml
Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16

  MySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24

  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0abcdef1234567890
      SubnetId: !Ref MySubnet
```

## Passo 5: Validação e Ajustes

1. Verifique o funcionamento dos serviços (EC2, S3, RDS).
2. Teste o site hospedado no navegador.
3. Verifique logs e métricas no CloudWatch.

## Passo 6: Prática Contínua

1. Expanda a arquitetura adicionando serviços como Lambda, DynamoDB ou API Gateway.
2. Use o arquivo CloudFormation para recriar a arquitetura de forma automatizada.

## Conclusão

Seguindo este guia, você poderá criar e testar uma arquitetura de referência na AWS usando o Free Tier, enquanto aprende os principais conceitos das certificações AWS. Certifique-se de destruir os recursos após o uso para evitar custos.
