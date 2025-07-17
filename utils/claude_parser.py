from anthropic import Anthropic

anthropic = Anthropic(api_key="your_claude_api_key")

def get_action_from_prompt(prompt: str) -> str:
    completion = anthropic.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=50,
        temperature=0,
        messages=[
            {"role": "user", "content": f"What should be done in this instruction? {prompt}\nReply with just one word: 'configure', 'troubleshoot', or 'audit'."}
        ]
    )
    return completion.content[0].text.strip().lower()
