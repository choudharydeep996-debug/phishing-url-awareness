
import re
from urllib.parse import urlparse


# ==============================================
# EWB PHISHING URL AWARENESS CHECKER
# ==============================================

def inspect_url(raw_url):
    """
    Analyze URL text for six selected phishing warning signs.
    This program never opens or visits a URL.
    """

    url = raw_url.strip()

    if not url:
        return "info", [], "No URL entered."

    # Add a scheme if the user has not provided one
    candidate = url if "://" in url else "http://" + url

    # Parse URL safely
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()

    except ValueError:
        return (
            "invalid",
            [],
            "This text is not a valid URL format."
        )

    if not host:
        return (
            "invalid",
            [],
            "Could not identify a hostname."
        )

    findings = []

    # CHECK 1: @ SYMBOL
    if "@" in candidate:
        findings.append((
            "Contains an @ symbol; inspect carefully.",
            "Text before @ can make a URL appear to belong "
            "to one website while its actual hostname is different."
        ))

    # CHECK 2: URL LENGTH
    if len(url) > 100:
        findings.append((
            "Unusually long URL (over 100 characters).",
            "Long URLs can hide the important destination "
            "or make the link difficult to inspect."
        ))

    # CHECK 3: IP ADDRESS
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append((
            "Uses an IP address instead of a familiar domain.",
            "A numerical address can make the destination "
            "less recognizable."
        ))

    # CHECK 4: HOSTNAME SEGMENTS
    labels = [part for part in host.split(".") if part]

    if len(labels) >= 5:
        findings.append((
            "Contains many hostname segments/subdomains.",
            "Many hostname parts can make a destination "
            "look complicated or misleading."
        ))

    # CHECK 5: PUNYCODE
    if "xn--" in host:
        findings.append((
            "Contains a punycode-style hostname.",
            "Punycode can represent special characters "
            "that may resemble familiar website names."
        ))

    # CHECK 6: HTTP
    if parsed.scheme.lower() == "http":
        findings.append((
            "Uses HTTP. HTTPS alone does not prove trust.",
            "HTTP does not encrypt the connection like HTTPS."
        ))

    if findings:
        return "warning", findings, ""

    return "clean", [], ""


def display_result(raw_url):
    """Display the analysis in a readable format."""

    status, findings, message = inspect_url(raw_url)

    print("\n" + "=" * 60)
    print("                  SCAN RESULT")
    print("=" * 60)

    if status == "info":
        print("[INFO]", message)

    elif status == "invalid":
        print("[INVALID URL]", message)

    elif status == "warning":

        print("STATUS: REVIEW CAREFULLY")
        print(f"Warning indicators found: {len(findings)}")

        print("-" * 60)

        for number, (warning, explanation) in enumerate(
            findings, start=1
        ):
            print(f"\n{number}. [!] {warning}")
            print(f"   Why it matters: {explanation}")

        print("\n" + "-" * 60)
        print(
            f"SUMMARY: {len(findings)} possible warning "
            "sign(s) detected."
        )
        print("Recommendation: Review this URL carefully.")

    elif status == "clean":

        print("STATUS: NO LISTED WARNING SIGNS")
        print("No listed warning signs were detected.")
        print("This does NOT prove that the URL is safe.")

    print("=" * 60)


def main():

    print("\n" + "=" * 60)
    print("          EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 60)

    print("Purpose: Identify selected URL warning signs.")
    print("Mode: Text analysis only.")
    print("Safety: This program never opens websites.")

    print("\nInstructions:")
    print("- Enter a URL to analyze it.")
    print("- Type q to quit the program.")

    # Continuous URL checking
    while True:

        try:
            raw_url = input(
                "\nEnter a sample URL (or q to quit): "
            )

        except (KeyboardInterrupt, EOFError):
            print("\nProgram stopped safely.")
            break

        # Quit option
        if raw_url.strip().lower() in ("q", "quit", "exit"):
            print("\nThank you for using EWB URL Checker.")
            print("Stay alert and stay safe online.")
            break

        # Analyze and display results
        display_result(raw_url)


# Start the program
if __name__ == "__main__":
    main()
