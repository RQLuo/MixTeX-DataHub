# LaTeXDataHub
LaTeXDataHub is an open-source platform dedicated to the sharing and contribution of real-world LaTeX image datasets and their annotations, allows users to upload, download, and contribute to a growing collection of high-quality LaTeX datasets. To ensure that the data is not dependent on third-party platforms and can be shared everywhere, I recommend using magnet links to deliver the dataset.

LaTeXDataHub 是一个开源平台，致力于共享和贡献真实 LaTeX 图像数据及其注释，允许上传、下载并为高质量 LaTeX 数据集做出贡献。为确保数据不依赖于第三方平台，以及在任何地方都能够共享，我建议使用磁力链接传递数据集。

## 建议数据标注方法

对于较为标准的现代打印latex文档的数据图片，您可以直接采用MixTeX，它已有较高的准确率，您只需要纠正少量的错误。

对于手写或者老教材latex的数据集，目前MixTeX暂时还没有训练过，表现的不太好。

您可以采用chatgpt或者claude辅助标注。您可以参考以下提示词：_latex ocr 直接输出，所有公式用align*，文字放在外面，文内公式用\( .. \)，不要废话，不要继承直接输出ocr结果：_

## 常见数据集收集项目1：现代打印文档MixTeX表现较差数据集 (对应模型参数<100M)

## 特殊数据集收集项目1：手写latex草稿数据集 (对应模型参数 150-200M)

## 特殊数据集收集项目2：黑板板书latex数据集 (对应模型参数 150-200M)

## 复杂指令数据集1:识别latex并翻译成[语言] (对应模型参数 300-600M)

## 复杂指令数据集2:识别latex并用自己的话重述 (对应模型参数 300-600M)

## 超复杂指令数据集1:识别板书并写成Lecture Note (对应模型参数 > 2B)

## 超复杂指令数据集1: 识别latex并用前置知识解释 (对应模型参数 > 2B)

## claude都做不到的数据集1：证明和推理 (还不知道用啥模型能实现，该数据集必须有来源，最好是经典教材上的证明和推导)



