# Redesigning and assessing the intro course sequence

**Challenge.** By the time students start their CS2 course (typically, COMP 271), we notice that they retain few of the skills introduced in COMP 141 (CLI and other system tools), COMP 163 (discrete mathematics), and COMP 170 (introductory programming/CS1).

**Hypothesis.** Concepts in these courses are presented in isolation of each other. For example, COMP 163 may discuss a vector product $\mathbf x\cdot\mathbf y = \sum x_i\,y_i$ but outside the context of programming, the presentation misses a perfect opportunity to operationalize it as a loop over two arrays. Likewise, students in COMP 141 may use command line interface for a couple of assignments, but without a persistent production goal, the skill does not carry forward to, say, using CLI to build code in COMP 170.

**Proposal.** In a course that spans two terms, mix and match topics from COMP 141, 163, and 170. The order in which these topics will be presented shall establish the command line interface as the principal modality for interacting with a computer system. It should also establish core mathematical concepts that are vital for programming.

**Implementation.** Create two experimental courses, COMP 158 and COMP 159. (These are approximately the average value of 141, 163, and 170). Offer the courses back-to-back in a Fall/Spring arrangement. Have the courses co-taught by two instructors.

**Note on downstream language transition.** Students who complete the integrated sequence will eventually move from Python (the language of COMP 158/159 and COMP 271) to Java (COMP 272, non-linear data structures). The integrated sequence should build enough language-agnostic programming intuition — separating concepts like recursion, iteration, and data modeling from syntax — so that the Python-to-Java transition in COMP 272 is not a barrier.

---

## Assessment Framework: COMP 158/159 Integrated Intro Sequence

### Theory of Change

This proposal is based on the assumption (and hope) that the **integrated presentation of CLI together with discrete math and introductory programming** will lead to the following outcomes:

* stronger conceptual cross-linking;
* better retention of foundational skills;
* improved performance and persistence in COMP 271.

The following research questions are designed to test whether the integrated approach produces the desired outcomes.

---

### Research Questions

| # | Question | Type |
|---|----------|------|
| RQ1 | Do 158/159 students enter COMP 271 with stronger foundational skills than legacy-sequence students? | Comparative |
| RQ2 | Which topic integrations (CLI↔programming, math↔programming) show the strongest transfer? | Mechanistic |
| RQ3 | Does the integrated sequence improve retention in the CS program through CS2? | Longitudinal |
| RQ4 | Is the co-taught model pedagogically coherent from the student perspective? | Process |

Comparative questions ask whether one group differs from another on some outcome — the classic treatment vs. control framing. Mechanistic questions ask why or how an effect occurs — not just that integration helps, but which specific integrations drive the benefit. Longitudinal questions track the same students over time, capturing change and persistence rather than a single snapshot. Process questions examine how an intervention is being delivered — whether the co-teaching model is coherent and experienced as intended — independent of outcomes.

---

### Study Design

#### Control and Treatment Groups

| Group | Sequence | Cohort Size (target) |
|-------|----------|----------------------|
| **Treatment** | COMP 158 → 159 → 271 | ~25–30 per cohort |
| **Control** | COMP 141 + 163 + 170 → 271 | Matched historical + concurrent enrollees |

Match control students on: declared major, incoming math placement score, and term of first CS course. Use **two cohorts** (Year 1 and Year 2) so Year 2 can replicate and refine findings from Year 1.

#### Timeline

```
Year 1 Fall   → Cohort 1 begins COMP 158
Year 1 Spring → Cohort 1 takes COMP 159
Year 1 Spring → Cohort 2 begins COMP 158 (overlapping pipeline)
Year 2 Fall   → Cohort 1 enters COMP 271 ← primary outcome window
Year 2 Fall   → Cohort 2 takes COMP 159
Year 2 Spring → Cohort 2 enters COMP 271 ← replication window
Year 2 Spring → Cross-cohort analysis and reporting
```

---

### Assessment Instruments

#### Standardized Pre/Post Concept Tests

Administer at four time points: **entry to 158, exit from 159, entry to 271, exit from 271**.

Design three short modules (~10 items each):

**Module A — CLI Fluency**
Items probe: navigation, file I/O, piping, scripting. Use scenario-based tasks ("given this directory tree, write the command that…"). Score as correct/partial/incorrect.

**Module B — Mathematical Operationalization**
Items bridge discrete math to code. Example: given the formula $\mathbf{x} \cdot \mathbf{y} = \sum x_i y_i$, write a Python loop that computes it. Or: given a recurrence relation, trace its evaluation. This is the most novel module and directly tests the core hypothesis.

