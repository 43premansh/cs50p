from datetime import date
import inflect


def main():
    d = input("your DOB as YYYY-MM-DD: ")
    today = date.today()
    birth = date.fromisoformat(d)
    diff = today - birth
    print(diff.days * 24 * 60)
    p = inflect.engine()
    print(p.number_to_words((diff.days * 24 * 60), andword = " "))


if __name__ == "__main__":
    main()
