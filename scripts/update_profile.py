#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Caminhos
SOURCE_FILE = "/home/paulo-lima/AppGear/README.md"
TARGET_FILE = "/home/paulo-lima/.github/profile/README.md"

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_info(content):
    info = {}
    
    # Extrair Versão
    # ![Version](https://img.shields.io/badge/Version-2.0.0-blue)
    version_match = re.search(r'!\[Version\]\(.*?Version-(.*?)-.*?\)', content)
    if version_match:
        info['version'] = version_match.group(1)
    
    # Extrair Status
    # ![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
    status_match = re.search(r'!\[Status\]\(.*?Status-(.*?)-.*?\)', content)
    if status_match:
        info['status'] = status_match.group(1).replace('%20', ' ')

    return info

def update_target(content, info):
    # Mapeamento manual de meses para garantir Português
    months = {
        1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril',
        5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
        9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
    }
    now = datetime.now()
    month_name = months[now.month]
    today = f"{now.day:02d} de {month_name} de {now.year}"
    
    new_content = content
    
    # Atualizar Versão no Rodapé
    # **Versão 2.0** • Última atualização: ...
    if 'version' in info:
        # Regex para encontrar o padrão de versão
        new_content = re.sub(
            r'\*\*Versão.*?\*\*', 
            f'**Versão {info["version"]}**', 
            new_content
        )

    # Atualizar Data
    # Última atualização: ...
    new_content = re.sub(
        r'Última atualização: .*?$', 
        f'Última atualização: {today}', 
        new_content,
        flags=re.MULTILINE
    )
    
    return new_content

def main():
    if not os.path.exists(SOURCE_FILE):
        print(f"Erro: Arquivo fonte não encontrado em {SOURCE_FILE}")
        return
    
    if not os.path.exists(TARGET_FILE):
        print(f"Erro: Arquivo alvo não encontrado em {TARGET_FILE}")
        return

    print("Lendo arquivo fonte...")
    source_content = read_file(SOURCE_FILE)
    
    print("Extraindo informações...")
    info = extract_info(source_content)
    print(f"Informações encontradas: {info}")
    
    print("Lendo arquivo alvo...")
    target_content = read_file(TARGET_FILE)
    
    print("Atualizando conteúdo...")
    new_target_content = update_target(target_content, info)
    
    if new_target_content != target_content:
        write_file(TARGET_FILE, new_target_content)
        print("profile/README.md atualizado com sucesso")
    else:
        print("Nenhuma alteração necessária em profile/README.md")

if __name__ == "__main__":
    # Tenta definir o locale para pt_BR, mas usa fallback manual caso falhe
    try:
        import locale
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except:
        pass 
        
    main()
