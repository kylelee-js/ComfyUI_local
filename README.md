
```
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

pip install -r requirements.txt
```

모델 다운로드 후 clip, vae, checkpoint 폴더에 safetensor 모델을 넣기.

`python main.py` 실행 후 http://localhost:8188/ 접속한다.

사용하는 모델의 workfolw.json 파일을 드ㅊ래그 드롭으로 워크플로우 설정 후 모델 설정하기.