**Module C — Programming Concepts**
Standard CS1 exit inventory: variables, loops, conditionals, functions, basic data structures. Instruments like the [FCS1](https://dl.acm.org/doi/10.1145/1352135.1352296) can be adapted here rather than built from scratch.

**Scoring and analysis:** Compute gain scores (post − pre) and compare treatment vs. control using a two-sample t-test or Mann-Whitney U per module. With two cohorts we can check whether Year 2 replicates Year 1 effect sizes.

#### COMP 271 Performance Metrics

This is the primary downstream outcome. Collect for both treatment and matched control students:

- Final course grade (A/B/C/D/F/W)
- Grade on the first major programming assignment (a leading indicator of preparation)
- Grade on any assessment that explicitly requires CLI usage
- Withdrawal/failure rate

Additionally, ask the COMP 271 instructor(s) — ideally blinded to which students came from which sequence — to rate a random sample of submitted work on a rubric that includes: *code organization*, *use of tools*, and *mathematical reasoning in comments/documentation*.

#### Oral Exam / Interview Data

Oral assessment serves two purposes here: it is a richer signal of deep understanding than written tests, and it offers a natural opportunity to pilot AI-assisted oral examination at scale.

> **IRB flag:** Recording students during oral exams and retaining identifiable audio/video data requires IRB approval before data collection begins. Consent forms must be obtained from all participants prior to any session.

**Structured exit interview from COMP 159** (~15 minutes per student, recorded with consent):

Prompt categories:
1. *Integration prompts* — "Walk me through how you'd use the terminal to compile and run a program that computes a dot product." Tests whether CLI, math, and code are linked in the student's mental model.
2. *Transfer prompts* — "You're about to start CS2. What do you feel most and least prepared for?"
3. *Reflection prompts* — "When you see a mathematical formula, what's your first instinct now compared to when you started?"

**Coding with narration** — give one small problem (e.g., implement a dot product from scratch using only CLI tools and a text editor), ask the student to think aloud. Score on a rubric: tool fluency, mathematical setup, code correctness, self-correction behavior.

**AI-agent deployment opportunity:** This is also a natural place to pilot an AI oral examiner. The agent can deliver the integration prompts consistently across all students, transcribe responses, and produce a preliminary rubric score for human review — reducing interviewer fatigue over 50+ students while generating a rich qualitative corpus.


#### CLI / Artifact Logs

Because CLI fluency is a *behavioral* outcome, self-report and concept tests are insufficient. Collect:

- **Shell history exports** (opt-in, anonymized) from student dev environments at the end of 158, 159, and the first week of 271. Compute: command vocabulary size, frequency of piping, presence of scripting constructs.
- **Assignment artifacts** — for any assignment in 158/159 where students submit via CLI (e.g., `git push`, `make`, a shell script), retain the submission logs. Code a random 20% sample for CLI sophistication on a 3-point scale.
- **COMP 271 artifact check** — does the student's first 271 submission use a `Makefile`, a `.gitignore`, a build script? Binary indicator, but meaningful.

**Data management:** Shell history exports and oral exam recordings should be stored on university-managed infrastructure, anonymized before analysis, and deleted at the end of Year 2 per IRB data retention requirements. Consent forms should specify these terms explicitly.

#### Retention Metric

Even without retention/continuation rates as a formal instrument, we can track: of students who completed 159, what fraction enrolled in 271 within two semesters? Compare to the analogous rate for students who completed all three legacy courses. This is a low-burden metric that speaks directly to institutional adoption arguments.

---

### Construct Validity Threats (and mitigations)

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Selection bias** | Students who choose the new sequence may be more motivated | Match on math placement; collect motivation survey at entry |
| **Instructor effect** | Co-taught by specific faculty; results may not generalize | Document pedagogical decisions; Year 2 can vary one instructor |
| **Novelty effect** | Students perform better simply because the course is new | Year 2 replication with a less "fresh" offering tests this |
| **Teaching to the test** | 158/159 instructors know the exit instruments | Use Module C (FCS1-derived) which is not course-specific |
| **Attrition** | Students who drop 158 are not in the 271 comparison | Report intent-to-treat and per-protocol analyses separately |

---

### Deliverables by End of Year 2

1. **Quantitative report** — gain scores per module, COMP 271 grade distributions, retention rates, with effect sizes and confidence intervals.
2. **Qualitative report** — thematic analysis of oral exam transcripts, organized around the four RQs.
3. **Artifact portfolio** — anonymized sample of CLI submissions annotated with rubric scores.
4. **Instructor reflection document** — structured post-mortems from both co-instructors after each term (what integrations worked, what sequencing changes are needed).
5. **Recommendation memo** — 2–3 pages for the curriculum committee, answering: *should COMP 158/159 replace the legacy sequence, run in parallel, or be revised further?*

---

### What "Success" Looks Like

The pilot should be declared a candidate for adoption if it meets **at least three of the following four criteria**:

1. Treatment students show statistically significant higher gain scores on Module B (math operationalization) at COMP 271 entry.
2. Treatment students' COMP 271 first-assignment grade is ≥ 0.3 letter grades higher on average than matched controls.
3. CLI artifact sophistication in COMP 271 week 1 is rated higher for treatment students in a blinded rubric review.
4. Retention from end of intro sequence to COMP 271 enrollment is at least 5 percentage points higher for the treatment group.

Partial success on two criteria warrants a revised second offering before a broader rollout decision.