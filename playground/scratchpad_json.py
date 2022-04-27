import json
import json.decoder
import requests
import plotext as plt
import argparse


parser = argparse.ArgumentParser(description="Plot a job to triage")
parser.add_argument('--job', type=str, metavar='', required=True, help='Job type')
args = parser.parse_args()

if args.job == "sanity":
    print("Triaging Sanity Jobs")
    jenkins_json = requests.get("https://mobile-jenkins-sxmp.savagebeast.com/job/apple-apps-px-ios-prod-sanity/job/develop/api/json")
elif args.job == 'synthetic':
    print("Triaging Synthetic Jobs")
    jenkins_json = requests.get("https://mobile-jenkins-sxmp.savagebeast.com/job/apple-apps-px-ios-prod-synthetic/job/develop/api/json")
else:
    print("Unidentified job")
    quit()

# print(jenkins_json.text)
json_object = json.loads(jenkins_json.text)
json_pretty = json.dumps(json_object, indent=2)
# print(json_pretty)

builds = []
passed = []
failed = []
for line in json_object['builds']:
    builds_number = line['number']
    builds.append(str(builds_number))
    builds_url = line['url']
    build_test_data = requests.get(builds_url + '/testReport/api/json').text
    try:
        build_test_json = json.loads(build_test_data)
    except json.decoder.JSONDecodeError:
        continue
    build_test_json_pretty = json.dumps(build_test_json, indent=2)
    # print(build_test_json_pretty)
    # print(f"BUILD: {builds_number}")

    for test_key in build_test_json['suites']:
        pass_number = 0
        fail_number = 0
        for tests in test_key['cases']:
            # if tests['className'].startswith("System Failures"):
            if tests['className']
                continue
            # print(f"TEST: {tests['className']}.{tests['name']}, STATUS: {tests['status']}")
            if tests['status'] in ['PASSED', 'FIXED']:
                pass_number += 1
            else:
                fail_number += 1
        passed.append(pass_number)
        failed.append(fail_number)

#     print()
# print(builds, passed, failed)


plt.multiple_bar(builds, [passed, failed], color=["green", "red"], label=["Passed", "Failed"])
plt.yticks(range(1,50))
plt.ylabel("Tests")
plt.xlabel("Builds")
plt.canvas_color("black")
if args.job == "synthetic":
    plt.title("Synthetic")
else:
    plt.title("Sanity")
plt.show()
