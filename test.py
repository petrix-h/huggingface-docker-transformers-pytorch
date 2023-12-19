import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

start_time=time.time() 
torch.set_default_device("cpu")

#model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype=torch.float32, device_map="cpu", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

tokeniser_start_time=time.time() 

inputs = tokenizer('''
What is  (2 + 2) * (4 / 4) ? 
''', return_tensors="pt", return_attention_mask=False)

generate_start_time=time.time()
outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
end_time = time.time()

print(text)

total_time = end_time - start_time; 
gen_time = end_time - generate_start_time; 
token_time = generate_start_time - tokeniser_start_time; 

print(f"Total time: {total_time} seconds of which generation time: {gen_time} s, tokeniser time: {token_time} s ")
