from src.functions.content_censor import content_censor
from dotenv import load_dotenv

load_dotenv()


def main(req):
    response = content_censor(req)
    return response


if __name__ == "__main__":
    main()
