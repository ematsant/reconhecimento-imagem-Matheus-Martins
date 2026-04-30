# Reconhecimento de Imagem com Machine Learning

Um projeto completo que demonstra **reconhecimento de imagem em tempo real** usando Teachable Machine do Google, com uma aplicação web interativa e exemplos práticos de código Python para aprendizado de Clean Code.

## 📋 Visão Geral do Projeto

Este projeto combina:
- **🎨 Aplicação Web**: Interface moderna para reconhecimento de imagem via webcam
- **🤖 Modelo ML**: Modelo treinado usando Teachable Machine (TensorFlow)
- **📚 Exemplos Python**: Código para aprendizado de debugging, Clean Code e refatoração

### Estrutura do Projeto

```
reconhecimento-imagem-Matheus-Martins/
├── index.html                    # Aplicação web principal
├── README.md                     # Este arquivo
├── my_model/
│   ├── model.json               # Modelo do TensorFlow
│   └── metadata.json            # Metadados do modelo (labels, versão)
└── teste-assistente-code/       # Exemplos e exercícios Python
    ├── debug.py                 # Código com erros (exercício de debug)
    ├── num_primos.py            # Verificador de primos (Clean Code)
    ├── refatoracao.py           # Análise estatística (código refatorado)
    ├── explicacao_debug.md      # Análise de erros em debug.py
    ├── explicacao_num_primo.md  # Análise técnica de números primos
    └── explicacao-refatoracao.md # Explicação de refatoração
```

---

## 🚀 Começando

### Requisitos

- Navegador web moderno com suporte a:
  - TensorFlow.js
  - Teachable Machine
  - Acesso à webcam

- Para exercícios Python:
  - Python 3.7+
  - Biblioteca `math` (padrão)

### Instalação

1. **Clone ou baixe o projeto**
   ```bash
   # Se estiver em um repositório Git
   git clone <seu-repositorio>
   cd reconhecimento-imagem-Matheus-Martins
   ```

2. **Abra a aplicação web**
   - Abra `index.html` em um navegador web
   - Permita o acesso à webcam quando solicitado

### Uso da Aplicação Web

1. **Interface Principal**
   - A aplicação carrega automaticamente o modelo de Machine Learning
   - Exibe a transmissão da webcam em tempo real
   - Mostra predicções em tempo real

2. **Funcionalidades**
   - ✅ Detecção de cores: **Azul**, **Vermelho**, **Verde**
   - 📊 Confiança da predição em percentual
   - 🔄 Processamento em tempo real

---

## 📊 Modelo de Machine Learning

### Configuração do Modelo

**Arquivo**: `my_model/metadata.json`

```json
{
  "modelName": "My image model",
  "labels": ["Azul", "Vermelho", "Verde"],
  "imageSize": 224,
  "tfjsVersion": "1.7.4",
  "tmVersion": "2.4.12",
  "timeStamp": "2026-04-22T22:09:28.423Z"
}
```

### Detalhes Técnicos

