# LinkedIn Profile Optimizer

A Claude skill that optimizes LinkedIn profiles and helps you choose the right skills using LinkedIn's standardized skills taxonomy.

**Created by Daniel Rodrigues.**

---

## What it does

A strong LinkedIn profile has to work for two audiences: the search algorithm (keywords and standardized skills) and the human who decides in a few seconds whether to keep reading. This skill helps with both.

- **Profile diagnosis**: scores an existing profile against a prioritized checklist.
- **Headline**: 3 variations (role + value, keyword-focused, personal brand), within the 220-character limit.
- **About section**: structured template with a hook, proof points, key skills and a call to action.
- **Experience rewrite**: turns task lists into result-driven bullets (action verb + what + how + measurable result).
- **Skills selection**: builds a prioritized Top 50 list, with the 3 pinned skills marked, using standardized skill names.
- **Next steps**: the 3 highest-impact actions to take after the rewrite.

It works in **English and Portuguese (pt-BR)**.

## When it triggers

Claude uses the skill when you mention things like LinkedIn, headline, About section, skills or endorsements, recommendations, profile SEO, personal branding, career change, job search or recruiters. It also triggers when you paste a profile or resume for review.

## Example prompts

- "Review my LinkedIn profile and tell me what is hurting my visibility." *(paste the text)*
- "Write 3 headline options for a senior data analyst moving into product management."
- "Rewrite these job experiences with measurable results."
- "Suggest my top 50 LinkedIn skills for a Product Manager role in fintech."
- "Escreva o meu Sobre do LinkedIn em português, com foco em recrutadores de tecnologia."

## Installation

1. Download `linkedin-profile-optimizer.zip` (or the `.skill` file).
2. In Claude, open your settings and go to the **Skills** section.
3. Upload the file and enable the skill.

The exact menu names may vary depending on your Claude app or plan.

## Repository structure

```
linkedin-profile-optimizer/
├── SKILL.md                      # Instructions, workflow and output format
├── LICENSE.txt
├── references/
│   ├── checklist-perfil.md       # Profile diagnosis checklist
│   ├── modelos-secoes.md         # Templates: headline, About, experience, recommendations
│   └── taxonomia-skills.md       # Curated skills catalog by area + selection rules
└── scripts/
    └── buscar_skill.py           # Search a community skills list by keyword
```

## About the skills data

The skill uses a **curated catalog** of common LinkedIn skill names (AI and data, engineering, management, marketing and sales, leadership). It is not the complete official list.

An optional helper script can search a community-maintained list from the public repository [`maciejszewczyk/linkedin-skills`](https://github.com/maciejszewczyk/linkedin-skills):

```bash
# Download the community list (requires network access)
python scripts/buscar_skill.py --baixar linkedin_skills.txt

# Search for terms
python scripts/buscar_skill.py linkedin_skills.txt "Storytelling" "Project Management"
```

**Important:** that list is a community extraction (about 17,000 terms) and can be out of date. For example, newer terms such as `Prompt Engineering` were not found in it. If a term does not appear, it may still exist on LinkedIn. Always confirm the final name in LinkedIn's autocomplete when adding a skill.

## Principles

- **Results over tasks.** Metrics are used whenever available. When they are not, the skill marks estimates as `[confirm]` instead of inventing numbers.
- **No fabrication.** It never invents employers, titles, certifications or skills you do not have.
- **Natural keywords.** Search terms go into the headline, About, experience and skills without keyword stuffing.
- **Privacy.** It only works with text you provide and never asks for your LinkedIn password.
- **Terms of Service.** It does not recommend scraping or automation that violates LinkedIn's rules.

## Disclaimer

This is an independent project. It is not affiliated with, endorsed by or sponsored by LinkedIn or Microsoft. LinkedIn is a trademark of its respective owner.

## Author

Created by **Daniel Rodrigues**.
