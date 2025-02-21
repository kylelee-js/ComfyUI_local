
```
// python 버전 : 3.12.1
pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

pip3 install -r requirements.txt
```

모델 다운로드 후 clip, vae, checkpoint 폴더에 safetensor 모델을 넣기.
> ./models/checkpoint/sd3.5_medium.safetensors
> ./models/clip/clip_g.saftensors
> ./models/clip/clip_l.saftensors
> ./models/clip/t5xxl_fp8_e4mfn.saftensors
> ./models/vae/diffusion_pytorch_model.safetensors
> 

`python main.py` 실행 후 http://localhost:8188/ 접속한다.

사용하는 모델의 workfolw.json 파일을 드래그 드롭으로 워크플로우 설정 후 모델 설정하기.


#### 참고
https://wikidocs.net/275959
https://huggingface.co/stabilityai/stable-diffusion-3.5-medium/tree/main
https://stable-diffusion-art.com/stable-diffusion-3-5-medium-comfyui/
