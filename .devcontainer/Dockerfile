FROM pytorch/pytorch:latest
# create vscode user
RUN groupadd --gid 1000 vscode \
	&& useradd --uid 1000 --gid 1000 -m vscode \
	&& apt -qq update \
	&& apt -qq upgrade -y \
	&& apt -qq install -y sudo git \
	&& echo vscode ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/vscode \
	&& chmod 0440 /etc/sudoers.d/vscode

# install python dependencies
RUN pip install -U pip --no-cache-dir
WORKDIR /workspaces/midterm
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install black flake8 isort --no-cache-dir
USER vscode
