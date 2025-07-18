import argparse
import torch
from preprocess import load_and_prepare
from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments

def main():
    parser = argparse.ArgumentParser(description="Train Open Rotor Copilot model")
    parser.add_argument("--csv", type=str, default="data/train.csv", help="Path to training CSV file")
    parser.add_argument("--model_name", type=str, default="google/flan-t5-small", help="Base model name")
    parser.add_argument("--output_dir", type=str, default="checkpoints", help="Directory to save model")
    args = parser.parse_args()

    # Load and preprocess dataset
    dataset = load_and_prepare(args.csv)

    # Load model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(args.model_name)
    model = T5ForConditionalGeneration.from_pretrained(args.model_name)

    # Tokenize
    def tokenize(example):
        input_text = example["input"]
        target_text = example["issues"]  # renamed from 'issues' in preprocessing

        model_inputs = tokenizer(
            input_text, truncation=True, padding="max_length", max_length=512
        )

        labels = tokenizer(
            target_text, truncation=True, padding="max_length", max_length=20
        )

        labels["input_ids"] = [
            (l if l != tokenizer.pad_token_id else -100) for l in labels["input_ids"]
        ]
      

        model_inputs["labels"] = labels["input_ids"]
        return model_inputs
    
    tokenized = dataset.map(tokenize, batched=False)

    
    training_args = TrainingArguments(
       output_dir=args.output_dir,
        per_device_train_batch_size=8,
        num_train_epochs=5,  # consider increasing a bit
        logging_steps=100,  # log more frequently
        save_strategy="epoch",
        save_total_limit=2,
        remove_unused_columns=True,
        fp16=False,  # enable if supported by GPU
        logging_dir="./logs",
        report_to="none"  # or "tensorboard" if you want tracking
        )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model(args.output_dir)

if __name__ == "__main__":
    main()
