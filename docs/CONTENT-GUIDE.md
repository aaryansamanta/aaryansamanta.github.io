# Content guide

This page is a record other people will check, so the rules are stricter than the design.

## Rules

1. **Results only.** Something goes in as a result only when it is finished. Plans, goals and "expected" outcomes stay out.
2. **Every number is traceable.** Either a public source is linked (see the Sources section) or an official record exists that can be shown on request.
3. **No unsourced rankings or percentiles.** "Top X%" appears only when a published field size backs it up.
4. **Unfinished work is labeled as unfinished.** Use the hollow dot, and say what stage it is at ("submitted", "in progress", "not yet accepted").
5. **One number, one value.** If two files disagree (a resume, a spreadsheet, a README), settle it once and update everything that repeats it, including the other repositories.
6. **Privacy.** No phone number, no home address, no reference contact details. The only email on the site is the contact address. `tools/check.py` enforces this.
7. **No placeholders on the live page.** Nothing in square brackets, no "TBD".

## Status labels

The dot next to each entry shows completion at a glance. Each row must carry exactly one.

| Class | Dot | Use for |
|---|---|---|
| `status status--done` | filled blue | published, founded, medal earned |
| `status status--accepted` | filled teal | accepted, not yet published |
| `status status--open` | hollow ring | ongoing, in progress, under review, submitted |

Promote `status--open` to `status--done` (or `--accepted`) only when the milestone has actually happened, and add the public link in the same commit.

## Entry templates

A ledger row (research, building, outside the classroom):

```html
<article class="row">
  <div class="row-aside"><span class="status status--open">Ongoing</span><span class="row-date">2026 to present</span></div>
  <div>
    <h4 class="row-title">Title</h4>
    <p class="row-venue">Where, role, mentor</p>
    <p class="row-text">What it is and what was found. Wrap key numbers in <span class="figure-num">23</span>.</p>
    <p class="row-links"><a href="https://example.org">Public source</a></p>
  </div>
</article>
```

Use `<h4>` inside Research (under the group headings) and `<h3>` in the other sections.

A competition line:

```html
<li>
  <span class="year">2026</span>
  <span class="contest">Contest name<small>National</small></span>
  <span class="result"><span class="rank">1st</span> One sentence with the score and the field size.</span>
</li>
```

A paper also gets a `<details class="cite">` block with its BibTeX; the script adds the copy button.

## Items deliberately not on the site

Keep these off until they are real and documented: prospective honors and application targets, download or user counts, patents that are not granted, study sizes for studies not yet run, unnamed employers or placeholder organization names, and any percentile without a source.

## Repository settings (once)

- Description: `Aaryan Samanta: machine learning for biology and medicine. Research, competitions, and AI Ethos.`
- Website: `https://aaryansamanta.github.io/`
- Topics: `personal-website`, `portfolio`, `github-pages`, `research`, `machine-learning`
- Pin this repository and `ai-research-publications` on your GitHub profile.
- Settings, Pages: enable "Enforce HTTPS".
