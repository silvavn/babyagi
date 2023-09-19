# Task Prioritization

## You are tasked with prioritizing the following tasks

```plaintext
    {TASK_PRIORITY_LIST}
```

Consider the ultimate objective of your team:

```plaintext
    {OBJECTIVE}
```

Tasks should be sorted from highest to lowest priority, where higher-priority tasks are those that act as pre-requisites or are more essential for meeting the objective.

Do not remove any tasks. Return the ranked tasks as a numbered list in the format:

```plaintext
    $first_task
    $second_task
    ...
    $nth_task
...

The entries must be consecutively numbered, starting with 1. The number of each entry must be followed by a period.
Do not include any headers before your ranked list or follow your list with any other output.
