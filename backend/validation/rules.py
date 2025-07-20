def run_validations(config: dict) -> str:
    """
    Runs static validation rules over the parsed config dict.
    Returns a human-readable string of all issues found.
    """
    issues = []

    # Flatten nested keys for easier checking
    def walk(d, path=[]):
        for k, v in d.items():
            current_path = path + [k]
            if isinstance(v, dict):
                yield from walk(v, current_path)
            else:
                yield (".".join(current_path), v)

    flat_config = dict(walk(config))

    # Rule 1: public IP on EC2
    for key in flat_config:
        if "associate_public_ip_address" in key and flat_config[key] == True:
            issues.append({
                "type": "Security",
                "message": f"{key} is set to true — this exposes the instance to the internet.",
                "severity": "high"
            })

    # Rule 2: missing tags
    if "tags" not in flat_config and not any("tags." in k for k in flat_config.keys()):
        issues.append({
            "type": "BestPractice",
            "message": "No tags found on resources. Tags are recommended for cost tracking and environment labeling.",
            "severity": "medium"
        })

    # Rule 3: unversioned S3 bucket
    if "versioning.enabled" in flat_config and flat_config["versioning.enabled"] == False:
        issues.append({
            "type": "Compliance",
            "message": "S3 bucket versioning is disabled — this can lead to data loss.",
            "severity": "medium"
        })

    # Rule 4: open security group
    for key, value in flat_config.items():
        if "cidr_blocks" in key and ("0.0.0.0/0" in str(value) or "::/0" in str(value)):
            issues.append({
                "type": "Security",
                "message": f"{key} allows traffic from all IPs (0.0.0.0/0). This is insecure.",
                "severity": "high"
            })

    if not issues:
        return "✅ No validation issues found."

    report = ["❗Validation Results:"]
    for issue in issues:
        report.append(f"- [{issue['severity'].upper()}] {issue['type']}: {issue['message']}")

    return "\n".join(report)
