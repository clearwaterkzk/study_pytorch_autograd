FROM pytorch/pytorch:2.5.1-cuda12.4-cudnn9-devel
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ Asia/Tokyo

RUN apt update -y \
    && apt upgrade -yq \
    && apt install -yq --no-install-recommends \
    graphviz \
    wget

# requirements.txtをコンテナ内にコピー
COPY requirements.txt .

RUN pip install -r requirements.txt

