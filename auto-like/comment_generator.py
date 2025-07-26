import random
from typing import Dict
from openai import OpenAI


class CommentGenerator:
    def __init__(self, api_key: str):
        self.openai_client = OpenAI(api_key=api_key)
    
    def generate_smart_comment(self, post_caption: str, post_type: str, communication_patterns: Dict) -> str:
        """Generate a comment using OpenAI based on learned communication patterns"""
        style_context = self._build_communication_context(communication_patterns)
        
        prompt = f"""You are writing an Instagram comment as a son to their mother's post. 

Your communication style based on WhatsApp analysis:
{style_context}

The post caption is: "{post_caption}"
Post type: {post_type}

Generate a short, natural comment (2-8 words) that sounds like how this person would actually respond to their mom on social media. The comment should be:
- Warm and family-appropriate
- Match the communication style patterns
- Be genuine and not overly enthusiastic unless that's the pattern
- Include relevant emojis if that matches the style

Just return the comment, nothing else."""

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert at mimicking personal communication styles for family interactions."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50,
                temperature=0.7
            )
            
            comment = response.choices[0].message.content.strip()
            comment = comment.strip('"\'')
            
            if not comment or len(comment) > 100:
                comment = self._generate_fallback_comment(communication_patterns)
                
            return comment
            
        except Exception as e:
            print(f"OpenAI API error: {e}")
            return self._generate_fallback_comment(communication_patterns)
    
    def _build_communication_context(self, patterns: Dict) -> str:
        """Build context about communication style for OpenAI"""
        context_parts = []
        
        if patterns.get('common_responses'):
            common = patterns['common_responses'][:5]
            context_parts.append(f"Common responses: {', '.join(common)}")
        
        if patterns.get('emoji_usage'):
            top_emojis = sorted(patterns['emoji_usage'].items(), key=lambda x: x[1], reverse=True)[:3]
            emoji_list = [emoji for emoji, _ in top_emojis]
            context_parts.append(f"Frequently used emojis: {' '.join(emoji_list)}")
        
        if patterns.get('enthusiasm_indicators'):
            context_parts.append("Tends to show enthusiasm with exclamation marks and positive words")
        
        if not context_parts:
            context_parts.append("Casual, family-friendly communication style")
        
        return ". ".join(context_parts)
    
    def _generate_fallback_comment(self, patterns: Dict) -> str:
        """Fallback comment generation if OpenAI fails"""
        default_comments = [
            "❤️", "Beautiful!", "Love this!", "😍", "Amazing!",
            "So nice!", "Perfect! ❤️", "Lovely! 💕"
        ]
        
        if patterns.get('common_responses'):
            appropriate_responses = [
                resp for resp in patterns['common_responses'] 
                if len(resp) > 1 and not any(word in resp.lower() for word in ['work', 'busy', 'meeting'])
            ]
            if appropriate_responses:
                return random.choice(appropriate_responses)
        
        return random.choice(default_comments)
