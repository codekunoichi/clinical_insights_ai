class VisitSummary:
    def __init__(self, text_snippets: list):
        self.text_snippets = text_snippets

    def get_text(self) -> str:
        """Combine and return the visit summary text snippets."""
        return " ".join(self.text_snippets)
    
    @staticmethod
    def get_sample_visits() -> list:
        return [diagnosis_visit_note]
    
    @staticmethod
    def get_medication_adherance() -> tuple:
        return [medication_adherance_note], [medication_adherance_response]
    
    @staticmethod
    def get_diagnosis_visit_note() -> list:
        return [diagnosis_visit_note]

    @staticmethod
    def get_lab_result_samplenote() -> list:
        return [lab_result]
    
    @staticmethod
    def get_visit_1():
        return [visit_1]
    
    @staticmethod
    def get_visit_2():
        return [visit_2]
    
    @staticmethod
    def get_visit_3():
        return [visit_3]
    
    @staticmethod
    def get_visit_4():
        return [visit_4]
    
    @staticmethod
    def get_sdoh_visit():
        return sdoh_visit
    
    @staticmethod
    def get_followup_visit():
        return follow_up_example

    @staticmethod
    def get_previst_planning_visit():
        return previsit_example


visit_4 = """Pre-operation evaluation for cataract surgery, left side. Patient planning for cataract surgery and denying difficult breathing, denying chest pain, denying nausea, vomiting, denying breathing. Next paragraph. Patient was evaluated by cardiology. According to cardiology report, on July 22, patient had CAD. CAD concern had stress positive on 2022. Last CAT showed LAD mild. Patient on aspirin. Patient denied any chest pain but had exertion shortness of breath. Next paragraph. Patient also had severe apnea, snoring, denying any severe. Next paragraph. Pre-diabetic hemoglobin A1c 6.4, non-compliant with the IR. Next paragraph. Next paragraph. COPD. Patient will have COPD. Was on inhaler and followed up by pulmonary. Recent CT scan was told unremarkable. CT scan on March 2023 shows emphysema in aorta, ascending aorta. Next paragraph. ECTASIS 3.9 cm. CT scan on the left upper lobe 1.6 cm was told stable by pulmonary. Assessment pre-operation evaluation, medical stable for cataract. This gastric patient continued on aspirin and Serato unless contraindicated by ophthalmology. Next paragraph. Emphysema. This gastric patient continued on the inhaler including Comvavent, COMVI, ENT inhaler stable. CT scan showed emphysema. Next paragraph. CAD with angina. Patient continued on Lipitor 20 mg and aspirin stable. Next paragraph. Patient had psoriasis. Psoriasis was followed by rheumatology. Continued on MTX 2.53 tablet and also another medication OTE ZLA 30 mg. Patient continued followed by rheumatology."""

# Example patient visit notes (this would be dynamic in a real app)
visit_1 = """
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
"""
# Example visit_2
visit_2 = """
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
"""

# example visit_3
visit_3 = """
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
"""

lab_result = """Lab Results for: John Doe
Date: October 10, 2024

HbA1c (Hemoglobin A1c):
- HbA1c: 6.5% (Normal: 4.0% - 5.6%)
  - Interpretation: Consistent with Diabetes

Complete Blood Count (CBC):
- Hemoglobin: 14.8 g/dL (Normal: 13.8 - 17.2 g/dL)
- Hematocrit: 44.5% (Normal: 40.7 - 50.3%)
- White Blood Cells (WBC): 9.5 x10^9/L (Normal: 4.5 - 11.0 x10^9/L)
- Platelet Count: 250 x10^9/L (Normal: 150 - 400 x10^9/L)
- Mean Corpuscular Volume (MCV): 89 fL (Normal: 80 - 100 fL)

Basic Metabolic Panel:
- Sodium: 140 mmol/L (Normal: 135 - 145 mmol/L)
- Potassium: 4.3 mmol/L (Normal: 3.5 - 5.0 mmol/L)
- Chloride: 102 mmol/L (Normal: 98 - 107 mmol/L)
- Bicarbonate: 25 mmol/L (Normal: 22 - 29 mmol/L)
- Blood Urea Nitrogen (BUN): 18 mg/dL (Normal: 7 - 20 mg/dL)
- Creatinine: 1.0 mg/dL (Normal: 0.6 - 1.2 mg/dL)
- Glucose (Fasting): 105 mg/dL (Normal: 70 - 99 mg/dL)
  - Interpretation: Mildly elevated fasting glucose level (Pre-Diabetes)
- Calcium: 9.4 mg/dL (Normal: 8.5 - 10.2 mg/dL)

Liver Enzymes (Part of the Metabolic Panel):
- Alanine Aminotransferase (ALT): 22 U/L (Normal: 7 - 55 U/L)
- Aspartate Aminotransferase (AST): 18 U/L (Normal: 8 - 48 U/L)
"""

