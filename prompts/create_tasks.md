# Task Creation

## Create new tasks with the following objective

```plaintext
    {OBJECTIVE}
```

The last completed task has the following result:

```plaintext
    {LAST_RESULT}
```

This result was based on the following task description:

```plaintext
    {TASK_DESCRIPTION}
```

Based on the result and on the incomplete task list, make a list of new tasks that must be completed to achieve the results. The new tasks must NOT overlap with the list fo completed or incomplete tasks.

Return one task per line in your response. The result must be a numbered list in the format:

```plaintext
    $first_task
    $second_task
    ...
    $nth_task
```

The number of each entry must be followed by a period. If your list is empty, return an `<no_tasks>` tag.
