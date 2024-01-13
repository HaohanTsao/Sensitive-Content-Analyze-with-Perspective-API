from src.functions.content_censor import content_censor
from dotenv import load_dotenv

load_dotenv()


def main(req):
    content_censor(req)


if __name__ == "__main__":
    main()
