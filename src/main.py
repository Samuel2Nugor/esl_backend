from src.db.database import init_db




def main() -> None:
    init_db()
    print("Backend started")
    

if __name__ == "__main__":
    main()
