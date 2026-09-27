REFUSAL='I cannot answer reliably because authorized, applicable evidence is missing or ambiguous.'

def answer(question,retriever,user,today=None):
    results=retriever.retrieve(question,user,today)
    if not results: return REFUSAL
    lines=[]
    for r in results[:3]:
        lines.append(f'{r.document.content} {r.citation}')
    return ' '.join(lines)