- **Tipo**: Classificador de Imagem (Transfer Learning)
- **Plataforma**: [Teachable Machine (Google)](https://teachablemachine.withgoogle.com/)
- **Tamanho da Entrada**: 224×224 pixels
- **Classes**: 3 labels de cores
- **Framework**: TensorFlow.js

---

## 💻 Exemplos Python

Acesse a pasta `teste-assistente-code/` para exemplos de código Python com foco educacional.

### 1. 🐛 Debug e Tratamento de Erros

**Arquivo**: `debug.py`

Um código intencional com erros para praticar debugging. Simula um sistema de faturamento com:
- Entrada de dados do cliente
- Cálculo de múltiplos itens
- Aplicação de impostos e descontos

**Erros a Identificar**:
- ❌ Aspas faltantes em strings
- ❌ F-strings não inicializadas
- ❌ Comparação tipo string vs número
- ❌ Indentação incorreta

**Análise**: Ver `explicacao_debug.md`

### 2. 🔢 Números Primos (Clean Code)

**Arquivo**: `num_primos.py`

Implementação profissional de um verificador de números primos seguindo princípios de **Clean Code**:

**Classe Principal: `PrimeChecker`**
```python
@staticmethod
def is_prime(number: int) -> bool:
    """Verifica se um número é primo com complexidade O(√n)"""
    cls.validate_input(number)
    # ... implementação otimizada
```

**Princípios Aplicados**:
- ✅ Nomes significativos
- ✅ Funções pequenas e focadas
- ✅ Type hints (Tipagem)
- ✅ Docstrings detalhadas
- ✅ Tratamento robusto de erros
- ✅ Testes automatizados

**Complexidade**: O(√n) - muito mais eficiente que verificar todos os divisores

**Análise Técnica**: Ver `explicacao_num_primo.md`

**Para Executar**:
```bash
python num_primos.py
```

### 3. 📈 Análise Estatística (Refatoração)

**Arquivo**: `refatoracao.py`

Código refatorado que demonstra boas práticas de estruturação:

**Funções**:

1. **`calcular_estatisticas(numeros)`**
   - Calcula: soma, média, máximo, mínimo
   - Retorna tupla com resultados
   - Usando funções built-in Python

2. **`exibir_resultado(soma, media, maximo, minimo)`**
   - Exibe resultados formatados
   - Separação de responsabilidades

3. **`main()`**
   - Ponto de entrada do programa
   - Executa análise em dataset exemplo

**Para Executar**:
```bash
python refatoracao.py
```

**Saída Esperada**:
```
Total: 356
Média: 35.6
Maior: 89
Menor: 2
```

**Análise**: Ver `explicacao-refatoracao.md`

---

## 🛠️ Tecnologias Utilizadas

### Frontend/Web
- **HTML5**: Estrutura da página
- **CSS3**: Styling com gradientes e efeitos modernos
- **TensorFlow.js**: Inferência de ML no navegador
- **Teachable Machine API**: Integração do modelo

### Backend/Python
- **Python 3.7+**: Linguagem principal
- **Type Hints**: Verificação de tipos
- **Docstrings**: Documentação de código
- **unittest** (implícito): Testes de validação

### Design
- **Dark Mode**: Tema escuro com contraste otimizado
- **Responsive**: Adapta-se a diferentes tamanhos de tela
- **Glassmorphism**: Efeitos visuais modernos

---

## 📚 Conceitos Aprendidos

Este projeto aborda:

### Engenharia de Software
- ✅ Clean Code principles
- ✅ Refatoração de código
- ✅ Debugging e tratamento de erros
- ✅ Type hints e tipagem estática
- ✅ Documentação de código (Docstrings)
- ✅ Separação de responsabilidades

### Machine Learning
- ✅ Transfer Learning
- ✅ Classificação de imagens
- ✅ TensorFlow.js (ML no navegador)
- ✅ Inferência em tempo real
- ✅ Tratamento de entrada (webcam)

### Python Best Practices
- ✅ Estrutura de classes
- ✅ Métodos estáticos vs de classe
- ✅ Validação de entrada
- ✅ Otimização de algoritmos (complexidade)
- ✅ Type hints e verificação de tipo

---

## 🎯 Objetivos Educacionais

1. **Compreender Debug**: Identificar e corrigir erros comuns
2. **Escrever Código Limpo**: Aplicar princípios SOLID e Clean Code
3. **Otimizar Algoritmos**: Entender complexidade e performance
4. **Implementar ML**: Usar modelos treinados em aplicações reais
5. **Integração Web+Python**: Conectar frontend e lógica de backend

---

## 📖 Recursos Adicionais

- [Teachable Machine - Google](https://teachablemachine.withgoogle.com/)
- [TensorFlow.js Documentation](https://www.tensorflow.org/js)
- [Clean Code em Python](https://www.oreilly.com/library/view/clean-code-in/9781491959633/)
- [Python Type Hints - PEP 484](https://www.python.org/dev/peps/pep-0484/)

---

## 📝 Notas de Desenvolvimento

- **Data do Modelo**: 22 de abril de 2026
- **Versão TensorFlow.js**: 1.7.4
- **Versão Teachable Machine**: 2.4.12
- **Autoria**: Matheus Martins

---

## 🤝 Contribuições

Este é um projeto educacional. Sugestões e melhorias são bem-vindas!

### Possíveis Melhorias
- [ ] Adicionar suporte a mais categorias de cores
- [ ] Implementar histórico de predições
- [ ] Criar interface para retreinar o modelo
- [ ] Adicionar testes automatizados para as funções Python
- [ ] Documentar mais exemplos de uso

---

## 📄 Licença

Este projeto é fornecido como material educacional.

---

**Desenvolvido com ❤️ para aprendizado de Machine Learning e Clean Code**
