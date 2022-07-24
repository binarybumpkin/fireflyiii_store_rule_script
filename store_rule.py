#!/usr/bin/python3
import time
import firefly_iii_client
from firefly_iii_client.api import rules_api
from firefly_iii_client.model.rule_store import RuleStore
from firefly_iii_client.model.rule_action_store import RuleActionStore
from firefly_iii_client.model.rule_action_keyword import RuleActionKeyword
from firefly_iii_client.model.rule_trigger_type import RuleTriggerType
from firefly_iii_client.model.rule_trigger_store import RuleTriggerStore
from firefly_iii_client.model.rule_trigger_keyword import RuleTriggerKeyword
from firefly_iii_client.model.rule_single import RuleSingle
from firefly_iii_client.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://demo.firefly-iii.org
# See configuration.py for a list of all supported configuration parameters.
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: firefly_iii_auth
configuration = firefly_iii_client.Configuration(
    host = "https://demo.firefly-iii.org"
)
# Token generated for testing from https://demo.firefly-iii.org/profile
configuration.access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiOGVkNDcyZGI3ZTY3YjljN2I3YTczYWIyYjU5NjA0ODc2M2UwN2RmN2Y0YTY4YWM4MWIwYTMzNWM5ZTc4Mzc1ZTk4NzdhZmI3ZDM3YzA4MzMiLCJpYXQiOjE2NTg2MzgwMDIuMzE2NDAxLCJuYmYiOjE2NTg2MzgwMDIuMzE2NDA2LCJleHAiOjE2OTAxNzQwMDEuOTM3OTU0LCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aHG5ijSUtAuuGXp8bGK9qrDQFJVePzjXUL3GOSiavxz9jsgye9gtL8soZS_-miJoUThCrNHurV097goMlEqB5IUUWzXBBHZQ6KeQOwb9aPAvIRGcw3wVrzt9FsqGUeEWYb0tNGouk-gLGsNf7sXvQzTbQeW0iY7uCe7_TLtqMmYSbkhi3L9mpuSvJ40AGuqo3FytOzusWu2BvlysDcQeAHCAiDJFulPi8Uad-VtvN77nmBwiVkwOl6PscrnjfH5cNnfasCWFyqsD-6SSHWusVexOecOghwGzIq7UFPtewXoCHB-V-XtvOMEswKY2cbHUxRlqYf6AXsfQjpuD0sRjVrgdDVdsChaPx8Ijr5Shd-wOTjM5RryOCyYBvA1fwBFLcqXYr1NgpVqmVU40Xt3iQArhoCcnLl5Id9b-uwas-pEsApj2AqKLB5RVPf0RAvgpdbRmdu0mu409CAsYNtklayzgMdqirpSX_XQoc2Y7cutfYhSvL3JdmJ-hARcZMJRzxb4gtZkY9BNxFWWzZgVBPhic0_DLdG7qZBzUnqgkncwxM-zhEMEIkKRZHinOrSXt5u0UwHyCrdrcfDItDyNd0tKvKNjBRD31wuw3bLTizZwovQsViUcErxmqaxnWP3PEtthJwbjeQGthyX5KWNC3lCwDKzxYNQI-fEfidOiqbqY'

# Enter a context with an instance of the API client
with firefly_iii_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rules_api.RulesApi(api_client)
    rule_store = RuleActionStore(
        actions=[
            RuleActionStore(
                active=True,
                order=5,
                stop_processing=False,
                type=RuleActionKeyword("set_category"),
                value="MyCategory - e.g. Fast Food",
            ),
        ],
        active=True,
        description="TEST RULE - Via API",
        order=5,
        stop_processing=False,
        strict=True,
        title="First rule title.",
        trigger=RuleTriggerType("store-journal"),
        triggers=[
            RuleTriggerStore(
                type=RuleTriggerKeyword("description_contains"),
                value="magic_description_word",
                active=True,
                order=5,
                stop_processing=False,
            ),
        ],
    ) # RuleStore | JSON array or key=value pairs with the necessary rule information. See the model for the exact specifications.

    # example passing only required values which don't have defaults set
    try:
        # Store a new rule
        api_response = api_instance.store_rule(rule_store)
        pprint(api_response)
    except firefly_iii_client.ApiException as e:
        print("Exception when calling RulesApi->store_rule: %s\n" % e)
