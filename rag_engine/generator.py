from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class Generator:

    def __init__(self):

        model_name = "mistralai/Mistral-7B-Instruct-v0.3"

        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        print("Loading model...")

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.float16
        )

    def generate_answer(self, prompt):

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)