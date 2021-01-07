from django.core.management.base import BaseCommand, CommandError
from python_graphql_client import GraphqlClient
from dj_proposals_candidates.models import Territory, Proposal


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
                nickname
                name
              }
              author {
                name
                nickname
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
        client = GraphqlClient(endpoint=url)
        data = client.execute(query=query, variables=variables)
        for assembly in data['data']['assemblies']:
            territory_id = assembly['id']
            territory_name = assembly['title']['translations'][0]['text']
            exists_territory = Territory.objects.filter(remote_id=territory_id).exists()
            if not exists_territory:
                territory = Territory.objects.create(remote_id=territory_id, name=territory_name)
            else:
                territory = Territory.objects.get(remote_id=territory_id)
            proposals_component = next(filter(lambda component: component['__typename'] == 'Proposals', assembly['components']), None)
            if proposals_component:
                proposals = proposals_component['proposals']['edges']
                for p_dict in proposals:
                    proposal_dict = p_dict['node']
                    proposal_id = proposal_dict['id']
                    proposal_exists = Proposal.objects.filter(remote_id=proposal_id).exists()
                    if not proposal_exists:
                        proposal = Proposal.objects.create(remote_id=proposal_id,
                                                           title=proposal_dict['title'],
                                                           territory=territory,
                                                           description=proposal_dict['body'],
                                                           votes = proposal_dict['voteCount'])
                    else:
                        proposal = Proposal.objects.get(remote_id=proposal_id)
                    print(proposal, territory)
                
