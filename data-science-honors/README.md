# Healthcare Data Explorer — LCP Data Science Honors

Interactive GitHub Pages companion to Aaryan Samanta's 2025 Legend College Preparatory capstone, **Exploring Disease Symptom and Patient Profile Analysis**.

## Run

Open `index.html` locally or host the repository on GitHub Pages. Click **Load synthetic example** for an immediate working demonstration, or **Upload CSV** and select `Disease_Symptom_and_Patient_Profile_Dataset.csv`, then click **Run EDA**. Uploaded data is processed entirely in the browser; it is not transmitted to a server.

## Source alignment

- Duplicate removal (`df.drop_duplicates()`)
- Numeric conversion of Age, invalid values filled with zero
- Categorical encoding of text Blood Pressure and Cholesterol Level
- Age histogram (20 bins), blood pressure histogram (15 bins)
- Age and blood pressure boxplots grouped by Gender
- Top 20 Disease counts
- Pearson correlation heatmap for numeric columns

Browser visualizations are reimplementations, not Seaborn/Matplotlib output. For CSV category encoding, alphabetical ordering is used to approximate Pandas categorical codes. Unlike Pandas, this version deliberately treats blank CSV values as missing and may differ in unusual mixed-type columns. The original CSV is not included; synthetic data does **not** reproduce the report's numerical findings. The reported 0.31 blood pressure/cholesterol correlation is from the original report and cannot be validated without the original dataset.

## Files

- `index.html`: self-contained interactive demo
- `source/symptoms.py`: preserved original 2025 student Python code
- `references/report.pdf`: original submitted report
- `references/presentation.pdf`: original submitted capstone slides

## Authorship and scope

Original source credits Aaryan Samanta, Legend College Preparatory, and explicitly notes adaptation from classroom exercises. The interactive JavaScript website was created with AI assistance as a separate presentation companion. Do not present the website as independently authored by the student. This is exploratory data analysis, not a disease classifier, CNN, or medical diagnostic tool. Use only non-identifiable data.

## GitHub Pages

Upload all files to a repository, go to Settings → Pages → Deploy from branch → main → /(root). The published URL is `https://USERNAME.github.io/REPOSITORY/`.
