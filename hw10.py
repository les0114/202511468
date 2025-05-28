import os
import pickle

filename = 'score.bin'

def save_scores(scores):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    with open(filename, 'rb') as f:
        return pickle.load(f)

def print_scores(scores):
    print("\n[점수 출력]")
    print("개인점수:", *scores)
    print("평균:", sum(scores)/len(scores) if scores else 0)

def main():
    if os.path.exists(filename):
        scores = load_scores()
        print("\n[파일 읽기]")
        print_scores(scores)
    else:
        scores = []
        print("[점수 입력]")
        while True:
            try:
                score = int(input(f"#{len(scores)+1}? "))
                if score < 0:
                    break
                scores.append(score)
            except ValueError:
                print("정수를 입력하세요.")

        save_scores(scores)
        print_scores(scores)

if __name__ == "__main__":
    main()
