# Pelvic Floor Motion Lab — Stanford-mentored research (2026)

Static GitHub Pages research companion with a compact Stanford-cardinal-inspired interface.

## Run
Open `index.html`, or upload this folder’s contents to the repository root / `docs` and enable GitHub Pages. No backend, dependencies, or dataset download.

## Source fidelity and scope
The provided ZIP describes perineal ultrasound imaging under voluntary contraction (The Knack), cough, and Valsalva. The supplied summary reports 23 subjects, mean age 31.1 ± 13.6 years, and a 5.5 MHz probe. The browser lab generates **synthetic illustrative displacement curves** and computes numerical first and second derivatives. It does **not** reproduce measurements from the original project, infer anatomy from images, train an ML model, or make medical claims. No computational code or measurement tables were supplied.

The research presentation PDF is included for context. Original imaging videos and photos are excluded because public sharing permission was not established. Verify rights for the included presentation before publishing. This is an AI-assisted demonstration companion, not a student-authored original analysis or an official Stanford site.

## Repository-inspired visual theme
The site incorporates the animated `assets/banner.svg` supplied in the project repository, with its indigo/violet gradient, moving cyan scan beam, and animated waveform. The header stays compact so the browser lab appears near the top. Clinical GIFs are **not** bundled because the source README says permission is required to redistribute mentor-owned clinical imagery.

## See it in action — original animations

The top of the page now includes three original annotated ultrasound GIFs (The Knack, Valsalva, cough), and a collapsible section with three pressure visualization GIFs, copied from the supplied `stanford-urology-2026` repository. These are separate from the illustrative JavaScript-generated motion traces.

**Permission:** The source README states the imaging belongs to Dr. Constantinou and no license is granted for redistribution. This package includes the GIFs for local review at the user’s request. **Obtain the mentor/rightsholder’s permission before publicly deploying this version.** If permission is not granted, remove `assets/gifs/` and the gallery from `index.html`, or replace with authorized media.

## Original research repository

The compact header, introduction and sources section link to the original project:
https://github.com/aaryansamanta/ai-research-publications/tree/main/stanford-urology-2026
