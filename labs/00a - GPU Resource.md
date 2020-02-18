## Why a GPU?

GPUs (Graphics Processing Units) are specialized computer hardware originally created to render images at high frame rates. They are good at texture rendering and shading which require more matrices and vector operation than a CPU can handle.
As we all know, Deep Learning also requires superfast matrix computations. So researchers [started training models in GPU's](http://www.machinelearning.org/archive/icml2009/papers/218.pdf).

| GPU                     |            CPU            |
| ----------------------- | :-----------------------: |
| Optimized FP Operations |  Complex Instruction Set  |
| Slow (1-2 Ghz)          |      Fast (3-4 Ghz)       |
| > 1000 Cores            |        < 100 Cores        |
| Fast Dedicated VRAM     | Large Capacity System RAM |

Deep Learning only cares about the number of Floating Point Operations per second (FLOPs) and GPUs are highly optimized for that. 


## Free Gpu Resources

* [Kaggle](https://kaggle.com)
* [Google colab](https://colab.research.google.com/)
* [Paperspace](https://paperspace.io/&R=NKIXO6I)
