<h1>Postmortem: Web Stack Outage - Unauthorized Access Error</h1>

<img src="./assets/INCIDDENT.gif" alt="Postmortem" />

<details>
	<summary>
    <b>
      Issue Summary:
    </b>
  </summary>
	<br/>
    <h2>
        Duration: May 12, 2024, 09:00 AM - May 12, 2024, 10:30 AM (UTC)
    </h2>
    <p>
        Impact: The web application experienced an outage resulting in users receiving 401 (Unauthorized) errors when accessing the "/api/users/getUser" endpoint. The service was completely down during the outage, affecting approximately 50% of the users trying to access the getUser API.
        Root Cause: The issue was caused by a misconfiguration in the access control rules of the authentication middleware.
    </p>
   <br/>
    <h2>
        Timeline:
    </h2>
    <p>
        09:00 AM: The issue was detected when users started reporting 401 errors while accessing the getUser API.
        Actions taken: The engineering team investigated the system logs and reviewed the authentication middleware. The initial assumption was that the issue was related to a recent code deployment that might have introduced a bug.
        Misleading investigation: The team spent time reviewing the recent code changes and rolled back to a previous version, but the issue persisted.
        Escalation: The incident was escalated to the security team to investigate potential security vulnerabilities or unauthorized access attempts.
        10:00 AM: The incident was resolved after identifying the misconfiguration in the access control rules.
        Resolution: The misconfiguration was fixed by updating the access control rules to allow proper authentication and access to the getUser API.
    </p>
    <br/>
    <h2>
        Root Cause and Resolution:
    </h2>
    <p>
    The root cause of the issue was a misconfiguration in the access control rules of the authentication middleware. This misconfiguration caused the middleware to reject valid user requests, resulting in 401 (Unauthorized) errors. The issue was resolved by updating the access control rules to properly authenticate and authorize user requests.
    </p>
    <br/>
    <h2>
        Corrective and Preventative Measures:
    </h2>
    <p>
        To prevent similar issues in the future, the following actions will be taken:
        Conduct a thorough review of the access control rules and configurations to ensure they align with the intended security policies.
        Implement automated tests to validate the functionality of the authentication middleware, including proper handling of authorized and unauthorized requests.
        Enhance monitoring and alerting systems to proactively detect and notify the team about unauthorized access attempts or misconfigurations.
        Provide additional training to the engineering team on secure coding practices and the proper configuration of access control rules.
    </p>
    <br/>
    <h2>
        Tasks to Address the Issue:
    </h2>
    <p>
        Review and update access control rules in the authentication middleware.
        Implement automated tests to verify the functionality of the authentication middleware.
        Enhance monitoring and alerting systems to detect unauthorized access attempts and misconfigurations.
        Conduct regular security audits to identify and address potential vulnerabilities.
        Provide training sessions for the engineering team on secure coding practices and access control configuration.
    </p>
    <br/>
    <p>
    By implementing these corrective measures and addressing the identified tasks, we aim to prevent similar unauthorized access errors in the future and ensure a more secure and reliable web stack.
    </p>
</details>