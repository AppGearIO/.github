<div align="center">
  <img src="https://raw.githubusercontent.com/AppGearIO/.github/main/profile/assets/AppGear.png" alt="AppGear Logo" width="200"/>
  <h1>AppGear.io</h1>
  <p><strong>Plataforma Kubernetes Production-Ready para Desenvolvimento Avançado</strong></p>

  [![Status](https://img.shields.io/badge/Status-Em%20Implementação--Ready-success?style=for-the-badge)](https://appgear.io)
  [![Fase 1](https://img.shields.io/badge/Fase_1-Concluída-blue?style=for-the-badge)](https://github.com/AppGearIO/AppGear)
  [![Fase 2](https://img.shields.io/badge/Fase_2-Concluída-blue?style=for-the-badge)](https://github.com/AppGearIO/AppGear)
  [![Fase 3](https://img.shields.io/badge/Fase_3-Concluída-blue?style=for-the-badge)](https://github.com/AppGearIO/AppGear)
  [![Fase 4](https://img.shields.io/badge/Fase_4-Concluída-blue?style=for-the-badge)](https://github.com/AppGearIO/AppGear)
  [![Kubernetes](https://img.shields.io/badge/K8s-v1.33.6-326CE5?style=for-the-badge&logo=kubernetes)](https://kubernetes.io)
  [![Made in Brazil](https://img.shields.io/badge/Made%20in-Brazil-green?style=for-the-badge&logo=brazil)](https://github.com/AppGearIO)
</div>

---

## 🚀 Sobre o AppGear

AppGear é uma plataforma completa de desenvolvimento que oferece infraestrutura robusta com **Kubernetes**, **IA integrada** e **observabilidade completa**. Projetada para acelerar o desenvolvimento de aplicações modernas com as melhores práticas DevOps.

## 📊 Status Atual

### Sistema em Produção ✨

| Métrica | Valor | Observação |
|---------|-------|------------|
| **Serviços Ativos** | 11 | Core + Infrastructure |
| **Pods Running** | 13 | Todos healthy ✅ |
| **Namespaces** | 4 | appgear, observability, ingress-nginx, cert-manager |
| **Storage** | 45 Gi | Persistente com política Retain |
| **Uptime** | 46+ horas | Zero restarts |
| **Alta Disponibilidade** | ✅ Ativo | LiteLLM 2x réplicas |

### Progresso de Fases

| Fase | Topologia | Status | Foco |
| :--- | :--- | :--- | :--- |
| **Fase 1** | **Minimal (Docker Compose)** | ✅ **Concluída** | Desenvolvimento rápido, PoC |
| **Fase 2** | **Standard (Kubernetes)** | ✅ **Concluída** | Core, Observabilidade, Escalabilidade |
| **Fase 3** | **Full (Service Mesh)** | ✅ **Concluída** | Istio, Multi-tenancy, Business Dashboards |
| **Fase 4** | **Enterprise** | ✅ **Concluída - ATIVO** | Multi-cluster, GitOps, Disaster Recovery |

## 🛠️ Stack Tecnológica

### Core Services (9 serviços)

**Aplicações:**
- 🤖 **LiteLLM** (2x HA) - AI Gateway com suporte multi-provider
- 🌊 **Flowise** - AI Workflow Builder
- 🔄 **n8n** - Automação avançada
- 💻 **Platform** - Admin Panel (Next.js)
- 🛡️ **Coraza WAF** - Web Application Firewall

**Dados:**
- 🐘 **PostgreSQL** - Banco de dados (10Gi PVC)
- 🔴 **Redis** - Cache e sessões (5Gi PVC)

**Observabilidade:**
- 📊 **Prometheus** - Coleta de métricas (10Gi PVC)
- 📈 **Grafana** - Dashboards e visualização (5Gi PVC)

### Infrastructure Services (2 serviços)

- 🌐 **NGINX Ingress Controller** - Roteamento HTTP/HTTPS
- 🔐 **Cert-Manager** - Gerenciamento automático de certificados SSL/TLS

### Tecnologias Base

- **Orquestração:** Kubernetes (K3s v1.33.6)
- **Acesso:** Dual-mode (NodePort para dev + Ingress HTTPS para produção)
- **Monitoramento:** Prometheus + Grafana com baseline de 15min
- **Segurança:** Coraza WAF, Cert-Manager, TLS automático
- **Storage:** 45Gi persistente com política Retain (proteção contra deleção)

## 🔌 Modos de Acesso

### 🔧 Desenvolvimento (NodePort)
Acesso direto via `localhost` - 7 serviços expostos em portas NodePort

### 🚀 Produção (Ingress HTTPS)
Acesso via domínio com certificados SSL/TLS automáticos (Let's Encrypt)
- Configurado e pronto para ativação
- Aguardando apenas configuração DNS

## 🔗 Links Importantes

- [🌐 Website](https://appgear.io)
- [📂 Repositório Principal](https://github.com/AppGearIO/AppGear)
- [📄 Documentação](https://docs.appgear.io)
- [📊 Status Detalhado](https://github.com/AppGearIO/AppGear/blob/main/CURRENT-STATUS.md)

---

<div align="center">
  
**AppGear - Production-Ready Kubernetes Platform**

Desenvolvido com ❤️ e 🇧🇷 pela Equipe AppGear

**Versão 0.1.0** • Última atualização: 10 de dezembro de 2025

</div>
