from dj_proposals_candidates.models import Territory, Proposal, Candidate, Commitment
import numpy as np

def dummy_representation(proposal):
    return np.zeros(1)

def process_proposals_from_data(data, url, get_representation_function=dummy_representation):
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
                    proposal.representation = get_representation_function(proposal)
                else:
                    proposal = Proposal.objects.get(remote_id=proposal_id)
                for endorsement in p_dict['node']['endorsements']:
                    profile_path = url+endorsement['profilePath']
                    candidate_exists = Candidate.objects.filter(profile_path=profile_path).exists()
                    if not candidate_exists:
                        candidate = Candidate.objects.create(
                            profile_path=profile_path,
                            name=endorsement['name'],
                            img_url=url+endorsement['avatarUrl'],
                            nickname=endorsement['nickname'],
                            territory=territory
                        )
                    else:
                        candidate = Candidate.objects.get(profile_path=profile_path)
                    
                    commitment, created_commitment = Commitment.objects.get_or_create(candidate=candidate, proposal=proposal)
                    print(commitment)
                      