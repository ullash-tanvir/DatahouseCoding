from flask import Flask, request, jsonify

app = Flask(__name__)

def score_applicants(applicants ):
    max_value=10 
    min_value=1
    scored_applicants = [] # list of the appilicants with their name and compatibility score
    for applicant in applicants:
        normalized_value_list= [] 
        for attribute, value in applicant['attributes'].items():
            normalized_value_list.append((value - min_value) / (max_value - min_value)) # normalizing all the attribute values with min-max approach
        compatibility = round(sum(normalized_value_list)/4,2) # Calculating compatibility score with average of the normalized value
        scored_applicants.append({'name': applicant['name'], \
                                  'compatibility':compatibility })
    return {'scoredApplicants': scored_applicants}

@app.route('/', methods=['POST'])
def process_json():
    # Read in the input JSON file
    input_data = request.get_json(force=True)
    output_data = score_applicants( input_data['applicants'])
    print(output_data)
    return jsonify(output_data)

if __name__ == '__main__':
    app.run(debug=True)
