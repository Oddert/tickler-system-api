from pydantic import BaseModel, Field


class PromptPost(BaseModel):
    """Represents a POST or PUT request to Prompt."""

    # checklist: str=Field(...)
    criticality: str = (
        Field(
            'default',
            title='The criticality rating.',
            description='Criticality must be one of "default", "severe", "reminder", "reference".',
            pattern='^(severe|default|reminder|reference)$',
        ),
    )
    date: str = (
        Field(
            ...,
            title='Prompt schedule date.',
            description='The date the prompt is scheduled for.',
            max_length=55,
            min_length=6,
        ),
    )
    deferPeriod: str = (
        Field(
            'week',
            title='The date period.',
            description='The unit time period quantified by deferQuantity.',
            pattern='^(day|month|year)$',
        ),
    )
    deferQuantity: int = (
        Field(
            2,
            title='The defer quantity.',
            description='The number of units to defer by.',
            min=1,
            max=999,
        ),
    )
    description: str | None = (
        Field(
            default=None,
            title='Prompt description.',
            description='A longer form description field.',
            min_length=0,
            max_length=2000,
        ),
    )
    # links: str=Field(...)
    status: str = (
        Field(
            'open',
            title='Active status.',
            description='The active status of the prompt. Must be one of "open", "resolved", "archived", "deleted".',
            pattern='^(open|resolved|archived|deleted)$',
        ),
    )
    title: str = (
        Field(
            ...,
            title='The prompt title.',
            description='The main title for the prompt.',
            min_length=3,
            max_length=250,
        ),
    )


class PromptPut(PromptPost):
    """Represents a POST or PUT request to Prompt."""

    # checklist: str=Field(...)
    deferredCount: int = Field(
        0,
        title='The defer count.',
        description='The number of times the prompt has been deferred.',
        min=0,
    )


class PromptDefer(BaseModel):
    """Represents a PUT request to defer a Prompt."""

    deferredCount: int = Field(
        0,
        title='The defer count.',
        description='The number of times the prompt has been deferred.',
        min=0,
    )
    deferPeriod: str = (
        Field(
            'week',
            title='The date period.',
            description='The unit time period quantified by deferQuantity.',
            pattern='^(day|month|year)$',
        ),
    )
    deferQuantity: int = (
        Field(
            2,
            title='The defer quantity.',
            description='The number of units to defer by.',
            min=1,
            max=999,
        ),
    )
