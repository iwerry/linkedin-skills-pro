---
name: linkedin-profile-optimizer
description: Otimiza perfis do LinkedIn e escolhe as competências (skills) certas, usando a taxonomia padronizada da plataforma. Use SEMPRE que o usuário mencionar LinkedIn, perfil profissional, headline/título, seção Sobre (About), experiências, competências/skills, recomendações, SEO de perfil, posicionamento profissional, mudança de carreira ou recrutadores — mesmo que não peça explicitamente "otimizar o perfil". Também use para revisar um perfil colado ou enviado, escrever o Sobre, reescrever experiências com resultados, sugerir as 50 competências do perfil, ou planejar conteúdo/networking no LinkedIn. Criado por Daniel Rodrigues.
metadata:
  author: Daniel Rodrigues
  version: "1.0.0"
  language: pt-BR
---

# LinkedIn Profile Optimizer

Skill criada por **Daniel Rodrigues**. Ajuda a transformar um perfil do LinkedIn em algo encontrável por recrutadores (busca) e convincente para humanos (leitura).

## Por que o perfil funciona assim

O LinkedIn tem duas "audiências": o algoritmo de busca (que casa palavras-chave e competências padronizadas) e a pessoa que decide em poucos segundos se continua lendo. Um bom perfil serve às duas: usa os termos exatos que recrutadores pesquisam **e** conta uma história clara com resultados. Por isso, sempre trabalhe em ambas as frentes.

## Fluxo de trabalho

1. **Entender o objetivo.** Descubra (pergunte só o que faltar, no máximo 2–3 perguntas): cargo/área-alvo, senioridade, setor, idioma(s) do perfil, e se é busca ativa de emprego, freelancing, ou construção de marca pessoal. Se o usuário já colou o perfil ou CV, extraia isso dele antes de perguntar.
2. **Diagnosticar** o que existe (se houver) usando o checklist em `references/checklist-perfil.md`.
3. **Escolher competências** com `references/taxonomia-skills.md` (categorias, nomes padronizados e a regra das 50 skills).
4. **Redigir** cada seção seguindo `references/modelos-secoes.md`.
5. **Entregar** no formato abaixo, pronto para copiar e colar.

## Princípios de escrita

- **Resultado > tarefa.** "Reduzi o tempo de fechamento de 12 para 7 dias" vence "Responsável pelo fechamento". Se o usuário não tem números, pergunte ou use estimativas honestas marcadas como `[confirmar]`. Nunca invente métricas, empregadores, certificações ou títulos.
- **Primeira pessoa, tom humano.** Evite jargão vazio ("proativo", "orientado a resultados") sem prova.
- **Palavras-chave naturais.** Coloque os termos de busca no headline, Sobre, experiências e competências, sem empilhar.
- **Idioma.** Escreva no idioma do mercado-alvo. Para vagas internacionais, mantenha os nomes das competências em inglês (a taxonomia oficial é em inglês); para o Brasil, ofereça o perfil em português e, se fizer sentido, a versão em inglês.
- **Primeiras linhas importam.** O Sobre é cortado após ~3 linhas ("ver mais") e o headline aparece em toda busca e comentário: invista mais neles.

## Formato de entrega

Use esta estrutura, adaptando ao pedido (se o usuário pediu só uma seção, entregue só ela):

```
## Diagnóstico rápido
(3–5 pontos: o que está forte, o que está custando visibilidade)

## Headline (3 opções)
## Sobre
## Experiências (reescritas)
## Competências (Top 50 priorizadas + as 3 fixadas)
## Próximos passos (3 ações de maior impacto)
```

Para o headline, forneça 3 variações (ex.: foco em cargo+valor, foco em palavras-chave, foco em marca pessoal) com limite de 220 caracteres.

## Sobre a base de dados de competências

A taxonomia pública de competências do LinkedIn circula em repositórios abertos, como `maciejszewczyk/linkedin-skills` (um arquivo `linkedin_skills.txt` com a lista de skills; é uma extração comunitária e pode estar desatualizada). Por isso:

- Trate a lista como **referência de nomenclatura**, não como verdade oficial: o LinkedIn muda e adiciona termos. Em teste, a lista comunitária (~17 mil termos) não continha termos recentes como `Prompt Engineering`; se um termo atual não aparecer, ele ainda pode existir no LinkedIn, então confira no autocompletar.
- Se houver acesso à internet/rede e o usuário quiser a lista completa, baixe o arquivo e busque o termo exato com `scripts/buscar_skill.py` (veja o script). Se não houver acesso, use o catálogo curado em `references/taxonomia-skills.md` e avise que os nomes devem ser conferidos na caixa de busca do próprio LinkedIn ao adicionar (o autocompletar mostra o termo oficial).
- Outros materiais úteis para entender tendências: o relatório *Skills-First* do LinkedIn e o projeto `nestauk/skills-taxonomy-v2` (extração de skills a partir de anúncios). São contexto de mercado, não listas para copiar.

## Limites e boas práticas

- Nunca peça nem armazene senha do LinkedIn; esta skill só trabalha com texto que o usuário fornece.
- Não recomende automação/scraping que viole os Termos de Uso do LinkedIn. Sugira ações manuais ou ferramentas oficiais.
- Não infle competências que o usuário não tem: recrutadores testam isso em entrevistas e as recomendações/avaliações expõem a incoerência.
