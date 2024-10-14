from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))



# Function to create the prompt for summarization
def create_prompt(patient_notes):
    # Prompt components
    persona = (
        "You are an expert in Large Language models. You excel at breaking down complex papers "
        "into digestible summaries. You are also an expert primary care physician.\n"
    )
    instruction = "Summarize the key findings of the patient chart from past visit summaries.\n"
    context = (
        "Your summary should extract the most crucial points that can help medical assistants, "
        "physicians, and care providers quickly understand the most vital information in the patient chart.\n"
    )
    data_format = (
        "Create a bullet-point summary that outlines the key points. Follow this up with a concise "
        "paragraph that encapsulates the patient's condition, trends, and the most important information from the visits.\n"
    )
    audience = (
        "The summary is designed for busy healthcare providers who need to quickly grasp the patient's health trends "
        "in prior visit notes.\n"
    )
    tone = "The tone should be professional and clear.\n"
    data = f"Text to summarize: {patient_notes}"

    # Combine all components into one prompt
    prompt = persona + instruction + context + data_format + audience + tone + data

    return prompt

# Function to call OpenAI API with prompt
def summarize_patient_notes(patient_notes):
    # Generate the prompt
    prompt = create_prompt(patient_notes)

    # Format the prompt for gpt-3.5-turbo (it expects messages in a chat format)
    messages = [
        {"role": "system", "content": "You are an expert summarizer of patient visit notes."},
        {"role": "user", "content": prompt}
    ]

    # Use the gpt-3.5-turbo model for chat-based completion
    response = client.chat.completions.create(
        model= "gpt-4-turbo", #"gpt-4o-mini" ,
        messages=messages,
        temperature=0.5,
        max_tokens=500,
        n=1
    )

    print(response)
    # Extract the response text
    summary = response.choices[0].message.content.strip()
    return summary

# Function to convert to ASCII-friendly output (removes Markdown-like syntax)
def convert_to_ascii(text):
    # Replace bold markdown (**text**) with dashes
    text = text.replace('**', '')
    
    # Replace bullet points (-) with dashes (--)
    #text = text.replace('- ', '-- ')
    
    # Return the converted text
    return text

# Example patient visit notes (this would be dynamic in a real app)
text = """
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
"""

# Call the summarization function
summary = summarize_patient_notes(text)
#print(summary)

# Convert the summary to ASCII-friendly format
ascii_summary = convert_to_ascii(summary)

# Output the ASCII-formatted summary
print(ascii_summary)