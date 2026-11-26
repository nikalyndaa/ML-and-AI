
import os
import kagglehub

from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader


# 1. Завантаження датасету
path = kagglehub.dataset_download(
    "paultimothymooney/chest-xray-pneumonia"
)

# 2. Визначення шляху до папок
if os.path.isdir(os.path.join(path, "chest_xray")):
    DATA_DIR = os.path.join(path, "chest_xray")
else:
    DATA_DIR = path

# 3. Перетворення зображень
transform = transforms.Compose([
    transforms.Resize((224, 224)),

    transforms.Grayscale(num_output_channels=3),

    transforms.ToTensor(),

    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# 4. Завантаження навчальної вибірки
train_dataset = ImageFolder(
    os.path.join(DATA_DIR, "train"),
    transform=transform
)

# 5. Завантаження тестової вибірки
test_dataset = ImageFolder(
    os.path.join(DATA_DIR, "test"),
    transform=transform
)

# 6. Завантаження валідаційної вибірки
val_dataset = ImageFolder(
    os.path.join(DATA_DIR, "val"),
    transform=transform
)

# 7. Формування DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=32,
    shuffle=False
)

val_loader = DataLoader(
    val_dataset,
    batch_size=32,
    shuffle=False
)

# 8. Назви класів
class_names = train_dataset.classes

# 9. Інформація про датасет
print("Класи:", class_names)
print("Відповідність класів:", train_dataset.class_to_idx)

print("Train:", len(train_dataset))
print("Test:", len(test_dataset))
print("Validation:", len(val_dataset))
