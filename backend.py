
"""
data = [
    {"number":0,
     "name": "",
     "tags": ["dp","array"],
     "date": 222202,
     "url": "www.problem/sjksjkskjs"
     }

]
"""

import json
import leetcode

# Get the next two values from your browser cookies
leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb2NpYWxhY2NvdW50X3NvY2lhbGxvZ2luIjp7ImFjY291bnQiOnsiaWQiOm51bGwsInVzZXJfaWQiOm51bGwsInByb3ZpZGVyIjoiZ29vZ2xlIiwidWlkIjoiMTA5MTU0ODA2OTAzOTYzNTI2MTUwIiwibGFzdF9sb2dpbiI6bnVsbCwiZGF0ZV9qb2luZWQiOm51bGwsImV4dHJhX2RhdGEiOnsiaWQiOiIxMDkxNTQ4MDY5MDM5NjM1MjYxNTAiLCJlbWFpbCI6Im5lbHNvbmR1dGhlbjQyQGdtYWlsLmNvbSIsInZlcmlmaWVkX2VtYWlsIjp0cnVlLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FMVi1ValZTaUpHUkVtUmNLNVBwU0hoYzJzRS1qY0g3Q1F5Z0NKZjFfN1FsSkxfTVV6cm55Zz1zOTYtYyJ9fSwidXNlciI6eyJpZCI6bnVsbCwicGFzc3dvcmQiOiIhbDZpbWpmS1FKNzBGQW5ZQUpJT0d4WEJ6VkcyNEdkVDA0em16NEJhNCIsImxhc3RfbG9naW4iOm51bGwsImlzX3N1cGVydXNlciI6ZmFsc2UsInVzZXJuYW1lIjoiIiwiZmlyc3RfbmFtZSI6IiIsImxhc3RfbmFtZSI6IiIsImVtYWlsIjoibmVsc29uZHV0aGVuNDJAZ21haWwuY29tIiwiaXNfc3RhZmYiOmZhbHNlLCJpc19hY3RpdmUiOnRydWUsImRhdGVfam9pbmVkIjoiMjAyNS0wMS0wOVQxODo0NDo1NC4wNDhaIn0sInN0YXRlIjp7Im5leHQiOiIvIiwicHJvY2VzcyI6ImxvZ2luIiwic2NvcGUiOiIiLCJhdXRoX3BhcmFtcyI6IiJ9LCJlbWFpbF9hZGRyZXNzZXMiOlt7ImlkIjpudWxsLCJ1c2VyX2lkIjpudWxsLCJlbWFpbCI6Im5lbHNvbmR1dGhlbjQyQGdtYWlsLmNvbSIsInZlcmlmaWVkIjp0cnVlLCJwcmltYXJ5Ijp0cnVlfV0sInRva2VuIjp7ImlkIjpudWxsLCJhcHBfaWQiOjEsImFjY291bnRfaWQiOm51bGwsInRva2VuIjoieWEyOS5hMEFSVzVtNzV1a3R1ZHdITDhQcnZpcFdNaEF5WVVyY2oybW04QURIU2ZkOW5pc1cxb2hFX3lMZGd2WFpTTm9jYVlfVGxsQlozX0dDcy1fQnp0RE5tYnQxUWQwLVQ2NGxsVUlDTHUtR1lVLVRzUy1vRzVFN09ZUTdIT0psZDU1UHVLNDNtOXc5eTZZTnZyWC1veS0zZ1M2N3ZDT3JxSWR6SnFkUVJIYUNnWUtBVG9TQVJFU0ZRSEdYMk1pWGtuWldjYldHNmZDdXFDbGlmaDhYUTAxNzEiLCJ0b2tlbl9zZWNyZXQiOiIiLCJleHBpcmVzX2F0IjoiMjAyNS0wMS0wOVQxOTo0NDo1Mi45NzhaIn19LCJfcGFzc3dvcmRfcmVzZXRfa2V5IjoiY2pjejdwLTRkN2IyNTMxMjAwZDlhOTIwOTFiMWUzZjNiMTZiNWRiIiwiX2F1dGhfdXNlcl9pZCI6Ijc3NzY4NDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiNzJjNzQ4N2IxMGI2YzdmY2IyYTFmMmEwOWMxOWM2N2RjMGY1NjQ5MjY0ZGZiMTE3NzUzYWY0MjFiMjMwN2Q2Iiwic2Vzc2lvbl91dWlkIjoiM2RmNzA1MWEiLCJpZCI6Nzc3Njg0OCwiZW1haWwiOiJuZWxzb25kdXRoZW40MkBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Im5lbHNvbnRoZW40MiIsInVzZXJfc2x1ZyI6Im5lbHNvbnRoZW40MiIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9uZWxzb250aGVuNDIvYXZhdGFyXzE3MzYzMTcwNjcucG5nIiwicmVmcmVzaGVkX2F0IjoxNzM3NzY3MzE2LCJpcCI6IjEyOS45Ni44NS42OSIsImlkZW50aXR5IjoiMDg0NWIzMDljN2I5Yjk1N2FmZDllY2Y3NzVhNGMyMWYiLCJkZXZpY2Vfd2l0aF9pcCI6WyI2YTBkYzgyODZmZGM0YWIzMDYyYTEwMTE3N2ExNTI2MSIsIjEyOS45Ni44NS42OSJdLCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.GMsHrWxyKZrgKKJ-f7nLTUrFtCCggNFm0Vjl1OCbels"
csrf_token = "1zRX2BK8e4qERBwRhKoEkAKBnlJKlJT6xwMwTaFpREu72x2svHsA56F4V2UfYzoU"

# Experimental: Or CSRF token can be obtained automatically
import leetcode.auth

# Configure the API client
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

def get_problem_tags_by_slug(slug):
    """
    Fetch the tags of a problem given its title-slug.

    Args:
        slug (str): The title-slug of the problem.

    Returns:
        List[str]: A list of tags associated with the problem.
    """
    try:
        # Construct the GraphQL query
        graphql_request = leetcode.GraphqlQuery(
            query="""
                query getQuestionDetail($titleSlug: String!) {
                  question(titleSlug: $titleSlug) {
                    topicTags {
                      name
                      slug
                    }
                  }
                }
            """,
            variables={"titleSlug": slug},  # Pass variables as a dictionary
            operation_name="getQuestionDetail",
        )

        # Make the API request
        api_response = api_instance.graphql_post(body=graphql_request)

        # Extract the tags
        tags = [tag.slug for tag in api_response.data.question.topic_tags]
        return tags

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

import json

def fetch_leetcode_problems_from_file(file_path):
    try:
        # Read the JSON data from the file
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Parse the JSON data
        data = json.loads(file_content)

        # Extract problems from the JSON content
        problems = data.get("stat_status_pairs", [])

        # Create the formatted data array
        formatted_data = [
            {
                "question_id": problem["stat"]["frontend_question_id"],
                "title-slug": problem["stat"]["question__title_slug"],
                "status": problem["status"] == "ac",  # True if status is "ac", otherwise False
                "total_acs": problem["stat"]["total_acs"],
                "total_submitted": problem["stat"]["total_submitted"],
                "difficulty": problem["difficulty"]["level"]  # 1 = Easy, 2 = Medium, 3 = Hard
            }
            for problem in problems
        ]

        return formatted_data

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"An error occurred while reading or parsing the file: {e}")
        return []

# Example usage
if __name__ == "__main__":
    file_path = "problemsdata.txt"  # Replace with your file path
    leetcode_data = fetch_leetcode_problems_from_file(file_path)
    for d in leetcode_data:
        print(d)

