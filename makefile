install:
	pip install -r requirements.txt

run:
	python ./main.py

upgrade-pip:
	python -m pip install --upgrade pip

install-pytorch-gpu:
	pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118