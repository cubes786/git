from transformers import BertTokenizer, BertModel
import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torch.onnx as onnx

# Define the custom dataset class
class CustomDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]

        encoding = self.tokenizer(
            text,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'label': torch.tensor(label, dtype=torch.long)
        }

# Define the custom model class
class CustomBERT(nn.Module):
    def __init__(self, model_name='bert-base-uncased', num_classes=2):
        super(CustomBERT, self).__init__()
        self.bert = BertModel.from_pretrained(model_name)
        self.dropout = nn.Dropout(p=0.3)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        pooled_output = outputs.pooler_output
        pooled_output = self.dropout(pooled_output)
        outputs = self.classifier(pooled_output)
        return outputs

# Load pre-trained model and tokenizer
model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = CustomBERT(model_name=model_name, num_classes=2)

# Prepare the dataset
data = {
    "text": [
        "I love this product!",
        "This product is terrible.",
        "The service was amazing.",
        "I would never recommend this."
    ],
    "label": [1, 0, 1, 0]
}
df = pd.DataFrame(data)

max_len = 128
batch_size = 16

dataset = CustomDataset(
    texts=df['text'].tolist(),
    labels=df['label'].tolist(),
    tokenizer=tokenizer,
    max_len=max_len
)

dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Train the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
loss_fn = nn.CrossEntropyLoss()

num_epochs = 3
model.train()

for epoch in range(num_epochs):
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['label'].to(device)

        optimizer.zero_grad()

        outputs = model(input_ids, attention_mask)
        loss = loss_fn(outputs, labels)

        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Convert the model to ONNX
input_ids = torch.randint(0, 30522, (1, 128))
attention_mask = torch.ones(1, 128)

model.eval()
with torch.no_grad():
    outputs = model(input_ids, attention_mask)

onnx.export(
    model,
    args=(input_ids, attention_mask),
    f="custom_bert.onnx",
    opset_version=12,
    input_names=['input_ids', 'attention_mask'],
    output_names=['outputs'],
    dynamic_axes={
        'input_ids': {0: 'batch_size', 1: 'sequence_length'},
        'attention_mask': {0: 'batch_size', 1: 'sequence_length'},
        'outputs': {0: 'batch_size', 1: 'num_classes'}
    }
)