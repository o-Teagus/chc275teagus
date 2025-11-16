# Stock Market Evaluation

def average(prices):
    """Return the average"""
    return sum(prices) / len(prices)

def main():
    try:
        file = open("days.txt", "r")
        buffer = file.readlines()
        file.close()

        day1_20 = buffer[0:3]
        day21_40 = buffer[3:6]

        stocks1 = {}
        stocks2 = {}

        for line in day1_20:
            parts = line.strip().split(",")
            ticker = parts[0]
            numbers = []
            for i in range(1, len(parts)):
                numbers.append(int(parts[i]))
            stocks1[ticker] = numbers

        for line in day21_40:
            parts = line.strip().split(",")
            ticker = parts[0]
            numbers = []
            for i in range(1, len(parts)):
                numbers.append(int(parts[i]))
            stocks2[ticker] = numbers

        report = open("report.txt", "w")

        for ticker in stocks1:
            avg1 = average(stocks1[ticker])
            avg2 = average(stocks2[ticker])

            report.write(f"Ticker: {ticker}\n")
            report.write(f"  Day 1-20 Average: {avg1:.2f}\n")
            report.write(f"  Day 21-40 Average: {avg2:.2f}\n")

            if avg2 > avg1:
                report.write("  Recommend: BUY (average increased)\n\n")
            else:
                report.write("  Recommend: HOLD/SELL (average decreased)\n\n")

        report.close()
        print("Report generated successfully in report.txt")

    except Exception as e:
        print("Error:", e)

main()