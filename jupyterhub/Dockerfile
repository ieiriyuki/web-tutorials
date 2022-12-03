FROM jupyterhub/jupyterhub

RUN pip install -U pip \
    && pip install jupyter_server

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py

RUN useradd -m -s /bin/bash -N diego \
    && echo diego:diego | chpasswd

CMD jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
