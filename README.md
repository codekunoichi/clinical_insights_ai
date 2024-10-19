# Clinical Insights AI
Summarizes visit notes for patient historical visits.

## Example Visit Summary

```
Visit 1: October 1, 2024

Subjective:
    • The patient reports an increase in hip pain, especially when lying down.
    • Describes the pain as aching, mainly located around the hip bones and muscles.
    • The patient also reports occasional upper arm aches when in a lying position.
    • No radiating pain down the legs.
    • Microdiscectomy at L4/L5 was performed 6 months ago, and the patient denies any radiating pain to the lower extremities.

Objective:
    • Vitals: BP 130/85 mmHg, HR 72 bpm, Temp 98.6°F, BMI 28.
    • Physical exam:
    • Tenderness on palpation around both hip bones.
    • No visible swelling or erythema.
    • Range of motion in hips slightly reduced.
    • Neurological exam normal: no signs of numbness or weakness in lower extremities.
    • Recent imaging: Lumbar MRI shows post-surgical changes at L4/L5 but no new abnormalities.

Assessment:
    • ICD-10 Codes:
    • M25.551: Pain in right hip.
    • M25.552: Pain in left hip.
    • M54.5: Low back pain.
    • CPT Codes:
    • 99214: Established patient office visit, moderate complexity.
    • 72148: MRI of lumbar spine.

Plan:
    • Medications:
    • Ibuprofen 600 mg PO every 8 hours as needed for pain. RxNorm: 5640.
    • Cyclobenzaprine 10 mg PO at bedtime for muscle relaxation. RxNorm: 3112.
    • Continue physical therapy for mobility improvement.
    • Recommended stretching exercises for hips and back.
    • Follow up in 4 weeks for reassessment.

Visit 2: September 1, 2024

Subjective:
    • The patient reports persistent upper arm pain, mainly localized to the deltoid area.
    • Describes the pain as worse at night, interfering with sleep.
    • Denies any weakness or numbness in the arms.
    • The patient has a history of upper arm tendinitis diagnosed 6 weeks ago and is undergoing physical therapy.

Objective:
    • Vitals: BP 125/82 mmHg, HR 70 bpm, Temp 98.4°F.
    • Physical exam:
    • Tenderness on palpation over the deltoid muscle.
    • Range of motion of the shoulder is restricted (40% mobility).
    • No swelling, redness, or warmth in the affected area.
    • Strength testing: slightly reduced strength in the affected arm (4/5).
    • Recent ultrasound: Confirmed diagnosis of tendinitis without tear.

Assessment:
    • ICD-10 Codes:
    • M75.101: Tendinitis of right shoulder.
    • M75.102: Tendinitis of left shoulder.
    • CPT Codes:
    • 20552: Injection(s); single or multiple trigger point(s), 1 or 2 muscle(s).
    • 99213: Established patient office visit, low complexity.

Plan:
    • Medications:
    • Naproxen 500 mg PO twice daily for inflammation and pain. RxNorm: 857482.
    • Tizanidine 4 mg PO at bedtime for muscle spasm. RxNorm: 8786.
    • Continue with physical therapy for arm mobility.
    • Advise hot/cold compresses to reduce inflammation.
    • Follow up in 6 weeks or sooner if symptoms worsen.

Visit 3: August 1, 2024

Subjective:
    • The patient complains of lower back pain persisting since surgery.
    • The pain is mild but constant, especially after prolonged standing or sitting.
    • Denies any new neurological symptoms, such as numbness or weakness in the legs.
    • Reports that physical therapy has improved mobility but the pain has not completely resolved.

Objective:
    • Vitals: BP 128/80 mmHg, HR 75 bpm, Temp 98.7°F.
    • Physical exam:
    • Slight tenderness to palpation in the lumbar region.
    • No muscle spasms detected.
    • Full range of motion in the lower back, but slight discomfort on extension.
    • Neurological exam: normal strength, sensation, and reflexes in the lower extremities.
    • MRI: Shows post-operative changes, no new disc herniation.

Assessment:
    • ICD-10 Codes:
    • M54.5: Low back pain.
    • Z98.89: Post-procedural status (related to prior surgery).
    • CPT Codes:
    • 99214: Established patient office visit, moderate complexity.
    • 72148: MRI of lumbar spine.

Plan:
    • Medications:
    • Meloxicam 15 mg PO once daily for pain relief. RxNorm: 751986.
    • Continue physical therapy focusing on core strengthening.
    • Recommend over-the-counter NSAIDs for pain management.
    • Encourage gradual return to daily activities with attention to proper posture.
    • Follow-up visit in 2 months for reevaluation.
```

