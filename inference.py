from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Open Rotor Copilot model")    
    parser.add_argument("--output_dir", type=str, default="checkpoints", help="Directory to save model")
    parser.add_argument("--input", type=str, default="", help="Input string")
    args = parser.parse_args()

        
    tokenizer = AutoTokenizer.from_pretrained(args.output_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(args.output_dir)

    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    result = pipe(args.input, max_new_tokens=32)[0]['generated_text']
    print(result)