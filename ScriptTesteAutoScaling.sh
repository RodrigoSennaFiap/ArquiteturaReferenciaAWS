#!/bin/bash
# Define que o script será executado pelo interpretador bash

# Atualiza todos os pacotes do sistema
yum update -y

# Instala o servidor web Apache (httpd)
yum install -y httpd

# Inicia o serviço do Apache
systemctl start httpd

# Configura o Apache para iniciar automaticamente na inicialização do sistema
systemctl enable httpd

# Obtém a Availability Zone onde a instância EC2 está rodando através dos metadados
EC2AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)

# Cria um arquivo temporário com o template HTML
echo '<center><h1>Esta EC2 está na Zona: AZID </h1></center>' > /var/www/html/index.txt

# Substitui o placeholder AZID pela zona real e cria o arquivo HTML final
sed "s/AZID/$EC2AZ/" /var/www/html/index.txt > /var/www/html/index.html