## Open AI Summary

```
Key Points from Patient Visits:

- Visit 1 (October 1, 2024): Hip Pain
  - Patient reports increased hip pain, particularly when lying down.
  - Pain described as aching around hip bones and muscles.
  - Slight reduction in hip range of motion, no swelling or erythema noted.
  - Post-surgical changes at L4/L5, no new abnormalities on MRI.
  - Treatment includes Ibuprofen, Cyclobenzaprine, physical therapy, and stretching exercises.

- Visit 2 (September 1, 2024): Upper Arm Pain
  - Persistent pain in the upper arm, worse at night, affecting sleep.
  - Diagnosed tendinitis in deltoid area, confirmed by ultrasound.
  - Range of motion in shoulder restricted to 40%.
  - Prescribed Naproxen and Tizanidine, continued physical therapy, and advised hot/cold compresses.

- Visit 3 (August 1, 2024): Lower Back Pain
  - Persistent mild lower back pain post-microdiscectomy.
  - No new neurological symptoms; physical therapy has improved mobility but not completely alleviated pain.
  - MRI shows post-operative changes, no new issues.
  - Treatment includes Meloxicam, continued physical therapy focusing on core strengthening, and over-the-counter NSAIDs.

Summary Paragraph:

The patient has been experiencing persistent pain in multiple areas, including the hips, upper arms, and lower back, following a microdiscectomy at L4/L5. The hip pain is significant when lying down, and there is a reduction in the range of motion without visible inflammation. Upper arm tendinitis has been confirmed, causing sleep disturbances due to pain, with restricted shoulder mobility. Lower back pain remains mild and constant post-surgery, with no new neurological symptoms. Treatments across the visits have focused on managing pain and inflammation with NSAIDs, muscle relaxants, and targeted physical therapy to improve mobility and strength. Follow-up visits are scheduled to reassess and adjust treatment plans as needed, with an emphasis on non-invasive pain management and mobility enhancement.
```

## Anthropic Summary
```
Key Points:

- Persistent hip pain, worse when lying down
- History of lumbar microdiscectomy at L4/L5 6 months ago
- Upper arm tendinitis, with reduced range of motion and strength
- Lower back pain persisting after surgery
- Physical therapy has improved mobility but pain persists
- Imaging shows post-surgical changes but no new abnormalities

Summary:
The patient presents with a combination of musculoskeletal issues, including persistent hip and lower back pain following a recent lumbar microdiscectomy, as well as upper arm tendinitis. Despite undergoing physical therapy, the patient continues to experience discomfort, particularly when lying down or engaging in certain activities. Imaging studies reveal post-surgical changes but no new concerning findings. The treatment plan involves a combination of anti-inflammatory medications, muscle relaxants, and continued physical therapy focused on improving mobility, strength, and core stability. Close monitoring and follow-up are recommended to assess the effectiveness of the treatment and to address any potential complications or worsening of symptoms.
```

### Setup the file path for proper environment for running the app

```
export PYTHONPATH=/workspaces/patient_summary_app

/workspaces/patient_summary_app/.venv/bin/python -m app.model_orchestrator
```
- Setup the necessary libraries

```
pip install fastapi jinja2 uvicorn
```

- Run the server

```
uvicorn app.app:app --reload
```
