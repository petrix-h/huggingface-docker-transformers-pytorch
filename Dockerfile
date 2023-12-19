FROM miigotu/python3.11

RUN apt update
RUN apt install -y git build-essential cmake wget nano

#RUN pip install transformers
#For CPU only.. 
RUN pip install 'transformers[torch]'
#Required by Phi-2
RUN pip install einops

#TODO add ssh and expose a port... 
#In the meantime playground with: 
# docker-compose build huggingface-docker
# docker-compose run huggingface-docker bash
# nano test.py
# -- Copy paste the contents from test.py --  Ctrl + x y
# python3 test.py
# -- wait for the models to be loaded, then wait a bit more to run the thing... running on CPU takes about 350-400s on a M2 Pro... 
