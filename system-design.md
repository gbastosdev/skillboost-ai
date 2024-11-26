# SkillBoost AI - System Design

## 1. Requisitos Funcionais

### Funcionalidades Básicas:
1. Geração de desafios diários/semanal alternando front-end/back-end.
2. Auxílio de AI para solução do problema.
### Próximas features:
1. Personalização de desafios com base no nível do usuário.
2. Sistema de gamificação (pontuação, badges, rankings).
3. Relatórios de progresso do usuário.
4. Sistema de login e gerenciamento de contas.

### Não Funcionais:
1. Alta disponibilidade e escalabilidade para suportar muitos usuários.
2. Resposta rápida na geração de desafios.

---

## 2. Arquitetura de Alto Nível

A arquitetura será baseada em **microserviços** para maior escalabilidade e modularidade:

```
[Client] <-> [API Gateway] <-> [Microservices] <-> [Database + Cache] <-> [AI Service]
```

---

## 3. Componentes do Sistema

### **Frontend (Client):**
- **Tecnologia:** React-Native.
- **Responsabilidade:**
  - Interface do usuário para desafios. (login e navegação -> próximas etapas)
  - Consumo de APIs para exibir desafios.
  <!-- - Atualização em tempo real do progresso e ranking. -->

### **Backend:**

#### **API Gateway:**
- **Tecnologia:** FastAPI -> **GraphQL/REST APIs**.
- **Função:**
  - Roteamento das requisições para os microserviços corretos.
  <!-- - Gerenciamento de autenticação e autorização. -->

#### **Microserviços Principais:**

1. **Challenge Service:**
   - Gerencia a criação e o armazenamento dos desafios.
   - Define os níveis de dificuldade (fácil, médio, difícil).
   - Alternância lógica entre front-end e back-end.
   - Banco: MongoDB.

2. **AI Service:**
   - Modelo baseado no GPT (ou similar) para gerar desafios dinâmicos.
   - Feedback personalizado com base no envio do usuário.
   - Treinamento adicional com base nos resultados dos desafios dos usuários.
   - Auxílio com o usuário, através de uma aba, que poderá enviar dicas para ajudá-lo no processo.

<!-- 1. **User Service:**
   - Gerencia contas, autenticação (OAuth 2.0/JWT), perfis e configurações.
   - Integração com serviços externos (Google, GitHub).
   - Banco: MongoDB ou PostgreSQL. -->

<!-- 2. **Analytics Service:**
   - Gera relatórios de progresso para usuários e empresas.
   - Banco: BigQuery (ou semelhante) para análises em larga escala. -->

---

## 4. Fluxo de Dados

2. **Requisição de um Novo Desafio:**
   - Frontend -> API Gateway -> Challenge Service.
   - Challenge Service consulta o AI Service para gerar um desafio e armazenar no banco.
   - Desafio é retornado ao usuário.

<!-- 1. **Usuário Loga no Sistema:**
   - Frontend -> API Gateway -> User Service.
   - Autenticação via JWT. -->

<!-- 3. **Envio de Solução:**
   - Usuário envia solução via Frontend.
   - API Gateway -> Challenge Service -> AI Service.
   - AI Service avalia, retorna feedback e armazena o resultado.

4. **Atualização de Gamificação:**
   - Feedback gera pontos no Gamification Service.
   - Redis atualiza ranking em tempo real.

5. **Relatórios de Progresso:**
   - Analytics Service processa e fornece relatórios via API Gateway. -->

---

## 5. Diagrama Resumido

1. **Frontend:**
   - React-Native -> Consome APIs.

2. **Backend:**
   - Microserviços: Challenge e AI.
   - Banco de Dados: MongoDB.

3. **Infraestrutura:**
   - Docker, Kubernetes, AWS (EC2, S3, RDS).

4. **Fluxo Exemplo:**
   - Requisição -> Gateway -> Microserviço -> AI/DB -> Resposta.

---

<!-- ## 6. Segurança

1. **Autenticação:**
   - OAuth 2.0 + JWT para login seguro.

2. **Criptografia:**
   - HTTPS para todas as comunicações.
   - Criptografia de senhas (bcrypt).

3. **Controle de Acesso:**
   - Roles (usuário comum, empresa). -->

---

<!-- ## 7. Escalabilidade e Alta Disponibilidade

1. **Load Balancer:**
   - Distribui tráfego entre instâncias backend.

2. **Auto-scaling:**
   - Kubernetes ajusta a quantidade de pods conforme a demanda.

3. **Cache:**
   - Redis para acelerar respostas de dados acessados com frequência.

4. **CDN:**
   - Para entrega rápida de conteúdo estático. -->

---
