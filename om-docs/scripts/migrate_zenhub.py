#!/usr/bin/python
"""

    Import Github issues from one repo to another.

    The orignal work: https://github.com/mkorenkov/tools/blob/master/gh-issues-import/gh-issues-import.py
    (assuming public domain license).

    Used to migrate Github's Plone Conference 2012 temporary repository
    to collective.developermanual issues.

    NOTE: Comments are imported, but their author is not preserved.

"""

import os

import urllib2
import json
from StringIO import StringIO
import base64


#==== configurations =======
username = os.environ.get("GH_USER", None)
if not username:
    raise RuntimeError("Set environment variable GH_USER to your github user")

# set up a personal access token for this:
password = os.environ.get("GH_PASS", None)
if not password:
    raise RuntimeError("Set environment variable GH_PASS (access token)")

src_repo = "developer-journeys/journey-template"
dst_repo = os.environ.get("GH_REPO", None)
if not dst_repo:
    raise RuntimeError("Set environment variable GH_REPO to your new repo ex: journey/bacon")

#==== end of configurations ===

server = "github.ibm.com/api/v3"
src_url = "https://%s/repos/%s" % (server, src_repo)
dst_url = "https://%s/repos/%s" % (server, dst_repo)

print "Prepared to move issues\n FROM: %s\n   TO: %s" % (src_url, dst_url)
raw_input("Press Enter to continue...")

def get_milestones(url):
    req = urllib2.Request("%s/milestones" % url)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    response = urllib2.urlopen(req)
    result = response.read()
    milestones = json.load(StringIO(result))
    return milestones


def get_labels(url):
    req = urllib2.Request("%s/labels" % url)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    response = urllib2.urlopen(req)
    result = response.read()
    labels = json.load(StringIO(result))
    return labels


def get_issues(url):
    index = 1
    issues = []
    while True:
        req = urllib2.Request("%s/issues?state=open" % (url, ))
        req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
        response = urllib2.urlopen(req)
        result = response.read()
        new_issues = json.load(StringIO(result))
        # print new_issues
        print 'Loaded issues ', index, len(new_issues)

        #req = urllib2.Request("%s/issues?state=closed" % (url, ))
        #req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
        #response = urllib2.urlopen(req)
        #result = response.read()
        #new_issues += json.load(StringIO(result))
        # print new_issues
        #print 'Loaded issues ', index, len(new_issues)

        issues += new_issues
        index += 1
        break
    tissues = [(x['number'],x) for x in issues]
    tissues.sort()
    issues = [y for x,y in tissues]
    return issues



def find_issue_by_title(issues, title):
    for issue in issues:
        if title == issue['title']:
            return issue['number']
    return False

def find_issue_by_number(issues, number):
    for issue in issues:
        if number == issue['number']:
           return issue
    return None

def get_comments_on_issue(issue):
    if "comments" in issue \
      and issue["comments"] is not None \
      and issue["comments"] != 0:
        req = urllib2.Request("%s/comments" % issue["url"])
        req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
        response = urllib2.urlopen(req)
        result = response.read()
        comments = json.load(StringIO(result))
        return comments
    else:
        return []


def import_milestones(milestones):
    for source in milestones:
        dest = json.dumps({
            "title": source["title"],
            "state": "open",
            "description": source["description"],
            "due_on": source["due_on"]})

        req = urllib2.Request("%s/milestones" % dst_url, dest)
        req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json")
        res = urllib2.urlopen(req)

        data = res.read()
        res_milestone = json.load(StringIO(data))
        print "Successfully created milestone %s" % res_milestone["title"]

def label_names(extract_labels):
    labels = []
    for label in extract_labels:
        labels.append(label["name"])
    return labels

def import_labels(src_labels, dst_labels):
    for source in src_labels:
        if source["name"] not in dst_labels:
            dest = json.dumps({
                "name": source["name"],
                "color": source["color"]
            })
            req = urllib2.Request("%s/labels" % dst_url, dest)
            req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
            req.add_header("Content-Type", "application/json")
            req.add_header("Accept", "application/json")
            res = urllib2.urlopen(req)

            data = res.read()
            res_label = json.load(StringIO(data))
            print "  Successfully created label %s" % res_label["name"]
        else:
            print "  label %s already exists in destination" % source["name"]

def import_issues(src_issues, dst_issues,dst_milestones, dst_labels):
    for source in src_issues:
        print "Importing issue %s" % (source["title"],)
        import_issue(source, dst_issues,dst_milestones, dst_labels)
        print ""


