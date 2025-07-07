# Fixed evaluate function using OpenAI instead of Gemini
def evaluate_fixed(reply, message, history) -> Evaluation:
    messages = [{"role": "system", "content": evaluator_system_prompt}]
    messages += [{"role": "user", "content": evaluator_user_prompt(reply, message, history)}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    content = response.choices[0].message.content
    
    # Simple parsing
    import json
    try:
        parsed = json.loads(content)
        return Evaluation(is_acceptable=parsed.get("is_acceptable", True), 
                         feedback=parsed.get("feedback", "No feedback provided"))
    except:
        return Evaluation(is_acceptable=True, feedback=content)

# Usage: Replace the original evaluate function with this one
# evaluate = evaluate_fixed 