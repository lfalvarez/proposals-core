from dj_proposals_candidates.models import Territory, Proposal, Candidate, Commitment
import numpy as np


def dummy_representation(proposal):
    return np.zeros(1)


def get_terrytory_from_proposal_dict(scope):
    remote_territory_id = scope['id']
    territory_name = scope['name']['translations'][0]['text']
    exists_territory = Territory.objects.filter(remote_id=remote_territory_id).exists()
    if not exists_territory:
        territory = Territory.objects.create(remote_id=remote_territory_id, name=territory_name)
    else:
        territory = Territory.objects.get(remote_id=remote_territory_id)
    return territory


def process_proposals_from_data(data, url, get_representation_function=dummy_representation):
    for assembly in data['data']['assemblies']:
        assembly_id = assembly['id']
        proposals_component = next(
            filter(lambda component: component['__typename'] == 'Proposals', assembly['components']), None)
        if proposals_component:
            proposals = proposals_component['proposals']['edges']
            proposals_component_id = proposals_component['id']
            for p_dict in proposals:
                proposal_dict = p_dict['node']
                territory = get_terrytory_from_proposal_dict(proposal_dict['scope'])
                proposal_id = proposal_dict['id']
                proposal_exists = Proposal.objects.filter(remote_id=proposal_id).exists()
                if not proposal_exists:
                    remote_url = '/assemblies/{territory_id}/f/{proposals_component_id}/proposals/{proposal_id}'
                    remote_url = remote_url.format(territory_id=assembly_id,
                                                   proposals_component_id=proposals_component_id,
                                                   proposal_id=proposal_id)
                    remote_url = url + remote_url
                    proposal = Proposal.objects.create(remote_id=proposal_id,
                                                       title=proposal_dict['title'],
                                                       territory=territory,
                                                       description=proposal_dict['body'],
                                                       votes=proposal_dict['voteCount'],
                                                       remote_url=remote_url
                                                       )
                    proposal.representation = get_representation_function(proposal)
                else:
                    proposal = Proposal.objects.get(remote_id=proposal_id)
                for endorsement in p_dict['node']['endorsements']:
                    profile_path = url + endorsement['profilePath']
                    candidate_exists = Candidate.objects.filter(profile_path=profile_path).exists()
                    if not candidate_exists:
                        candidate = Candidate.objects.create(
                            profile_path=profile_path,
                            name=endorsement['name'],
                            img_url=url + endorsement['avatarUrl'],
                            nickname=endorsement['nickname'],
                            territory=territory
                        )
                    else:
                        candidate = Candidate.objects.get(profile_path=profile_path)

                    commitment, created_commitment = Commitment.objects.get_or_create(candidate=candidate,
                                                                                      proposal=proposal)
                    print(commitment)
