## Úlohy
1. [Úloha 1](#p1)
2. [Úloha 2](#p2)
3. [Úloha 3](#p3)
4. [Úloha 4](#p4)
5. [Úloha 5](#p5)
6. [Úloha 6](#p6)
7. [Úloha 7](#p7)
8. [Úloha 8](#p8)
9. [Úloha 9](#p9)
10. [Úloha 10](#p10)
11. [Úloha 11](#p11)
12. [Úloha 12](#p12)
13. [Úloha 13](#p13)
14. [Úloha 14](#p14)
15. [Úloha 15](#p15)

## Úloha 1: Analýza fungovania modelov Vision Question Answering<a name="p1"></a>

Vision Question Answering (VQA) modely kombinujú spracovanie obrazu a prirodzeného jazyka, aby dokázali odpovedať na otázky týkajúce sa vizuálneho obsahu. Moderné prístupy využívajú hlboké neurónové siete – typicky CNN alebo Vision Transformers na extrakciu vizuálnych čŕt – a jazykové modely (LSTM, Transformer či Large Language Models) na spracovanie otázok, pričom multimodálne mechanizmy (napr. attention alebo spoločné embeddingy) prepájajú obe modality. Nachádzajú uplatnenie v oblastiach ako vyhľadávanie podľa obrázkov, asistívne technológie či vizuálne chatboty a smerujú k všeobecným multimodálnym AI systémom. Vašou úlohou bude analyzovať a vizualizovať fungovanie takéhoto modelu.

### Popis problému
Na katedre máme skúsenosti s modelom CheXagent, ktorý je určený na odpovedanie otázok týkajúcich sa röntgenových snímok hrudníka, konkrétne pľúc. Model dokáže riešiť viacero typov úloh, pričom v zadaní sa zameriame na generovanie lekárskych správ na základe obrazových dát. Cieľom zadania je prepojiť vygenerovanú správu so vstupným obrázkom, a to vyznačením tých oblastí, ktoré najviac prispeli ku generovanému textu.

Pri vypracovaní zadania sa oboznámite s problematikou:

* embedding,
* attention mechanizmus,
* vysvetliteľná umelá inteligencia,
* analýza fungovania hlbokých modelov.

### Očakávaný výstup
Používateľská aplikácia, v ktorej si používateľ môže vygenerovať lekársku správu a následne označiť niektoré slová v texte. Aplikácia potom vyznačí oblasti obrázka, ktoré zodpovedajú daným artefaktom alebo lekárskym záverom. Napríklad, ak sa v správe spomína nádor v ľavej hornej časti pľúc, táto oblasť sa automaticky zvýrazní.

### Literatúra
* [A Vision-Language Foundation Model to Enhance Efficiency of Chest X-ray Interpretation](https://arxiv.org/abs/2401.12208)
* [CXR-Agent: Vision-language models for chest X-ray interpretation with uncertainty aware radiology reporting](https://arxiv.org/abs/2407.08811)
* [Improving explainable AI with patch perturbation-based evaluation pipeline: a COVID-19 X-ray image analysis case study](https://www.nature.com/articles/s41598-023-46493-2)
* [Perturbation-based methods for explaining deep neural networks: A survey](https://www.sciencedirect.com/science/article/pii/S0167865521002440)

**Konzultant:** Ing. Ján Magyar, PhD.

## Úloha 2: Reasoning v hlbokých sieťach<a name="p2"></a>

Reasoning v hlbokých neurónových sieťach predstavuje schopnosť modelu analyzovať komplexné problémy, rozdeliť ich na menšie podúlohy a následne ich riešiť postupne alebo paralelne. Moderné modely, ako sú veľké jazykové a multimodálne modely, využívajú vnútorné mechanizmy pozornosti, hierarchické reprezentácie a tzv. chain-of-thought prístupy na systematické uvažovanie. Cieľom zadania je analyzovať, ako modely dokážu rozložiť zložitú úlohu na jednoduchšie kroky a ako tieto kroky prispievajú k výslednému rozhodnutiu.

### Popis problému
V zadaní sa zameriate na spracovanie úloh, ktoré vyžadujú viacstupňové uvažovanie – napríklad logické hádanky, matematické výpočty alebo otázky s viacerými podmienkami. Budete pracovať s modelom, ktorý sa pokúsi rozložiť problém na menšie podúlohy (napr. extrakcia faktov, odvodenie vzťahov, vyhodnotenie výsledku) a následne tieto kroky skombinuje do konečnej odpovede. Cieľom bude zabudovať do modelu a otestovať rôzne mechanizmy riešenia a číselne vyjadriť ich efekt na výkon modelu.

Pri vypracovaní zadania sa oboznámite s problematikou:
* reasoning v hlbokých sieťach
* dekompozícia úloh (task decomposition)
* attention a hierarchické reprezentácie
* interpretácia medzikrokov a rozhodnutí modelu

### Očakávaný výstup
Výskumný report s vybraným otestovaným modelom na aspoň troch ukážkových príkladoch a s porovnaním niekoľkých mechanizmov rôznych modulov hlbokého modelu.

**Konzultant:** Ing. Ján Magyar, PhD.

## Úloha 3: Detekcia udalostí počas futbalového zápasu pomocou grafových neurónových sietí<a name="p3"></a>

Detekcia udalostí počas futbalového zápasu pomocou grafových neurónových sietí (GNN) predstavuje moderný prístup k analýze športových dát, kde sa vzťahy medzi hráčmi a objektmi (napr. lopta) modelujú ako graf. GNN umožňujú efektívne zachytiť interakcie medzi entitami na ihrisku a odhaliť komplexné dynamické vzorce, ktoré vedú k rôznym herným situáciám. Cieľom zadania je vytvoriť model schopný automaticky identifikovať kľúčové udalosti, ako sú prihrávky, strely, rohové kopy, priame kopy a vhadzovania, na základe časopriestorových dát zo zápasu.

### Popis problému
V rámci zadania budete pracovať s dátami z futbalových zápasov, ktoré obsahujú polohy hráčov a lopty v čase. Tieto dáta je potrebné transformovať do grafovej reprezentácie, kde uzly predstavujú hráčov a loptu a hrany vyjadrujú ich vzájomné interakcie. Pomocou grafovej neurónovej siete sa následne budete snažiť detegovať, kedy dochádza k špecifickým herným udalostiam. Dôraz bude kladený na pochopenie vzťahov medzi pohybom hráčov, polohou lopty a výslednou akciou.

Pri vypracovaní zadania sa oboznámite s problematikou:
* grafové neurónové siete (Graph Neural Networks)
* reprezentácia časopriestorových dát
* modelovanie interakcií a dynamických vzťahov
* detekcia a klasifikácia udalostí v sekvenčných dátach

### Očakávaný výstup
Vizualizačná aplikácia, ktorá dokáže na základe vstupných pohybových dát identifikovať a znázorniť vybrané typy udalostí. Používateľ si bude môcť zobraziť priebeh zápasu s vizualizovanými interakciami medzi hráčmi a označenými udalosťami. Napríklad, ak model deteguje úspešnú prihrávku, aplikácia zvýrazní príslušných hráčov a dráhu lopty, ktorá k udalosti viedla.

**Konzultant:** Ing. Ján Magyar, PhD.

## Úloha 4: Generovanie komentára k športovým udalostiam pomocou multimodálnych modelov<a name="p4"></a>

Generovanie komentára k športovým udalostiam pomocou multimodálnych modelov predstavuje úlohu, pri ktorej sa spájajú vizuálne a časové informácie zo zápasu s jazykovým modelom schopným vytvárať textový popis priebehu hry. Takéto modely dokážu automaticky generovať komentáre k videu, sumarizovať herné situácie alebo poskytovať kontext pre konkrétne akcie hráčov. Cieľom zadania je navrhnúť systém, ktorý dokáže na základe videa alebo série snímok opísať, čo sa práve deje na ihrisku – napríklad „hráč prihráva na krídlo“ alebo „padol gól po strele spoza šestnástky“.

### Popis problému
V rámci zadania budete pracovať s multimodálnymi dátami – obrazovými sekvenciami (video alebo snímky) a doplnkovými informáciami o zápase (napr. poloha lopty, identita hráčov). Úlohou je prepojiť vizuálny vstup s jazykovým výstupom, teda vytvoriť model, ktorý pochopí priebeh situácie a dokáže k nej vygenerovať textový komentár. Dôraz sa kladie na synchronizáciu vizuálnych a jazykových čŕt a na to, aby model generoval gramaticky a obsahovo správne vety.

Pri vypracovaní zadania sa oboznámite s problematikou:
* multimodálne učenie (spojenie obrazu, zvuku a textu)
* transformerové architektúry pre generovanie textu
* spracovanie sekvenčných video dát
* hodnotenie kvality generovaného textu (BLEU, METEOR, ROUGE)

### Očakávaný výstup
Aplikácia, ktorá dokáže z krátkeho videozáznamu futbalovej situácie vygenerovať textový komentár. Používateľ si môže vybrať úsek zápasu a systém k nemu automaticky vytvorí stručný opis deja. Napríklad: po načítaní videa aplikácia vygeneruje vetu „hráč číslo 9 prihráva do šestnástky, hráč číslo 11 zakončuje a padá gól“.

**Konzultant:** Ing. Ján Magyar, PhD.

## Úloha 5: Semantic Segmentation with Capsule-ConvKAN:
Performance Analysis Against U-Net<a name="p5"></a>

### Literature Overview:
Capsule-ConvKAN combines a Convolutional Kolmogorov–Arnold Network (ConvKAN) as a feature extractor with Capsule Networks (CapsNet) for modeling part–whole hierarchies. Originally used for classification, ConvKAN can be extended into an encoder–decoder (UNet style) architecture for semantic segmentation. Capsules retained in the latent representation allow the model to preserve spatial hierarchies while the decoder reconstructs pixel-wise masks.

### Source of the Code:
1. Base Capsule-ConvKAN implementation (GitHub repository).
2. Optional references for U-Net and SegCaps for baseline comparisons.

### Platform:
* Google Colab or Hugging Face Spaces (lightweight experiments)
* DGX TUKE / HPC-Perun TUKE (for larger datasets)

### Dataset - Students can choose:
1. **MNIST Segmentation** (toy dataset, lightweight entry)
2. **CIFAR-10 Segmentation** (toy-scale object masks)
3. **Pascal VOC** (subset, 20 classes, moderate difficulty)
Dataset split: 70% train / 15% validation / 15% test

### Analytics:
* **Architecture Diagram**: ConvKAN encoder → Capsule bottleneck → decoder (UNet style)
* **Comparison**: Capsule-ConvKAN segmentation vs. U-Net vs. SegCaps
* **Experiment Variants**:
  * Capsule layer sizes
  * Routing mechanisms: Dynamic Routing vs. EM Routing
  * Capsules in bottleneck vs. capsules in bottleneck + decoder
* **Metrics**: Pixel Accuracy; mean Intersection over Union (mIoU); Dice coefficient; parameter count; FLOPs
* **Visualization**: Predicted masks vs. ground truth; training curves

### Results Analysis:
* Expected outcomes include **quantitative improvement** in boundary preservation and segmentation quality compared to standard U-Net.
* Analysis of **capsule configuration effects** on mIoU and Dice metrics.
* Ablation studies demonstrate the impact of routing mechanism, capsule size, and placement on segmentation performance.

### Expected Outcomes:
* Measured improvement of Capsule-ConvKAN segmentation over standard U-Net and SegCaps.
* Overleaf contribution: backbone diagram; segmentation performance table (mIoU, Dice); plots of metrics vs. model variants.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing

**Konzultant:** Bc. Laura Pituková

## Úloha 6: Semantic Segmentation with Pyramid Vision Transformer v2 (PVTv2): Performance Analysis Against ResNet-50<a name="p6"></a>

Literature Overview: Pyramid Vision Transformer v2 (PVTv2) introduces linear-complexity attention and overlapping patch embeddings, improving segmentation backbones.

Source of the Code: OpenGVLab / timm implementations.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: ADE20K (70/15/15).

Analytics: Diagram of pyramid stages and attention; comparison with Residual Network (ResNet50) backbone.

Results Analysis: Pixel Accuracy; mean Intersection over Union (mIoU); parameter count and floating-point operations (FLOPs).

Hugging Face availability: [https://huggingface.co/timm/pvt_v2_b2](https://huggingface.co/timm/pvt_v2_b2)

Expected outcomes:
* Measured mIoU improvement over ResNet-50 on same head.
* Overleaf contribution: backbone diagram; mIoU vs ResNet table; complexity vs accuracy plot.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 7: Comparative Analysis: BLIP-2 vs. OpenFlamingo for Image Captioning and Visual Question Answering<a name="p7"></a>

Literature Overview: BLIP-2 uses a frozen image encoder + a Query-Transformer (Q-Former) to bridge to a Large Language Model (LLM). OpenFlamingo is an open reproduction of Flamingo for interleaved image-text prompting.

Source of the Code: BLIP-2 in LAVIS / Transformers; OpenFlamingo organization on HF.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: MS-COCO captions + VQAv2 (70/15/15 subsets).

Analytics: Pipelines; decoding strategies (beam / nucleus); prompt engineering.

Results Analysis: CIDEr; BLEU-4; ROUGE-L; VQA accuracy; throughput & VRAM usage.

Hugging Face availability:
* [https://huggingface.co/Salesforce/blip2-flan-t5-xxl](https://huggingface.co/Salesforce/blip2-flan-t5-xxl)
* [https://huggingface.co/openflamingo/OpenFlamingo-4B-vitt-rpj3b](https://huggingface.co/openflamingo/OpenFlamingo-4B-vitt-rpj3b)

Expected outcomes:
* Benchmark table (captioning + VQA) with examples; recommendation for low- vs highcompute scenarios.
* Overleaf contribution: method diagrams, metrics plots, failure cases discussion.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 8: Conversational Image Understanding with LLaVA: Building a Vision-Language Chat Assistant<a name="p8"></a>

Literature Overview: LLaVA integrates a vision encoder + LLM to allow conversational tasks about images.

Source of the Code: LLaVA models on HF (via Transformers).

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: COCO-based instruction subset / curated eval set.

Analytics: Connector architecture; prompt format; latency & resource profiling.

Results Analysis: VQA accuracy; examples of dialogues; VRAM usage.

Hugging Face availability: [https://huggingface.co/llava-hf/llava-1.5-7b-hf](https://huggingface.co/llava-hf/llava-1.5-7b-hf)

Expected outcomes:
* Working chat-about-images demo; prompt guidelines.
* Overleaf contribution: architecture sketch, sample dialogs, performance table.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 9: Instruction-Tuned Visual QA: Evaluating InstructBLIP for Prompt-Following Visual Question Answering<a name="p9"></a>

Literature Overview: InstructBLIP fine-tunes BLIP-2 for instruction following in Visual Question Answering (VQA).

Source of the Code: InstructBLIP implementations in HF / LAVIS.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: VQAv2 subset; optional TextCaps.

Analytics: Prompt taxonomy; decoding (beam, nucleus); safety / grounding.

Results Analysis: VQA accuracy; prompt wording robustness; resource usage.

Hugging Face availability: [https://huggingface.co/Salesforce/instructblip-flan-t5-xxl](https://huggingface.co/Salesforce/instructblip-flan-t5-xxl)

Expected outcomes:
* Comparative study vs BLIP-2; prompt design guidelines.
* Overleaf contribution: prompt taxonomy figure, accuracy deltas, qualitative grid.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 10: Cross-Modal Retrieval and Zero-Shot Classification Using CLIP: Embedding Alignment Analysis<a name="p10"></a>

Literature Overview: CLIP trains image & text encoders in a contrastive manner enabling retrieval & zero-shot classification.

Source of the Code: OpenAI CLIP in Transformers / timm.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: Custom dataset (images + captions); ImageNet subset for zero-shot.

Analytics: Similarity computation; prompt engineering; embedding extraction.

Results Analysis: Recall@k; zero-shot accuracy top-1/top-5; prompt ablation.

Hugging Face availability: [https://huggingface.co/openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32)

Expected outcomes:
* Reproducible retrieval demo + zero-shot baseline + prompt templates.
* Overleaf contribution: retrieval curves; confusion / failure examples.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 11: Video Question Answering with LLaVA-Video: Temporal Understanding in Vision-Language Models<a name="p11"></a>

Literature Overview: Extends LLaVA to video: frame sampling + temporal understanding.

Source of the Code: HF models of LLaVA-Video family / LLaVA-NeXT-Video.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: MSRVTT or small curated video Q&A sets.

Analytics: Sampling strategy; temporal prompt tokens; evaluation protocol.

Results Analysis: QA accuracy; latency vs number of frames; example transcripts.

Hugging Face availability:
* [https://huggingface.co/LanguageBind/Video-LLaVA-7B-hf](https://huggingface.co/LanguageBind/Video-LLaVA-7B-hf)
* [https://huggingface.co/llava-hf/LLaVA-NeXT-Video-7B-hf](https://huggingface.co/llava-hf/LLaVA-NeXT-Video-7B-hf)

Expected outcomes:
* Video-Q&A notebook + demo; guidelines for frame usage.
* Overleaf contribution: pipeline diagram; frames-vs-quality tradeoff; example dialogs.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 12: Inception-v4 Architecture Implementation: Image Classification on CIFAR-100 Dataset<a name="p12"></a>

Literature Overview: Inception-v4 refines Inception modules and the network stem for better accuracy/efficiency.

Source of the Code: TensorFlow Models; PyTorch Image Models (timm) port.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: CIFAR-100 (70/15/15).

Analytics: Preprocessing → stem → Inception-A/B/C modules → classifier; training loop; data augmentation.

Results Analysis: Top-1 accuracy, confusion matrix, learning curves, error exemplars.

Hugging Face availability: [https://huggingface.co/timm/inception_v4](https://huggingface.co/timm/inception_v4)

Expected outcomes:
* Clean report + topology diagram; ≥70% top-1 (stretch 75%+) on CIFAR-100.
* Overleaf contribution: intro, methods diagram, curves, results table, discussion, references.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 13: Architectural Comparison: Inception-v3 vs. Inception-ResNet-v2 for Image Classification<a name="p13"></a>

Literature Overview: Inception-v3 (pure Inception) vs. Inception-ResNet-v2 (residualized).

Source of the Code: Keras Applications; timm ports.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE

Dataset: ImageNet subset (60/20/20).

Analytics: Two architecture charts; parameter counts and floating-point operations (FLOPs); training/inference flows.

Results Analysis: Accuracy, precision, recall, F1-score; latency & throughput; simple significance test.

Hugging Face availability:
* [https://huggingface.co/timm/inception_v3](https://huggingface.co/timm/inception_v3)
* [https://huggingface.co/timm/inception_resnet_v2](https://huggingface.co/timm/inception_resnet_v2)

Expected outcomes:
* Benchmark plots + table; recommendation for low-compute vs. best accuracy.
* Overleaf contribution: side-by-side diagrams, ablation table, recommendation.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 14: Medical Image Classification via Transfer Learning: Fine-tuning Inception-v3 on Chest XRays<a name="p14"></a>

Literature Overview: Fine-tuning Inception-v3 for medical images.
Source of the Code: Keras Applications (Inception-v3).

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE
Dataset: Public chest X-ray (70/15/15).

Analytics: Feature extraction → staged fine-tuning → classifier; regularization and schedule.

Results Analysis: Accuracy, sensitivity, specificity, AUC-ROC; calibration; Grad-CAM.

Hugging Face availability: [https://huggingface.co/timm/inception_v3](https://huggingface.co/timm/inception_v3)

Expected outcomes:
* AUC-ROC ≥0.85 on held-out test; interpretability gallery; short model card.
* Overleaf contribution: ROC + calibration figures, methods, ethics/fairness note.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.

## Úloha 15: Residual Networks in Practice: Implementing and Analyzing ResNet-50 on CIFAR-10<a name="p15"></a>

Literature Overview: Residual learning enables very deep supervised networks; ResNet-50 is the common baseline.

Source of the Code: TorchVision ResNet-50; timm variants.

Platform: Google Colab or Hugging Face, DGX TUKE, HPC-Perun TUKE
Dataset: CIFAR-10 (70/15/15).

Analytics: Residual block and skip-connection diagram; learning-rate schedule; data augmentation.

Results Analysis: Test accuracy, confusion matrix, precision/recall/F1; overfitting controls.

Hugging Face availability: [https://huggingface.co/timm/resnet50](https://huggingface.co/timm/resnet50)

Expected outcomes:
* ≥90% on CIFAR-10; learning-curve plots; augmentation ablation.
* Overleaf contribution: block diagram, results table, discussion on generalization.
* PowerPoint presentation and Microsoft Teams video recording for peer inspiration and knowledge sharing.

**Konzultant:** prof. Ing. Peter Sinčák, CSc.
