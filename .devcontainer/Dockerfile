FROM pytorch/pytorch:latest
# create vscode user
RUN groupadd --gid 1000 vscode \
	&& useradd --uid 1000 --gid 1000 -m vscode 

# install python dependencies
RUN pip install -U pip --no-cache-dir
WORKDIR /workspaces/midterm
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
USER vscode
