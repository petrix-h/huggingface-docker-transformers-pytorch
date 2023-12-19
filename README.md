# huggingface-docker-transformers-tensorflow
Minimal docker config testing for running HuggingFace transformers locally (CPU to start with)

TODO make better playground... 

## In the meantime playground with: 

```docker-compose build huggingface-docker```

```docker-compose run huggingface-docker bash```

To edit the test: 

```nano test.py```

 -- Copy paste the contents from test.py --  Ctrl + x y

To run the test: 

```python3 test.py```

 -- wait for the models to be loaded, then wait a bit more to run the thing... running on CPU takes about 350-400s on a M2 Pro... 
