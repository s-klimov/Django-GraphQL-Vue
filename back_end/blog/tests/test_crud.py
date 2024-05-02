import json

from graphene_django.utils.testing import GraphQLTestCase


class BlogListTestCase(GraphQLTestCase):

    fixtures = ["tags.json", "users.json", "profiles.json", "posts.json"]

    GRAPHQL_URL = "/graphql/"

    def test_get_articles(self):
        response = self.query(
            """
                query {
                  allPosts {
                    title
                    author {
                      user {
                        username
                      }
                    }
                    tags {
                      name
                    }
                  }
                }
            """
        )

        content = json.loads(response.content)

        self.assertResponseNoErrors(response)

        self.assertEqual(len(content["data"]["allPosts"]), 1)
        self.assertEqual(
            content["data"]["allPosts"][0]["title"], "I started to learn English"
        )