def import_issue(source, dst_issues,dst_milestones, dst_labels):
    dst_issue = find_issue_by_number(dst_issues,source['number'])
    #if dst_issue is not None:
    #    print 'issue %d, %s,  already exists with title %s'%(source['number'],source['title'],dst_issue['title'])
    #return

    labels = []
    if source.has_key("labels"):
        for src_label in source["labels"]:
            name = src_label["name"]
            for dst_label in dst_labels:
                if dst_label["name"] == name:
                    labels.append(name)
                    break

    milestone = None
    if source.has_key("milestone") and source["milestone"] is not None:
        title = source["milestone"]["title"]
        for dst_milestone in dst_milestones:
            if dst_milestone["title"] == title:
                milestone = dst_milestone["number"]
                break

    assignee = None
    if source.has_key("assignee") and source["assignee"] is not None:
        assignee = source["assignee"]["login"]

    body = None
    if source.has_key("body") and source["body"] is not None:
        body = source["body"]

    # Create issue
    if dst_issue is None:
        res_issue = create_issue(dst_url, source["title"], body, assignee, milestone, labels)
    else:
        res_issue = edit_issue(dst_url, source['number'],
                               source["title"], body, assignee, milestone, labels)

    if not res_issue:
        return

    # Transfer comments
    comments = get_comments_on_issue(source)
    import_comments(dst_url, res_issue, comments)

    # Close issue if required
    if source['state'] == 'closed':
        close_issue(dst_url, res_issue)




def create_issue(url, title, body, assignee, milestone, labels):
    dest = json.dumps({
        "title": title,
        "body": body,
        "assignee": assignee,
        "milestone": milestone,
        "labels": labels
    })
    req = urllib2.Request("%s/issues" % url, dest)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError:
        # urllib2.HTTPError: HTTP Error 422: Unprocessable Entity
        print "  Could not process the issue %s" % dest
        return

    data = res.read()
    res_issue = json.load(StringIO(data))
    print "  Successfully created issue %s (%s)" % (res_issue["title"], res_issue["number"])
    return res_issue

def edit_issue(url, number, title, body, assignee, milestone, labels):
    dest = json.dumps({
        "title": title,
        "body": body,
        "assignee": assignee,
        "milestone": milestone,
        "labels": labels
    })
    req = urllib2.Request("%s/issues/%d" % (url,number), dest)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    req.get_method = lambda: 'PATCH'
    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError:
        # urllib2.HTTPError: HTTP Error 422: Unprocessable Entity
        print "  Could not process the issue %s" % dest
        return

    data = res.read()
    res_issue = json.load(StringIO(data))
    print "  Successfully created issue %s (%s)" % (res_issue["title"], res_issue["number"])
    return res_issue




def close_issue(url, issue):
    dest = json.dumps({"state": "closed"})
    req = urllib2.Request("%s/issues/%s" % (url, issue["number"]), dest)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print res.read()
        # urllib2.HTTPError: HTTP Error 422: Unprocessable Entity
        print "  Could not process the issue %s" % dest
        return

    data = res.read()
    res_issue = json.load(StringIO(data))
    print "  Successfully closed issue %s (%s)" % (issue["title"], issue["number"])



def import_comments(url, issue, comments):
    for comment in comments:
        import_comment(url, issue['number'], comment)
    print "  Successfully imported comments in %s (%s)" % (issue["title"], str(issue["number"]))


def import_comment(url, issue_number, comment):

    dest = json.dumps({"body": comment["body"]})
    req = urllib2.Request("%s/issues/%s/comments" % (url, issue_number), dest)
    req.add_header("Authorization", "Basic " + base64.urlsafe_b64encode("%s:%s" % (username, password)))
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json")
    try:
        res = urllib2.urlopen(req)
    except urllib2.HTTPError:
        print res.read()
        # urllib2.HTTPError: HTTP Error 422: Unprocessable Entity
        print "  Could not process the comment %s" % dest
        return

    data = res.read()
    res_issue = json.load(StringIO(data))
    print "  Successfully posted comment in issue %s" % (issue_number)



def main():
    #get milestones and issues to import
    #print "  Loading milestones from source"
    milestones = get_milestones(src_url)

    print "Loading labels from source"
    labels = get_labels(src_url)

    dst_labels = label_names(get_labels(dst_url))

    print "Importing labels to destination"
    import_labels(labels, dst_labels)

    #get imported milestones and labels
    #dst_milestones = get_milestones(dst_url)
    dst_labels = get_labels(dst_url)

    #process issues
    print "  Loading issues from source"
    src_issues = get_issues(src_url)
    print "  Loading issues from destination"
    dst_issues = get_issues(dst_url)
    import_issues(src_issues, dst_issues, milestones, labels)

if __name__ == '__main__':
    main()
