"""Prompt templates for toxic comment classification."""

PROMPT_SIMPLE = """Is this comment toxic? A comment is toxic if it contains hate speech, harassment, threats, or severe insults.
Reply only "yes" or "no".

Comment: {comment}

Answer:"""


PROMPT_DETAILED = """You are a content moderator for a large platform. A comment is toxic if it:
- Attacks someone personally (insults, name-calling)
- Contains hate speech or discrimination
- Includes threats or wishes harm
- Uses severe profanity in an attacking way

Does this comment meet the toxic criteria? Reply only "yes" or "no".

Comment: {comment}

Answer:"""


PROMPT_FEWSHOT = """You are a content moderator. Classify if comments are toxic.

Examples:
Comment: "Oh wow, you're SO smart 🙄 maybe think before you post next time" -> yes
Comment: "I mean, people like that just shouldn't be on the internet" -> yes
Comment: "This is objectively wrong and you clearly didn't do any research" -> yes
Comment: "Not my favorite approach but I see where you're coming from" -> no
Comment: "I hate how this platform keeps recommending this garbage" -> no
Comment: "Some people just aren't cut out for this, and that's okay" -> yes
Comment: "The editing was rough and the pacing felt off to me" -> no
Comment: "Bold of you to post this with that profile picture 💀" -> yes
Comment: "I respectfully disagree — the data doesn't support that claim" -> no
Comment: "Sure, if you ignore literally every fact, that makes sense" -> yes
Comment: "J Bar and C Fred are having anal sex together...." -> yes
Comment: "You're watching Dirty Jobs too I guess? Haha......" -> yes

Now classify the following comment. Reply only "yes" or "no", nothing else.

Comment: {comment}

Answer:"""


PROMPT_MORE_DETAILED = """You are a content moderator for a large platform. 
A comment is toxic if it:
- Attacks someone personally (insults, name-calling, mockery)
- Contains hate speech or discrimination against a group
- Includes threats or wishes harm on a person or group
- Uses severe profanity in an attacking or demeaning way
- Uses sarcasm or irony to belittle or demean someone
- Dismisses or demeans someone's intelligence or worth ("you clearly don't understand anything")
- Makes someone feel unwelcome or excluded based on who they are
- Uses backhanded compliments or passive-aggressive language to attack


Does this comment meet the toxic criteria? Reply only "yes" or "no".

Comment: {comment}

Answer:"""