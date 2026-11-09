# Chest X-Ray CNN Lab — LCP AI Internship

An interactive, GitHub Pages-compatible companion to **Exploring Pneumonia Detection with Chest X-Ray Images** by Aaryan Samanta, Legend College Preparatory AI Internship.

## Deploy to GitHub Pages

1. Create a public GitHub repository (suggested: `lcp-ai-internship-pneumonia-cnn`).
2. Upload the **contents of this folder** to the repository root, preserving the `source/` and `reports/` directories.
3. Under **Settings → Pages**, select **Deploy from a branch**, `main`, `/ (root)`.
4. Open the published GitHub Pages address.

No build tools, external libraries, API keys, or server required. Open `index.html` locally to test.

## Working interactions

- **Image pipeline:** upload a non-sensitive image or load a generated geometric pattern; click **Run preprocessing** to resize to 150×150 and calculate RGB normalization statistics. Image processing occurs entirely in-browser.
- **CNN architecture:** inspect each layer from the supplied Keras Sequential model.
- **Model evaluation:** switch between 1-, 3-, and 5-epoch historical experiments. Confusion matrices, class recall, and accuracy are calculated from the published report's counts.
- **Project notes:** original notebook, report, and slides are linked.

## Source fidelity and limitations

The supplied notebook contains `ImageDataGenerator(rescale=1./255, zoom_range=0.2)`, 150×150 RGB inputs, batch size 32, three convolutional stages (32/64/128 filters), max pooling, Flatten, Dense(128, relu), Dense(1, sigmoid), Adam/binary crossentropy, EarlyStopping monitoring validation loss, and evaluation using a 0.5 prediction threshold. This site visualizes the preprocessing and architecture; it **does not implement Keras model inference or training**.

The report supplies confusion matrices:

| Epochs | Actual NORMAL → predicted NORMAL | NORMAL → PNEUMONIA | PNEUMONIA → NORMAL | PNEUMONIA → PNEUMONIA |
|---|---:|---:|---:|---:|
| 1 | 141 | 93 | 20 | 369 |
| 3 | 141 | 93 | 20 | 369 |
| 5 | 158 | 76 | 2 | 387 |

All reported counts total 623 test samples. The original chest X-ray image dataset and trained model weights were **not supplied**, so the demo cannot make valid predictions on uploaded X-rays or recreate the original learning curves. The report discusses dropout and stronger augmentation as possible improvements, but these are **not active** in the supplied notebook's model.

## Reproducing original research

Open `source/Chest_X_Ray.ipynb` in Google Colab, obtain the original appropriately licensed chest X-ray dataset, and update `base_dir` to the location containing `train/`, `val/`, and `test/` directories. Install a compatible TensorFlow/Keras environment. The original notebook expects the data at a specific Google Drive path and is not a one-click hosted inference application.

## Attribution and responsible use

Original research materials and notebook: Aaryan Samanta / Legend College Preparatory AI Internship. Browser-based interactive companion developed separately with AI assistance. Educational demonstration only; not a diagnostic medical device. Do not upload identifiable patient images.
