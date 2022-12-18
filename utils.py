import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_candidate_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_candidate_by_name(candidate_name):
    result = []
    for candidate in load_candidates():
        if candidate_name in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidate_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].split(', '):
            candidates.append(candidate)
    return candidates

