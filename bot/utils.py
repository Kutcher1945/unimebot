import openpyxl

def get_faq_context(path: str) -> str:
    wb = openpyxl.load_workbook(path)
    sheet = wb["FAQ"]

    faq_lines = []
    for row in sheet.iter_rows(min_row=3, values_only=True):
        question = row[1]
        answer = row[4]
        if question and answer:
            faq_lines.append(f"Q: {question.strip()}\nA: {answer.strip()}")

    return "\n\n".join(faq_lines)
