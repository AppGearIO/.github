#!/usr/bin/env python3
"""
Script para atualizar profile/README.md com informações do README.md principal.
Sistema de Deployment: Ondas 0-12 (AppGear Production-Ready Platform)
"""
import os
import re
from datetime import datetime
from typing import Dict

# Caminhos
SOURCE_FILE = "/home/paulo-lima/AppGear/README.md"
TARGET_FILE = "/home/paulo-lima/.github/profile/README.md"


def read_file(path: str) -> str:
    """Lê o conteúdo de um arquivo."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Erro ao ler arquivo {path}: {e}")
        raise


def write_file(path: str, content: str) -> None:
    """Escreve conteúdo em um arquivo."""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Erro ao escrever arquivo {path}: {e}")
        raise


def decode_url_text(text: str) -> str:
    """Decodifica texto com URL encoding."""
    return text.replace("%20", " ").replace("%E2%80%93", "–").replace("--", "–")


def extract_info(content: str) -> Dict:
    """Extrai informações do README.md fonte (Sistema de Ondas)."""
    info = {}

    # Versão do projeto
    version_patterns = [
        r"!\[Version\]\([^)]*?[Vv]ersion-([0-9]+\.[0-9]+\.[0-9]+)[^)]*?\)",
        r"\*\*Versão[:\s]+([0-9]+\.[0-9]+\.[0-9]+)\*\*",
    ]
    for pattern in version_patterns:
        if match := re.search(pattern, content):
            info["version"] = match.group(1)
            break

    # Status do projeto
    status_pattern = r"!\[Status\]\([^)]*?Status-([^-\)]+)-[^)]*?\)"
    if match := re.search(status_pattern, content, re.IGNORECASE):
        info["status"] = decode_url_text(match.group(1))

    # Sistema de Ondas (0-12)
    # Formato: ![Onda 0](https://img.shields.io/badge/Onda_0-Concluída-success)
    onda_pattern = r"!\[Onda\s+(\d+)\]\([^)]*?Onda[_\s]+\d+-([^-\)]+)-[^)]*?\)"
    onda_matches = re.findall(onda_pattern, content)

    if onda_matches:
        ondas = {}
        for onda_num, onda_status in onda_matches:
            ondas[int(onda_num)] = decode_url_text(onda_status)
        info["ondas"] = ondas
        info["total_ondas"] = len(ondas)

        # Determinar onda atual (última concluída ou em andamento)
        concluidas = [
            num
            for num, status in ondas.items()
            if "concluída" in status.lower() or "completa" in status.lower()
        ]
        if concluidas:
            info["onda_atual"] = max(concluidas)

    # Versão do Kubernetes
    k8s_patterns = [
        r"!\[Kubernetes\][^)]*?K8s-v([0-9]+\.[0-9]+\.[0-9]+)",
        r"Kubernetes.*?[vV]([0-9]+\.[0-9]+\.[0-9]+)",
        r"K3s.*?[vV]([0-9]+\.[0-9]+\.[0-9]+)",
    ]
    for pattern in k8s_patterns:
        if match := re.search(pattern, content):
            info["k8s_version"] = match.group(1)
            break

    # Contagem de serviços
    if match := re.search(r"\*\*Serviços Ativos\*\*.*?(\d+)", content):
        info["services_count"] = int(match.group(1))

    return info


def update_target(content: str, info: Dict) -> str:
    """Atualiza profile/README.md com informações extraídas."""
    months = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro",
    }
    now = datetime.now()
    today = f"{now.day:02d} de {months[now.month]} de {now.year}"

    new_content = content

    # Atualizar versão do projeto
    if "version" in info:
        new_content = re.sub(
            r"\*\*Versão\s+[0-9]+\.[0-9]+\.[0-9]+\*\*",
            f'**Versão {info["version"]}**',
            new_content,
        )
        print(f"  ✓ Versão: {info['version']}")

    # Atualizar data
    new_content = re.sub(
        r"Última atualização:\s+.*?(?=\n|$)",
        f"Última atualização: {today}",
        new_content,
        flags=re.MULTILINE,
    )
    print(f"  ✓ Data: {today}")

    # Atualizar status
    if "status" in info:
        new_content = re.sub(
            r"(!\[Status\]\(https://img\.shields\.io/badge/Status-)([^-]+)(-[^)]*?\))",
            rf'\g<1>{info["status"].replace(" ", "%20")}\g<3>',
            new_content,
        )
        print(f"  ✓ Status: {info['status']}")

    # Atualizar badges de Ondas
    if "ondas" in info:
        for onda_num, status in info["ondas"].items():
            # Atualiza o badge de cada onda
            pattern = rf"(!\[Onda\s+{onda_num}\]\(https://img\.shields\.io/badge/Onda_{onda_num}-)([^-]+)(-[^)]*?\))"
            new_content = re.sub(
                pattern, rf'\g<1>{status.replace(" ", "%20")}\g<3>', new_content
            )
        print(f"  ✓ Ondas: {info['total_ondas']} atualizadas")
        if "onda_atual" in info:
            print(f"    → Onda atual: {info['onda_atual']}")

    # Atualizar versão do Kubernetes
    if "k8s_version" in info:
        new_content = re.sub(
            r"(!\[Kubernetes\]\(https://img\.shields\.io/badge/K8s-)v([0-9]+\.[0-9]+\.[0-9]+)",
            rf'\g<1>v{info["k8s_version"]}',
            new_content,
        )
        print(f"  ✓ Kubernetes: v{info['k8s_version']}")

    return new_content


def main():
    """Função principal."""
    print("=" * 60)
    print("🌊 AppGear Profile Updater - Sistema de Ondas")
    print("=" * 60)

    if not os.path.exists(SOURCE_FILE):
        print(f"❌ Arquivo fonte não encontrado: {SOURCE_FILE}")
        return 1

    if not os.path.exists(TARGET_FILE):
        print(f"❌ Arquivo alvo não encontrado: {TARGET_FILE}")
        return 1

    try:
        print(f"\n📖 Lendo: {os.path.basename(SOURCE_FILE)}")
        source_content = read_file(SOURCE_FILE)

        print("🔍 Extraindo informações do sistema de Ondas...")
        info = extract_info(source_content)

        if not info:
            print("⚠️  Nenhuma informação extraída")
            return 1

        print(f"\n📄 Lendo: {os.path.basename(TARGET_FILE)}")
        target_content = read_file(TARGET_FILE)

        print("\n🔄 Atualizando conteúdo:")
        new_content = update_target(target_content, info)

        if new_content != target_content:
            write_file(TARGET_FILE, new_content)
            print(f"\n✅ Profile atualizado com sucesso!")
        else:
            print(f"\n✓ Nenhuma alteração necessária")

        print("=" * 60)
        return 0

    except Exception as e:
        print(f"\n❌ Erro: {e}")
        return 1


if __name__ == "__main__":
    try:
        import locale

        locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")
    except:
        pass

    exit(main())
