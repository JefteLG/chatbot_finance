
# Chatbot Finance - Relatório da saúde do modelo
## Índice
 - [Overview](#overview)
 - [Configurações](#config)
 - [Intenções](#intention)
 - [Entidades](#entity)
 - [Respostas](#response)

[Voltar para o início](../../index.md)

## Overview <a name='overview'></a>
|Bot|Versão|Rasa|Data de criação|Data de atualização|
|:-:|:-:|:-:|:-:|:-:|
|<span style='font-size:16px'>**chatbot_finance**</span>|            <span style='font-size:16px'>local</span>|            <span style='font-size:16px'>2.8.25</span>|            <span style='font-size:16px'>11/04/23 12:34:32</span>|            <span style='font-size:16px'>11/04/23 12:34:32</span>|

|Intenção|Entidade|Resposta|<span style='font-size:20px'>Geral</span>|
|:-:|:-:|:-:|:-:|
|100.00            |0.00            |100.00            |<span style='font-size:20px'>**100.00**</span>|
|🟢            |❌            |🟢            |<span style='font-size:20px'>🟢</span>|

## Configurações <a name='config'></a>
Configurações que foram utilizadas na *pipeline* de treinamento e nas *policies*.
```yaml
# The config recipe.
# https://rasa.com/docs/rasa/model-configuration/
recipe: default.v1

# Configuration for Rasa NLU.
# https://rasa.com/docs/rasa/nlu/components/
language: pt

pipeline:
# No configuration for the NLU pipeline was provided. The following default pipeline was used to train your model.
# If you'd like to customize it, uncomment and adjust the pipeline.
# See https://rasa.com/docs/rasa/tuning-your-model for more information.
  - name: SpacyNLP
    model: pt_core_news_lg
    case_sensitive: False
  - name: SpacyTokenizer
  - name: SpacyFeaturizer
  - name: RegexFeaturizer
    case_sensitive: false
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: word
    lowercase: true
    strip_accents: unicode
  - name: CountVectorsFeaturizer
    analyzer: char_wb
    lowercase: true
    max_ngram: 4
    min_ngram: 1
    strip_accents: unicode
  - name: DIETClassifier
    epochs: 100
    constrain_similarities: true
  - name: EntitySynonymMapper
  - name: FallbackClassifier
    ambiguity_threshold: 0.1
    threshold: 0.8

# Configuration for Rasa Core.
# https://rasa.com/docs/rasa/core/policies/
policies:
# No configuration for policies was provided. The following default policies were used to train your model.
# If you'd like to customize them, uncomment and adjust the policies.
# See https://rasa.com/docs/rasa/policies for more information.
  - name: TEDPolicy
    max_history: 4
    epochs: 200
    constrain_similarities: true
  - name: UnexpecTEDIntentPolicy
    epochs: 250
    max_history: 3
    tolerance: 0
    ignore_intents_list: [saudar, noticia, start, rastreio_notificacao, ajuda, valor_ativo, menu, gerenciar_notificacao, rastrear_ativos, remover_ativos, adicionar_ativos]
  - name: RulePolicy
    core_fallback_action_name: action_custom_fallback
    core_fallback_threshold: 0.8
    enable_fallback_prediction: true
  - name: AugmentedMemoizationPolicy
    max_history: 3

```

## Intenções <a name='intention'></a>
Seção que aborda métricas sobre as intenções do modelo.

### Métricas
Tabela com as métricas das intenções.
||Intenção|Precisão|Recall|F1 Score|Número de exemplos|
|-|-|-|-|-|-|
|🟢|gerenciar_notificacao|100.0%|100.0%|100.0%|17|
|🟢|ajuda|100.0%|100.0%|100.0%|11|
|🟢|afirmar|100.0%|100.0%|100.0%|15|
|🟢|valor_ativo|100.0%|100.0%|100.0%|19|
|🟢|negar|100.0%|100.0%|100.0%|15|
|🟢|saudar|100.0%|100.0%|100.0%|18|
|🟢|noticia|100.0%|100.0%|100.0%|10|
|🟢|rastrear_ativos|100.0%|100.0%|100.0%|18|
|🟢|menu|100.0%|100.0%|100.0%|8|
|🟢|micro avg|100.0%|100.0%|100.0%|131|

### Intenções confusas
Aqui vão constar todas as frases confusas ou erradas do modelo.

Não foram encontradas confusões ou erros de intenções nesse modelo.
### Histograma
![Histograma](intent_histogram.png 'Teste')
### Matriz de Confusão
![Matriz de Confusão](intent_confusion_matrix.png 'Teste')

## Entidades <a name='entity'></a>
Seção que aborda métricas sobre as entidades do modelo.

### Métricas
Tabela com as métricas das entidades.


Não foram encontradas entidades nesse modelo.

### Entidades confusas
Aqui vão constar todas as entidades confusas ou erradas do modelo.

Não foram encontradas confusões ou erros de intenções nesse modelo.

## Respostas <a name='response'></a>
Seção que aborda métricas sobre as respostas e histórias do bot.

### Métricas
Tabela com as métricas das respostas do bot.

||Resposta|Precisão|Recall|F1 Score|Número de ocorrências|
|-|-|-|-|-|-|
|🟢|action_add_ativo|100.0%|100.0%|100.0%|2|
|🟢|utter_menu|100.0%|100.0%|100.0%|5|
|🟢|action_greet_init|100.0%|100.0%|100.0%|3|
|🟢|action_active_activate|100.0%|100.0%|100.0%|1|
|🟢|action_news|100.0%|100.0%|100.0%|1|
|🟢|utter_ajuda_2|100.0%|100.0%|100.0%|1|
|🟢|utter_activate_negative|100.0%|100.0%|100.0%|1|
|🟢|action_reset_slots|100.0%|100.0%|100.0%|17|
|🟢|action_fim_remover_ativo|100.0%|100.0%|100.0%|1|
|🟢|utter_ajuda_1|100.0%|100.0%|100.0%|1|
|🟢|action_manage_notification|100.0%|100.0%|100.0%|2|
|🟢|utter_news|100.0%|100.0%|100.0%|3|
|🟢|action_active|100.0%|100.0%|100.0%|2|
|🟢|utter_menu_ativos|100.0%|100.0%|100.0%|11|
|🟢|action_remover_ativo|100.0%|100.0%|100.0%|4|
|🟢|action_listen|100.0%|100.0%|100.0%|55|
|🟢|utter_active|100.0%|100.0%|100.0%|5|
|🟢|utter_active_not_activate|100.0%|100.0%|100.0%|1|
|🟢|action_fim_add_active|100.0%|100.0%|100.0%|1|
|🟢|action_activate_affirm|100.0%|100.0%|100.0%|1|
### Matriz de Confusão
![Matriz de Confusão](story_confusion_matrix.png 'Teste')
