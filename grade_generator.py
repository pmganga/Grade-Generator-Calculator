#!/usr/bin/env python3
import csv
from datetime import datetime

def get_valid_grade():
    while True:
        try:
            grade = float(input("Enter_grade obtained (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Error: Grade must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter weight (positive number): "))
            if weight > 0:
                return weight
            print("Error: Weight must be a positive number.")
        except ValueError:
            print("Error: Please enter a valid number.")

def get_category():
    while True:
        cat = input("Enter category (FA or SA): ").strip().upper()
        if cat in ['FA', 'SA']:
            return cat
        print("Error: Category must be FA or SA.")

def main():
    assignments = []
    print("=== Grade Generator Calculator ===\n")

    while True:
        print(f"--- Adding new assignment ---")
        name = input("Enter assignment name: ").strip()
        if not name:
            print("Error: Assignment name cannot be empty.")
            continue

        category = get_category()
        grade = get_valid_grade()
        weight = get_valid_weight()

        assignments.append({
            'name': name,
            'category': category,
            'grade': grade,
            'weight': weight,
            'weighted': (grade / 100) * weight
        })

        again = input("\nAdd another assignment? (y/n): ").strip().lower()
        if again != 'y':
            break
        print()

    if not assignments:
        print("No assignments entered. Exiting.")
        return

    # Calculate totals
    total_fa_weight = sum(a['weight'] for a in assignments if a['category'] == 'FA')
    total_sa_weight = sum(a['weight'] for a in assignments if a['category'] == 'SA')

    total_fa_weighted = sum(a['weighted'] for a in assignments if a['category'] == 'FA')
    total_sa_weighted = sum(a['weighted'] for a in assignments if a['category'] == 'SA')

    total_grade = total_fa_weighted + total_sa_weighted
    gpa = (total_grade / 100) * 5.0

    # Pass/Fail logic: >=50% in EACH category based on their total weight
    fa_needed = total_fa_weight * 0.5
    sa_needed = total_sa_weight * 0.5
    passed_fa = total_fa_weighted >= fa_needed
    passed_sa = total_sa_weighted >= sa_needed
    passed = passed_fa and passed_sa

    # Find lowest FA for resubmission suggestion (if any FA < 50)
    low_fa = [a for a in assignments if a['category'] == 'FA' and a['grade'] < 50]
    resubmit = min(low_fa, key=lambda x: x['grade'])['name'] if low_fa else "None"

    # Console Summary (exact format as transcript)
    print("\n" + "="*80)
    print("Assignment\t\tCategory\tGrade (%)\tWeight\tFinal weight")
    print("-"*80)
    for a in assignments:
        print(f"{a['name']:<25}\t{a['category']}\t\t{a['grade']:<8}\t{a['weight']}\t{a['weighted']:.2f}")
    print("-"*80)
    print(f"Formatives ({total_fa_weight})\t\t\t\t\t{total_fa_weighted:.1f}")
    print(f"Summatives ({total_sa_weight})\t\t\t\t\t{total_sa_weighted:.2f}")
    print("\nGPA\t{:.4f}".format(gpa))
    print("\nStatus\t\t\t\t\tPASSED" if passed else "Status\t\t\t\t\tFAILED")
    print(f"Available for resubmission\t\t{resubmit}")
    print("="*80)

    # Export to CSV
    with open('grades.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])
        for a in assignments:
            writer.writerow([a['name'], a['category'], a['grade'], a['weight']])

    print(f"\nData successfully saved to grades.csv")

if __name__ == "__main__":
    main()