sdoh_visit = """Visit 1: October 1, 2024

Subjective:
    • The patient reports an increase in hip pain, especially when lying down.
    • Describes the pain as aching, mainly located around the hip bones and muscles.
    • The patient also reports occasional upper arm aches when in a lying position.
    • No radiating pain down the legs.
    • Microdiscectomy at L4/L5 was performed 6 months ago, and the patient denies any radiating pain to the lower extremities.
    • The patient reports difficulty managing blood sugar levels, with fasting glucose consistently over 130 mg/dL over the last few weeks.
    • The patient reports concerns about the affordability of medications, noting difficulty paying for insulin and other diabetes-related medications.

Objective:
    • Vitals: BP 130/85 mmHg, HR 72 bpm, Temp 98.6°F, BMI 28.
    • Physical exam:
        • Tenderness on palpation around both hip bones.
        • No visible swelling or erythema.
        • Range of motion in hips slightly reduced.
        • Neurological exam normal: no signs of numbness or weakness in lower extremities.
    • Recent imaging: Lumbar MRI shows post-surgical changes at L4/L5 but no new abnormalities.
    • Diabetes Management:
        • HbA1c: 8.2% (elevated, goal < 7%).
        • Fasting glucose: 135 mg/dL (normal: 70-99 mg/dL).
    • Social Determinants of Health:
        • Reports financial difficulty affording medications, specifically insulin and glucose monitoring supplies.

Assessment:
    • ICD-10 Codes:
        • M25.551: Pain in right hip.
        • M25.552: Pain in left hip.
        • M54.5: Low back pain.
        • E11.65: Type 2 diabetes mellitus with hyperglycemia.
        • Z59.7: Insufficient social insurance and welfare support (related to medication affordability).
    • CPT Codes:
        • 99214: Established patient office visit, moderate complexity.
        • 72148: MRI of lumbar spine.
        • 83036: Hemoglobin A1c measurement.
        • 99401: Preventive care counseling, addressing diabetes management and SDOH concerns.

Plan:
    • Medications:
        • Ibuprofen 600 mg PO every 8 hours as needed for pain. RxNorm: 5640.
        • Cyclobenzaprine 10 mg PO at bedtime for muscle relaxation. RxNorm: 3112.
        • Insulin glargine 10 units at bedtime. RxNorm: 123456.
        • Continue Metformin 500 mg BID. RxNorm: 860975.
    • Diabetes Management:
        • Referral to endocrinology for diabetes management and medication adjustment.
        • Referral to social worker to assist with financial resources for insulin and glucose monitoring supplies.
    • Continue physical therapy for mobility improvement.
    • Recommended stretching exercises for hips and back.
    • Follow up in 4 weeks for reassessment of hip pain and diabetes control.
    • Consider adding a home health aide if the patient's diabetes control does not improve.
"""

diagnosis_visit_note = """Patient Name: John Doe
Visit Date: October 10, 2024

Chief Complaint: Increased fatigue and muscle weakness.

History of Present Illness:
The patient reports progressive fatigue over the last few weeks. Complains of general muscle weakness, particularly in the arms. No recent illnesses or injuries. No chest pain, shortness of breath, or palpitations. Blood pressure and heart rate are stable.

The patient is concerned about managing their diabetes due to financial difficulties in affording insulin and glucose testing supplies.

Medications:
Metformin 500mg BID, Lisinopril 10mg daily.

Physical Exam:
General: Alert and oriented.
Heart: Regular rate and rhythm.
Lungs: Clear to auscultation bilaterally.
Extremities: Mild muscle weakness in upper arms, normal reflexes.

Assessment and Plan:
- Likely cause of fatigue: medication side effects (Lisinopril).
- Type 2 diabetes, uncontrolled, contributing to fatigue.
- Referral to endocrinology for diabetes management.
- Patient referred to social services for assistance with insulin and glucose supply costs.
- Follow-up in 2 weeks to reassess symptoms.
"""

