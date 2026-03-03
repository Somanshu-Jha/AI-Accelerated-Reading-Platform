from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
torch.backends.cuda.matmul.allow_tf32 = True

class Generator:
    def __init__(self):

        self.model_name = "mistralai/Mistral-7B-Instruct-v0.3"

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

        print("Loading model in 4-bit (GPU optimized)...")
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            load_in_4bit=True
        )

    def generate(self, prompt: str, max_tokens: int = 512):
        formatted_prompt = f"""
        <s>[INST]
        You are a world-class AI research assistant.
        You must produce structured, analytical, deep responses.

        Task:
        {prompt}

        Respond in:
    - Clear headings
    - Bullet points
    - Professional tone
    [/INST]
"""



        inputs = self.tokenizer(
            formatted_prompt,
            return_tensors="pt"
        ).to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_tokens,
                temperature=0.5,
                top_p=0.9,
                do_sample=True
            )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response