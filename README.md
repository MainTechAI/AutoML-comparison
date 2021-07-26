# AutoML-comparison (Under development)

Some of the definitions (or all) given in this project may be changed later. The same applies to the project structure.

## Methods
Describe environment, data sources, data preprocessing steps, etc

### Datasets

List of used datasets

| ID | Dataset | Shape | Size | Task | Info |
|:---------:|:----------------|:---------:|:---------:|:---------:|:---------:|
| 1 | [Airlines]() | 539383 × 8 | 19.2 MB | Classification (binary) |  |
| 2 | [Amazon employee access]() | 32769 × 10 | 2.0 МB | Classification (binary) |  |
| 3 | [Blood transfusion service center]() | 748 × 5 | 10.5 КB | Classification (binary) |  |
| 4 | [CIFAR_10](https://www.openml.org/d/40927) | 12000 × 3073 | 131.9 МB | Classification (binary) | Images |
| 5 | [Connect 4 (balanced)]() | 46168 × 43 | 4.0 МB | Classification (binary) |  |
| 6 | [Connect 4 (imbalanced)]() | 67557 × 43 | 5.8 МB | Classification (binary) |  |
| 7 | [Fashion-MNIST](https://www.openml.org/d/40996) | 14000 × 785 | 32.0 МB | Classification (binary) | Images |
| 8 | [Jungle chess]() | 44819 × 7 | 609.3 КB | Classification (binary) |  |
| 9 | [kc1]() | 2109 × 22 | 192.2 КB | Classification (binary) |  |
| 10 | [KDDCup09 appetency]() | 50000 × 231 | 34.4 МB | Classification (binary) |  |
| 11 | [Vehicle](https://www.openml.org/d/54) | 434 × 19 | 29.1 КB | Classification (binary) | - |


## Results
Performance on each dataset

| AutoML system | Dataset 1 | Dataset 2 | Dataset 3 |
|:----------------|:---------:|:---------:|:---------:|
| auto-sklearn | - | - | - |
| H2O (AutoML) | - | - | - |
| TPOT         | - | - | - |
|  |  |  |  |

### Auto-WEKA  
Python wrapper: https://github.com/fracpete/python-weka-wrapper3
Weka installation: https://waikato.github.io/weka-wiki/downloading_weka/


## Open-source AutoML projects
AutoML systems focus on using Machine Learning algorithms. For example: SVM, GLM, decision tree based algorithms (DT, RF, GB), etc. Neural Networks can also be used. 

| Name | Repository | Documentation | Stats | Papers | License |
|:---------|:---------|:---------|:---------:|:---------|:---------|
| auto-sklearn | [Repository](https://github.com/automl/auto-sklearn) | [Documentation](https://automl.github.io/auto-sklearn/master/)             | ![Lines of code](https://img.shields.io/tokei/lines/github/automl/auto-sklearn?style=flat-square) | [Paper 1](http://papers.nips.cc/paper/5872-efficient-and-robust-automated-machine-learning.pdf), [Paper 2](https://arxiv.org/abs/2007.04074) | BSD-3-Clause 
| H2O (AutoML) | [Repository](https://github.com/h2oai/h2o-3)         | [Documentation](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html) | ![Lines of code](https://img.shields.io/tokei/lines/github/h2oai/h2o-3?style=flat-square)         | [Paper](https://www.automl.org/wp-content/uploads/2020/07/AutoML_2020_paper_61.pdf)                                                          | Apache-2.0
| TPOT         | [Repository](https://github.com/EpistasisLab/tpot)   | [Documentation](http://epistasislab.github.io/tpot/)                       | ![Lines of code](https://img.shields.io/tokei/lines/github/EpistasisLab/tpot?style=flat-square)   | [Paper 1](https://academic.oup.com/bioinformatics/article/36/1/250/5511404), [Paper 2](https://dl.acm.org/doi/10.1145/2908812.2908918)       | LGPL-3.0
| hyperopt-sklearn | [Repository](https://github.com/hyperopt/hyperopt-sklearn) | [Documentation](https://hyperopt.github.io/hyperopt-sklearn/) | ![Lines of code](https://img.shields.io/tokei/lines/github/hyperopt/hyperopt-sklearn?style=flat-square) | [Paper 1](http://conference.scipy.org/proceedings/scipy2014/pdfs/komer.pdf) | BSD-3-Clause  |
| Auto-WEKA | [Repository](https://github.com/automl/autoweka) | [Documentation](http://www.cs.ubc.ca/labs/beta/Projects/autoweka/manual.pdf) | ![Lines of code](https://img.shields.io/tokei/lines/github/automl/autoweka?style=flat-square)  | [Paper 1](http://www.cs.ubc.ca/labs/beta/Projects/autoweka/papers/autoweka.pdf), [Paper 2](http://www.cs.ubc.ca/labs/beta/Projects/autoweka/papers/16-599.pdf) | GPL-3.0 |
| AutoGluon | [Repository](https://github.com/awslabs/autogluon)| [Documentation](https://auto.gluon.ai/) | ![Lines of code](https://img.shields.io/tokei/lines/github/awslabs/autogluon?style=flat-square) | [Paper](https://arxiv.org/abs/2003.06505) | Apache-2.0 |
| GAMA | [Repository](https://github.com/PGijsbers/gama) | [Documentation](https://pgijsbers.github.io/gama/master/) | ![Lines of code](https://img.shields.io/tokei/lines/github/PGijsbers/gama?style=flat-square) | [Paper](https://arxiv.org/abs/2007.04911) | Apache-2.0 |
| OBOE | [Repository](https://github.com/udellgroup/oboe)| [Examples](https://github.com/udellgroup/oboe/tree/master/examples) |  ![Lines of code](https://img.shields.io/tokei/lines/github/udellgroup/oboe?style=flat-square) | [Paper](https://people.ece.cornell.edu/cy/_papers/oboe.pdf) | BSD-3-Clause |
| LAMA | [Repository](https://github.com/sberbank-ai-lab/LightAutoML) | [Documentation](https://lightautoml.readthedocs.io/en/latest/) | ![Lines of code](https://img.shields.io/tokei/lines/github/sberbank-ai-lab/LightAutoML?style=flat-square) | - | Apache-2.0 |
| WhiteBoxAutoML | [Repository](https://github.com/sberbank-ai-lab/AutoMLWhitebox) | - | ![Lines of code](https://img.shields.io/tokei/lines/github/sberbank-ai-lab/AutoMLWhitebox?style=flat-square) | - | Apache-2.0 |
| mljar-supervised | [Repository](https://github.com/mljar/mljar-supervised) | [Documentation](https://supervised.mljar.com/) | ![Lines of code](https://img.shields.io/tokei/lines/github/mljar/mljar-supervised?style=flat-square) | - | MIT |
| PyCaret | [Repository](https://github.com/pycaret/pycaret) | [Documentation](https://pycaret.readthedocs.io/en/latest/) | ![Lines of code](https://img.shields.io/tokei/lines/github/pycaret/pycaret?style=flat-square) | - | MIT |
| MLBox | [Repository](https://github.com/AxeldeRomblay/MLBox) | [Documentation](https://mlbox.readthedocs.io/en/latest/) | ![Lines of code](https://img.shields.io/tokei/lines/github/AxeldeRomblay/MLBox?style=flat-square) | - | BSD-3-Clause |
| auto_ml | [Repository](https://github.com/ClimbsRocks/auto_ml) | [Documentation](https://auto-ml.readthedocs.io/en/latest/) | ![Lines of code](https://img.shields.io/tokei/lines/github/ClimbsRocks/auto_ml?style=flat-square) | - | MIT |
| Pennai | [Repository](https://github.com/EpistasisLab/pennai) | [Documentation](https://epistasislab.github.io/pennai/) | ![Lines of code](https://img.shields.io/tokei/lines/github/EpistasisLab/pennai?style=flat-square) | [Paper](https://doi.org/10.1093/bioinformatics/btaa698) | GPL-3.0 |
| ML-Plan | [Repository](https://github.com/starlibs/AILibs) | [Documentation](https://starlibs.github.io/AILibs/projects/mlplan/) | ![Lines of code](https://img.shields.io/tokei/lines/github/starlibs/AILibs?style=flat-square) | [Paper](https://doi.org/10.1007/s10994-018-5735-z) | AGPL-3.0 |
| TransmogrifAI | [Repository](https://github.com/salesforce/TransmogrifAI) | [Documentation](https://docs.transmogrif.ai/en/stable/) | ![Lines of code](https://img.shields.io/tokei/lines/github/salesforce/TransmogrifAI?style=flat-square) | - | BSD-3-Clause |
| autoxgboost | [Repository](https://github.com/ja-thomas/autoxgboost) | [Example](https://github.com/ja-thomas/autoxgboost/blob/master/poster_2018.pdf) | ![Lines of code](https://img.shields.io/tokei/lines/github/ja-thomas/autoxgboost?style=flat-square) | [Paper](https://arxiv.org/abs/1807.03873v2) | ? |
| NNI | [Repository](https://github.com/microsoft/nni) | [Documentation](https://nni.readthedocs.io/en/stable/) | ![Lines of code](https://img.shields.io/tokei/lines/github/microsoft/nni?style=flat-square) | [Papers](https://nni.readthedocs.io/en/latest/ResearchPublications.html) | MIT |
| Recipe | [Repository](https://github.com/laic-ufmg/Recipe) | [Documentation](https://laic-ufmg.github.io/Recipe/docs/) | ![Lines of code](https://img.shields.io/tokei/lines/github/laic-ufmg/Recipe?style=flat-square) | [Paper](https://doi.org/10.1007/978-3-319-55696-3_16) | GPL-3.0 |
| Xcessiv | [Repository](https://github.com/reiinakano/xcessiv) | [Documentation](https://xcessiv.readthedocs.io/en/stable/) | ![Lines of code](https://img.shields.io/tokei/lines/github/reiinakano/xcessiv?style=flat-square) | - | Apache-2.0 |
| ATM | [Repository](https://github.com/HDI-Project/ATM) | [Documentation](https://hdi-project.github.io/ATM/index.html) | ![Lines of code](https://img.shields.io/tokei/lines/github/HDI-Project/ATM?style=flat-square) | [Paper](https://dai.lids.mit.edu/wp-content/uploads/2018/02/atm_IEEE_BIgData-9-1.pdf) | MIT |
| PMF | [Repository](https://github.com/rsheth80/pmf-automl) | - | ![Lines of code](https://img.shields.io/tokei/lines/github/rsheth80/pmf-automl?style=flat-square) | [Paper](http://papers.neurips.cc/paper/7595-probabilistic-matrix-factorization-for-automated-machine-learning) | BSD-3-Clause |
| | | | | | |



## Open-source AutoDL projects
Let's assume that AutoDL is a subset of AutoML. AutoDL systems focus only (or mainly) on using Deep Learning algorithms. Also assume that NAS is a part of AutoDL.

| Name | Repository | Documentation | Stats | Papers | License |
|:---------|:---------|:---------|:---------:|:---------|:---------|
| Auto-PyTorch | [Repository](https://github.com/automl/Auto-PyTorch) | [Examples](https://github.com/automl/Auto-PyTorch/tree/master/examples/basics) | ![Lines of code](https://img.shields.io/tokei/lines/github/automl/Auto-PyTorch?style=flat-square) | [Paper 1](https://arxiv.org/abs/2006.13799), [Paper 2](https://ml.informatik.uni-freiburg.de/papers/16-AUTOML-AutoNet.pdf) | Apache-2.0 |
| AutoKeras | [Repository](https://github.com/keras-team/autokeras) | [Documentation](https://autokeras.com/) | ![Lines of code](https://img.shields.io/tokei/lines/github/keras-team/autokeras?style=flat-square) | [Paper](https://dl.acm.org/doi/10.1145/3292500.3330648) | Apache-2.0 |
| DEvol | [Repository](https://github.com/joeddav/devol) | [Example](https://github.com/joeddav/devol/tree/master/example) | ![Lines of code](https://img.shields.io/tokei/lines/github/joeddav/devol?style=flat-square) | - | MIT |
| Ludwig | [Repository](https://github.com/ludwig-ai/ludwig) | [Documentation](https://ludwig-ai.github.io/ludwig-docs/) | ![Lines of code](https://img.shields.io/tokei/lines/github/ludwig-ai/ludwig?style=flat-square) | [Paper](https://arxiv.org/abs/1909.07930) | Apache-2.0 |
| MindsDB | [Repository](https://github.com/mindsdb/mindsdb) | [Documentation](https://docs.mindsdb.com/) | ![Lines of code](https://img.shields.io/tokei/lines/github/mindsdb/mindsdb?style=flat-square) | ? | GPL-3.0 |
| Lightwood | [Repository](https://github.com/mindsdb/lightwood) | [Documentation](https://docs.mindsdb.com/lightwood/info/) | ![Lines of code](https://img.shields.io/tokei/lines/github/mindsdb/lightwood?style=flat-square) | ? | GPL-3.0 |
| ENAS| [Repository](https://github.com/melodyguan/enas) | - | - | [Paper](https://arxiv.org/abs/1802.03268) | Apache-2.0 |
| Talos| [Repository](https://github.com/autonomio/talos) | [Documentation](https://autonomio.github.io/talos/#/) | ![Lines of code](https://img.shields.io/tokei/lines/github/autonomio/talos?style=flat-square) | - | MIT |
| Hyperas (Archived) | [Repository](https://github.com/maxpumperla/hyperas) | [Documentation](http://maxpumperla.com/hyperas/) | ![Lines of code](https://img.shields.io/tokei/lines/github/maxpumperla/hyperas?style=flat-square) | - | MIT |
| | | | | | |



## Other projects
For future categorization

| Name | Repository | Documentation | Stats | Papers | License |
|:---------|:---------|:---------|:---------:|:---------|:---------|
| PocketFlow | [Repository](https://github.com/Tencent/PocketFlow) | [Documentation](https://pocketflow.github.io/) | ![Lines of code](https://img.shields.io/tokei/lines/github/Tencent/PocketFlow?style=flat-square) | [Paper](https://openreview.net/pdf?id=H1fWoYhdim) | BSD-3-Clause |
|  |  |  |  |  |  |



## Commercial projects

| Name | Website | Documentation | Company |
|:---------|:---------:|:---------|:---------|
| Cloud AutoML | [Link](https://cloud.google.com/automl) | [Documentation](https://cloud.google.com/automl/docs) | Google |
| ADS (AutoML)  | - | [Documentation](https://docs.oracle.com/en-us/iaas/tools/ads-sdk/latest/user_guide/automl/overview.html) | Oracle |
| SageMaker Autopilot | [Link](https://aws.amazon.com/sagemaker/autopilot/) | [Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) | Amazon |
| Azure Automated ML | [Link](https://azure.microsoft.com/en-us/services/machine-learning/automatedml/) | [Documentation](https://docs.microsoft.com/en-us/azure/machine-learning/concept-automated-ml) | Microsoft |
| Watson AutoAI | [Link](https://www.ibm.com/cloud/watson-studio/autoai) | [Documentation](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html) | IBM |
| Driverless AI | [Link](https://www.h2o.ai/products/h2o-driverless-ai/) | [Documentation](https://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/index.html) | H2O.ai |
|  |  |  |  |