medication_adherance_note = """Visit Date: October 10, 2024

Subjective:
- The patient reports feeling lightheaded in the morning but denies any chest pain or shortness of breath. 
- They have been experiencing fatigue and mild headaches, especially after exertion.

Objective:
- Vitals: BP 135/85 mmHg, HR 80 bpm, Temp 98.1°F.
- Physical exam: The heart and lung sounds are normal. Mild pallor observed.

Assessment:
- Hypertension (ICD-10: I10).
- Fatigue, likely related to hypertension and suboptimal medication adherence.
- Headaches, likely related to elevated blood pressure.

Plan:
- Increase Lisinopril dosage from 10 mg to 20 mg daily.
- Emphasize the importance of adhering to the prescribed medication regimen.
- Follow-up in 4 weeks to reassess blood pressure and symptoms."""

medication_adherance_response = """- Medication Adherence Responses:
  - "Do you ever forget to take your medicine?": Yes, about once a week.
  - "When you feel better, do you sometimes stop taking your medicine?": Sometimes, especially when symptoms improve.
  - "If you feel worse when you take your medicine, do you sometimes stop taking it?": No, I continue taking it.
  - "Do you sometimes take your medicine differently from how your doctor prescribed?": Yes, occasionally I reduce the dose when I feel better."""
# example = VisitSummary(VisitSummary.get_sample_visits())
# print(example.get_text())

follow_up_example = """
Visit Date: October 15, 2024

Subjective:
- The patient reports mild abdominal discomfort for the past week. No significant weight loss or changes in bowel habits.
- Family history of breast cancer (mother) and colorectal cancer (father).

Objective:
- Vitals: BP 125/80 mmHg, HR 70 bpm, Temp 98.7°F.
- Physical exam: Abdomen soft with mild tenderness in the lower quadrant.

Assessment:
- Abdominal pain, likely non-urgent but requiring imaging.
- Routine cancer screening based on family history.

Plan:
- Schedule a CAT Scan of the abdomen within the next two weeks.
- Routine mammogram recommended in two years.
- FOBT (Fecal Occult Blood Test) for colorectal cancer screening to be performed annually starting this year.
"""

previsit_example = """
John Doe, a 58-year-old male, office worker who quit smoking 5 years ago, came in today saying he’s had a bit of discomfort after meals. He is still on his usual meds—Metformin, Lisinopril, and Simvastatin—and he says he’s pretty consistent with them. His last blood pressure check was slightly high, 135/85, but nothing unusual. His HbA1c came in at 7.1%, which is a little higher than we’d like to see but not a huge concern yet. We’ll need to keep an eye on that. He did his cholesterol panel recently too, and his LDL is fine, sitting at 100 mg/dL.

John also mentioned he got his flu shot last month. He’s up to date with his vaccinations except for his pneumococcal vaccine, which he’ll need again in 6 months. His diabetes is mostly under control, but I’ve asked him to see an endocrinologist for an opinion, especially considering his history with hyperlipidemia.

He hasn’t had a colonoscopy in 7 years, which is overdue. He also needs to schedule a diabetic eye exam, as it’s been over a year since his last one. During the visit, we talked a bit about his diet, but he says he hasn’t changed much, and that’s likely why his HbA1c hasn’t improved. He’s still at a BMI of 28.5, so we should also keep monitoring his weight.

He’s going to follow up with me in November to recheck his diabetes numbers and make sure the referrals are moving forward. He’s still a little stressed from work, but he hasn’t noticed any new issues. I’ll write up a referral to endocrinology and suggest that we book his follow-up appointments before the end of the year.”

This text contains excessive narrative and information that isn’t immediately necessary for pre-visit planning. It includes lifestyle details, general comments, and less organized follow-up items scattered throughout the note. Testing your PreVisitPlanningPrompter with this kind of noisy input will demonstrate how the system can distill the essential medical information (medications, lab results, referrals, and screenings) from the extraneous context.
"""