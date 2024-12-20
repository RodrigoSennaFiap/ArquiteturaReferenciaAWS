
# Guia para Criar uma Arquitetura de Referência na AWS
## Passo 1: Planejamento Inicial
### Entenda o que vamos criar
- Um site simples ou uma API funcional.
- Armazenamento de arquivos em S3.
- Banco de dados relacional em RDS.
- Monitoramento de desempenho com CloudWatch.
- Automação para deploys com CodePipeline.
### Configuração inicial
- Crie uma conta AWS: [https://aws.amazon.com/free](https://aws.amazon.com/free).
- Habilite o Billing Alerts no console de CloudWatch para monitorar gastos.
- Configure o AWS Budgets para criar alertas caso algum limite de custo seja ultrapassado.
### Ferramentas que você vai usar
- Navegador web (para acessar o console AWS).
- Editor de texto (Visual Studio Code ou outro).
- Um terminal para testes CLI (AWS CLI).
## Passo 2: Estrutura Inicial da Arquitetura
### Rede (VPC)
- Crie uma VPC com 2 sub-redes públicas e 2 sub-redes privadas.
- Configure tabelas de roteamento para suportar internet gateway e NAT Gateway.
### Computação (EC2)
- Configure uma instância EC2 (t2.micro no Free Tier).
- Instale um servidor web (ex.: Apache) e configure um site simples.
### Armazenamento (S3)
- Crie um bucket S3 para armazenar arquivos estáticos.
- Habilite a hospedagem de site estático.
### Banco de Dados (RDS)
- Configure um banco de dados relacional (MySQL ou PostgreSQL).
- Habilite backups automáticos e Multi-AZ.
### Monitoramento (CloudWatch)
- Configure métricas e alarmes para monitorar o uso de recursos (CPU, memória).
### Automação (CodePipeline)
- Configure um pipeline para automatizar o deploy de aplicações no EC2.
## Passo 3: Configuração e Implementação
- Configure o site hospedado no EC2, instale um servidor web (Apache ou Nginx) e faça upload de um arquivo index.html simples.
- Configure o bucket S3 para armazenar arquivos estáticos e habilite a hospedagem de site estático.
- Configure o banco RDS e crie tabelas simples para testes usando clientes SQL.
## Passo 4: Salve a Arquitetura como Código
### Exemplo de CloudFormation
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
- Verifique o funcionamento dos serviços (EC2, S3, RDS).
- Teste o site hospedado no navegador.
- Verifique logs e métricas no CloudWatch.
## Passo 6: Prática Contínua
- Expanda a arquitetura adicionando serviços como Lambda, DynamoDB ou API Gateway.
- Use o arquivo CloudFormation para recriar a arquitetura de forma automatizada.
## Conclusão
- Certifique-se de destruir os recursos após o uso para evitar custos.
