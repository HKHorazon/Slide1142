---
description: List all available slash commands and their descriptions
---

1. List all slash commands
// turbo
Get-ChildItem -Path ".agent/workflows" -Filter "*.md" | Select-Object @{Name="Command"; Expression={"/" + $_.BaseName}}, @{Name="Description"; Expression={($_ | Get-Content | Select-String "description:").ToString().Split(":", 2)[1].Trim()}} | Format-Table -AutoSize
