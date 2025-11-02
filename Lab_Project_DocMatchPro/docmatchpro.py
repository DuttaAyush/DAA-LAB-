import re, csv
import math
from collections import Counter

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.strip()

def compute_tfidf_cosine(a, b):
    docs = [a.split(), b.split()]
    all_words = list(set(docs[0] + docs[1]))
    N = len(docs)

    idf = {}
    for w in all_words:
        df = sum(1 for doc in docs if w in doc)
        idf[w] = math.log((N + 1) / (df + 1)) + 1

    tfidf_vecs = []
    for doc in docs:
        tf = Counter(doc)
        vec = [tf[w] / len(doc) * idf[w] for w in all_words]
        tfidf_vecs.append(vec)

    A, B = tfidf_vecs
    dot = sum(x*y for x, y in zip(A, B))
    normA = math.sqrt(sum(x*x for x in A))
    normB = math.sqrt(sum(y*y for y in B))
    return 0 if normA == 0 or normB == 0 else dot / (normA * normB)

def lcs(a, b):
    a, b = a.split(), b.split()
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n] / max(1, max(m, n))

def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return 1 - (dp[m][n] / max(1, max(m, n)))

def line_similarity(line1, line2):
    c = compute_tfidf_cosine(line1, line2)
    l = lcs(line1, line2)
    e = edit_distance(line1, line2)
    return round((c*0.5 + l*0.25 + e*0.25), 3)

def compare_documents(file1, file2, output="comparison_report.csv"):
    with open(file1, 'r', encoding='utf-8') as f:
        lines1 = [preprocess(x) for x in f.readlines() if x.strip()]
    with open(file2, 'r', encoding='utf-8') as f:
        lines2 = [preprocess(x) for x in f.readlines() if x.strip()]

    results = []
    total_score = 0
    for i, l1 in enumerate(lines1, 1):
        best_score, best_line = 0, ""
        for l2 in lines2:
            score = line_similarity(l1, l2)
            if score > best_score:
                best_score, best_line = score, l2
        total_score += best_score
        results.append([i, l1, best_line, best_score])

    overall_similarity = (total_score / len(lines1)) * 100 if lines1 else 0

    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Line_No", "Line_from_Doc1", "Most_Similar_Line_in_Doc2", "Similarity_Score"])
        writer.writerows(results)

    print(f"\nPlagiarism Detected: {overall_similarity:.2f}%")
    print(f"Detailed report saved as {output}")
    return overall_similarity

# Example usage
if __name__ == "__main__":
    compare_documents("doc1.txt", "doc2.txt")
