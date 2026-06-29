# Instructor Guide

This addon is intentionally broken for sequential Odoo debugging practice.

## Error 1: Python Import Error

File: `models/__init__.py`

Broken:

```python
from . import practice_tickets
```

Fix:

```python
from . import practice_ticket
```

## Error 2: Field Not Found In XML View

File: `views/error_practice_views.xml`

Broken:

```xml
<field name="assigned_user_id"/>
```

Fix option:

Add this field in `models/practice_ticket.py`:

```python
assigned_user_id = fields.Many2one("res.users", string="Assigned To")
```

## Error 3: Access Rights External ID Error

File: `security/ir.model.access.csv`

Broken:

```csv
model_error_practice_task
```

Fix:

```csv
model_error_practice_ticket
```

## Error 4: Compute Method Failed To Assign

File: `models/practice_ticket.py`

Broken method does not assign `remaining_hours` when `expected_hours` is zero.

Fix:

```python
@api.depends("expected_hours", "spent_hours")
def _compute_remaining_hours(self):
    for record in self:
        record.remaining_hours = record.expected_hours - record.spent_hours
```

## Error 5: Button Method Not Working

File: `views/error_practice_views.xml`

Button calls:

```xml
<button name="action_start" type="object" string="Start"/>
```

But Python has:

```python
def action_mark_start(self):
```

Fix option:

Rename Python method to:

```python
def action_start(self):
    self.write({"state": "in_progress"})
```
