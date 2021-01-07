from django.core.management.base import BaseCommand, CommandError
from python_graphql_client import GraphqlClient
from dj_proposals_candidates.create_proposals_from_data import process_proposals_from_data


query = """
{

  assemblies {
    id
    title {
      translations {
        text
      }
    }
    components {
      __typename
      ... on Proposals {
        id
        name {
          translations {
            text
          }
        }
        proposals(first: 1000) {
          edges {
            node {
              id
              title
              state
              body
              voteCount
              endorsements {
                profilePath
                avatarUrl
                nickname
                name
              }
              author {
                profilePath
                avatarUrl
                nickname
                name
              }
            }
          }
        }
      }
    }
  }
}
"""
variables = {}


class Command(BaseCommand):
    help = 'Carga desde un endpoint con graphql'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs=1, type=str)

    def handle(self, *args, **options):
        url = options['url'][0]
        api_url = "{url}/api".format(url = url)
        client = GraphqlClient(endpoint=api_url)
        data = client.execute(query=query, variables=variables)
        process_proposals_from_data(data, url)
                
