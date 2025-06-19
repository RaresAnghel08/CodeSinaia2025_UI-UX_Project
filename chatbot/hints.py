# predefined hints
hints = {
    "hint1": "split_message = re.split(r'\\s+|[,;?.-]\\s*', user_input.lower())",
    "hint2": "return check_all_messages(split_message)",
    "hint3": "return best_response if highest_prob > 0 else unknown()",
    "hint4": "if prob > highest_prob: highest_prob = prob; best_response = rule['response']",
    "hint5": "prob = message_probability(message, rule['keywords'], rule.get('single_response', False), rule.get('required', []))",
    "hint6": "message_certainty = sum(1 for word in user_message if word in keywords)",
    "hint7": "match_ratio = message_certainty / len(keywords) if keywords else 0",
    "hint8": "\"keywords\": [\"favorite\", \"color\"], \"required\": [\"color\"], \"response\": My favourite color is blue, \"single_response\": True"
    
}
