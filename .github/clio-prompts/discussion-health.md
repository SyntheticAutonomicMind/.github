# Discussion Health Analysis Instructions - HEADLESS CI/CD MODE

## CRITICAL: HEADLESS OPERATION

**YOU ARE IN HEADLESS CI/CD MODE:**
- NO HUMAN IS PRESENT
- DO NOT use user_collaboration - it will hang forever
- DO NOT ask questions - nobody will answer
- DO NOT checkpoint - this is automated
- JUST READ FILES AND WRITE JSON TO FILE

## Your Task

1. Read `DISCUSSIONS_REPORT.md` for all open discussions
2. Read `NEEDS_ATTENTION.md` for unanswered Q&A discussions
3. Read `NO_RESPONSES.md` for discussions with no responses
4. **WRITE your analysis to `/workspace/health-report.json` using file_operations**

## Analysis Goals

- **Identify trends:** Are there recurring topics? Common questions?
- **Flag urgent items:** Unanswered questions older than 3 days
- **Suggest improvements:** Categories that need attention, common issues
- **Calculate health score:** Overall community engagement assessment

## Health Score Criteria

- **excellent:** All Q&A answered, active community engagement, <3 days average response time
- **good:** Most Q&A answered, regular engagement, <5 days average response time
- **fair:** Some unanswered questions, moderate engagement, <7 days average response time
- **needs-attention:** Multiple unanswered questions, low engagement, >7 days response time
- **poor:** Many unanswered questions, minimal engagement, discussions going stale

## Output - WRITE TO FILE

**CRITICAL: Write your analysis to `/workspace/health-report.json` using file_operations**

```json
{
  "total_open": 10,
  "unanswered_qa": 2,
  "no_responses": 3,
  "health_score": "good",
  "needs_attention": 5,
  "trends": ["Feature requests increasing", "Documentation questions common"],
  "urgent_items": [
    {"number": 5, "title": "Question about X", "days_old": 5, "action": "needs-response"}
  ],
  "recommendations": [
    "Consider adding FAQ for common questions",
    "Close resolved discussions that are still open"
  ],
  "summary": "Community health is good. 2 Q&A discussions need responses."
}
```

## REMEMBER

- NO user_collaboration (causes hang)
- NO questions (nobody will answer)
- Read the files, analyze, **WRITE JSON TO /workspace/health-report.json**
- Use file_operations to create the file
- Focus on actionable insights, not just metrics
