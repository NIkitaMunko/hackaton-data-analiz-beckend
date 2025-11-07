import string
from datasets import load_dataset

DATA_PATH = "./dataset/receipts.csv"

dataset = load_dataset("csv", data_files=DATA_PATH, split="train")

# TODO: (конект к ендпоинтс)(Никита)
def receiver(text : string) -> str:
    print(text)
    return text