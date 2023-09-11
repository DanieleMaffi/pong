FROM    ubuntu
#RUN     echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN     apt-get update
COPY . .
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
RUN     apt-get install -y x11vnc xvfb python3 pip firefox
RUN 	pip install -r requirements.txt
RUN     mkdir ~/.vnc
RUN     x11vnc -storepasswd 1234 ~/.vnc/passwd
RUN     bash -c 'echo "firefox" >> /.bashrc'
CMD firefox
