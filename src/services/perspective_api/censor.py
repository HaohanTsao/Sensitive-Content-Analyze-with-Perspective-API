from googleapiclient import discovery


class Censor:
    def __init__(self, api_key, sensitive_keywords=[]) -> None:
        """
        Args:
        - api_key (str): The API key for accessing the comment analyzer.
        - sensitive_keywords (list): A list of sensitive keywords to be checked in content.
        """
        self.api_key = api_key
        self.sensitive_keywords = sensitive_keywords
        self.client = discovery.build(
            "commentanalyzer",
            "v1alpha1",
            developerKey=self.api_key,
            discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
            static_discovery=False,
        )

    def analyze(self, content, threshhold=0.5):
        """
        Analyzes the content for sensitivity.

        Args:
        - content (str): The text content to be analyzed.
        - threshhold (float): The sensitivity threshold score.

        Returns:
        - output (dict): containing the analysis results.
        """
        is_sensitive = False
        output = {"is_sensitive": is_sensitive, "toxic_score": 0.0}
        reasons = []

        # request api
        request_body = {
            "comment": {"text": content},
            "requestedAttributes": {"TOXICITY": {}},
        }
        response = self.client.comments().analyze(body=request_body).execute()

        score = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
        output["toxic_score"] = score
        if score >= threshhold:
            is_sensitive = True
            reasons.append("toxic score above threshhold")

        matched_keywords = []
        for sensitive_keyword in self.sensitive_keywords:
            if sensitive_keyword in content:
                is_sensitive = True
                matched_keywords.append(sensitive_keyword)

        if matched_keywords != []:
            output["matched_keywords"] = matched_keywords
            reasons.append(f'Detected sensitive keywords: {" ".join(matched_keywords)}')

        if reasons != []:
            output["reasons"] = reasons

        output["is_sensitive"] = is_sensitive

        return output
