# PseudoChat-Instruction-Dataset

## Introduce

본 프로젝트의 목적은 한국어로 이루어지고 구축에 누구나 참여할 수 있으며 공개적으로 사용할 수 있는 Instruction 데이터셋을 구축하는 것입니다.

## Tryout site

[🔥 PseudoChat Assistant](http://59.15.178.175:5003/)


## 데이터셋 제작 의도

- **Human Instruction과 Feedback이 반영된 데이터셋**은 사전 학습된 언어 모델을 학습시켜 인간과 유사한 Text Instruction을 생성하는 데 유용한 리소스입니다.
- 언어 모델을 단순히 거대하게만 만드는 것은 여러 태스크의 성능을 높이기는 하나, 이를 사용하는 유저들의 질문 의도를 파악하는데 효과적이지 않습니다.
- 또한, **사실성이 떨어지고 유해하며, 유저에게 도움이 되지 않는 답변**을 생성하는 경향이 있습니다.
- 이에 **OpenAI**의 **InstructGPT**는 인간의 피드백을 이용하여 유저의 질문 의도를 따르는 **Aligning Language Model 방법론**을 사용하여 이러한 문제를 해결하고 보다 유용한 답변을 출력하도록 합니다.
- 하지만 InstructGPT 방법론을 사용한 ChatGPT의 경우 학습에 사용한 데이터 570GB 중 한국어 데이터 비중이 **1.3%에 불과**하며, **공개되어 있지 않습니다.**
- 따라서 가짜연구소에서는 **한국어로 이루어지고 구축에 누구나 참여할 수 있으며 공개적으로 사용할 수 있는 Instruction 데이터셋과 Human Feedback 데이터셋을 구축하고자 합니다.**

## 데이터셋 제작 목표

- 공개된 LLMs 모델을 사용하여 InstructGPT에 사용된 데이터셋과 유사한 **Human Feedback이 적용된 데이터셋을 구축**하는 것입니다.
- 모델의 방법론을 학습하고 이를 구현하는 것도 좋지만, 본 데모에서는 **Prompt-Instruction 데이터셋 구축이 목표**입니다.
- 추후 모델을 통한 응답에 대해 평가하거나 수정하는 작업을 추가할 계획입니다.

## About PsuedoLab
- 가짜연구소는 머신러닝/데이터사이언스를 중심으로 모인 비영리 커뮤니티입니다.
- 성장의 앙상블이 만들어내는 울림을 통해 개인과 커뮤니티의 성장의 사이클을 함께 만들어나가요!
- [PseudoLab 찾아가기](https://pseudo-lab.com/)
## Authors
프로젝트에 참여한 가짜연구소 6기 멤버 명단입니다.
- [정영상](https://www.linkedin.com/in/video-jeong/)
- [염성현](https://www.linkedin.com/in/neulvo/)
- [백상원](https://www.linkedin.com/in/sangwon-baek-74a3241b7/)
