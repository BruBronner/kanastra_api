import sys
from services.portfolio_service import PortfolioService


def main():
    if len(sys.argv) < 4:
        print("Uso: python main.py <data_inicio> <data_fim> <slug>")
        return

    start_date = sys.argv[1]
    end_date = sys.argv[2]
    slug = sys.argv[3]

    service = PortfolioService()

    try:
        service.fluxo_completo(start_date, end_date, slug)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()