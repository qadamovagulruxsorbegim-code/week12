def analyze_fines(filename):
    genre_totals = {}  
    severe_books = [] 

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file: 
                parts = line.strip().split(",")  
                if len(parts) != 4:
                    continue  

                title, genre, days_str, fine_str = parts

                try:
                    days = int(days_str)
                    fine = float(fine_str)
                except ValueError:
                    continue  

                total_fine = days * fine
                genre_totals[genre] = genre_totals.get(genre, 0) + total_fine

                if days > 30:
                    severe_books.append((title, days))

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return {}, []

    return genre_totals, severe_books

def save_fine_report(genre_totals, severe_books):
    with open("fine_report.txt", "w", encoding="utf-8") as file:
        file.write("GENRE FINE REVENUE\n")
        file.write("------------------\n")
        for genre, total in genre_totals.items():
            file.write(f"{genre}: ${total:.2f}\n")

        file.write("\nSEVERE DELAYS (> 30 Days)\n")
        file.write("------------------------\n")
        for title, days in severe_books:
            file.write(f"{title} ({days} days)\n")

filename = "C:\\Users\\Windows 10\\Documents\\week12\\assigment\\overdue_log.txt"
genre_totals, severe_books = analyze_fines(filename)

if genre_totals or severe_books:
    save_fine_report(genre_totals, severe_books)
    print("\nReport created: fine_report.txt")
else:
    print("No data found or file missing!")
