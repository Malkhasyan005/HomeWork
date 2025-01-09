with open("story.txt", 'r') as f:
    text = f.read().strip()
    print(f"Total lenght = {len(text.split())}")
