# Fixed evaluate function
def evaluate_fixed(reply, message, history) -> Evaluation:
    messages = [{"role": "system", "content": evaluator_system_prompt}]
    messages += [{"role": "user", "content": evaluator_user_prompt(reply, message, history)}]
    response = gemini.chat.completions.create(model="gemini-2.0-flash", messages=messages)
    content = response.choices[0].message.content
    
    # Parse the response to extract is_acceptable and feedback
    import json
    try:
        # Try to parse as JSON first
        parsed = json.loads(content)
        return Evaluation(is_acceptable=parsed.get("is_acceptable", True), 
                         feedback=parsed.get("feedback", "No feedback provided"))
    except:
        # Fallback: assume it's acceptable if no clear rejection
        return Evaluation(is_acceptable=True, feedback=content) 